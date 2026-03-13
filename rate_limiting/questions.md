# Rate Limiting Interview Questions (27 Questions - Mid to Advanced)

> Curated from Google, Amazon, Stripe, Meta interviews
> Languages: Python (implementations) + Redis (distributed)

---

## Section A: Token Bucket (Q1-Q3)

### Q1. Token Bucket - Concept [Mid]
**Explain the Token Bucket algorithm. How does it handle burst traffic?**

Walk through: bucket capacity = 20, refill rate = 10/sec, client sends 50 requests in 1 second.

- Bucket starts full (20 tokens)
- First 20 requests: allowed (bucket empties)
- Next requests: denied until tokens refill (10/sec)
- Key insight: allows BURSTS up to bucket capacity, then enforces steady rate

---

### Q2. Token Bucket - Implementation [Advanced]
**Implement a thread-safe TokenBucketRateLimiter with lazy refill.**

```python
import time
import threading

class TokenBucket:
    def __init__(self, max_tokens: int, refill_rate: float):
        self.max_tokens = max_tokens
        self.refill_rate = refill_rate  # tokens per second
        self.tokens = max_tokens
        self.last_refill = time.monotonic()
        self.lock = threading.Lock()

    def allow_request(self) -> bool:
        with self.lock:
            now = time.monotonic()
            elapsed = now - self.last_refill
            self.tokens = min(
                self.max_tokens,
                self.tokens + elapsed * self.refill_rate
            )
            self.last_refill = now

            if self.tokens >= 1:
                self.tokens -= 1
                return True
            return False
```

**Follow-up:** Why use `time.monotonic()` instead of `time.time()`?
*Answer: monotonic clock is immune to NTP corrections / clock adjustments.*

---

### Q3. Token Bucket - Capacity Tuning [Advanced]
**How do you decide bucket capacity and refill rate for a production API?**

- Bucket capacity = max burst size you're willing to tolerate
- Refill rate = sustained throughput you want to allow
- Too large bucket = abuse potential during bursts
- Too small bucket = legitimate burst traffic gets rejected
- Inputs: SLA, server capacity, p99 latency targets, business requirements

---

## Section B: Leaky Bucket (Q4-Q6)

### Q4. Token Bucket vs Leaky Bucket [Mid]
**Compare them. When is Leaky Bucket strictly better?**

| Feature | Token Bucket | Leaky Bucket |
|---------|-------------|-------------|
| Burst handling | Allows bursts up to capacity | Smooths ALL traffic to constant rate |
| Output rate | Variable (bursty) | Constant (steady) |
| Implementation | Counter-based | Queue-based (FIFO) |
| Best for | General API rate limiting | Video streaming, payment processing |

*Leaky Bucket is better when downstream systems need CONSTANT input rate (e.g., payment gateway that processes exactly 100 txn/sec).*

---

### Q5. Leaky Bucket - Implementation [Advanced]
**Implement a Leaky Bucket using a FIFO queue.**

```python
import time
from collections import deque

class LeakyBucket:
    def __init__(self, capacity: int, leak_rate: float):
        self.capacity = capacity
        self.leak_rate = leak_rate  # requests processed per second
        self.queue = deque()
        self.last_leak = time.monotonic()

    def allow_request(self, request_id: str) -> bool:
        self._leak()
        if len(self.queue) < self.capacity:
            self.queue.append(request_id)
            return True
        return False  # Queue full, drop request

    def _leak(self):
        now = time.monotonic()
        elapsed = now - self.last_leak
        leaked = int(elapsed * self.leak_rate)
        for _ in range(min(leaked, len(self.queue))):
            self.queue.popleft()
        if leaked > 0:
            self.last_leak = now
```

---

### Q6. Leaky Bucket - Latency Impact [Mid]
**What happens to latency during a burst? How do you communicate rate limiting to clients?**

- During burst: requests queue up, latency increases linearly with queue depth
- HTTP headers to communicate: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `Retry-After`
- HTTP status: `429 Too Many Requests`

---

## Section C: Fixed Window Counter (Q7-Q9)

### Q7. Boundary Burst Problem [Advanced]
**Rate limit = 100 req/min. Show how a client can send 200 requests in ~1 second.**

```
Window 1: [0:00 - 0:59]    Window 2: [1:00 - 1:59]
                     ↑ 100 requests at 0:59
                       100 requests at 1:00 ↑
```

Client sends 100 at 0:59 (end of window 1) + 100 at 1:00 (start of window 2) = **200 requests in 1 second**, but each window only sees 100.

---

### Q8. Fixed Window in Redis [Advanced]
**Implement using Redis. Why is GET-then-SET unsafe?**

```
-- WRONG (race condition):
GET counter → 99
-- another thread: GET counter → 99
SET counter 100
-- another thread: SET counter 100 (both allowed!)

-- CORRECT (atomic):
INCR counter
-- if result == 1, set EXPIRE
-- OR use Lua script:
```

```lua
local count = redis.call('INCR', KEYS[1])
if count == 1 then
    redis.call('EXPIRE', KEYS[1], ARGV[1])
end
return count
```

---

### Q9. Distributed Fixed Window Problem [Advanced]
**4 API gateway instances, each with local counters. Limit = 100. What goes wrong?**

Each instance allows 100 → total = 400 requests (4x the limit).

**Fixes:**
1. Centralized store (Redis) -- simple but adds latency + SPOF
2. Sticky sessions (route same client to same instance) -- uneven load
3. Distributed counter with eventual consistency -- allows slight over-admission

---

## Section D: Sliding Window Log (Q10-Q12)

### Q10. Sliding Window Log - Concept [Mid]
**Why is it more accurate? What's the memory problem?**

- Stores timestamp of every request in the window
- Always checks last N seconds (truly sliding)
- Memory: 10K users x 1K req/min = **10 million timestamps in memory**
- Accurate but expensive at scale

---

### Q11. Sliding Window Log in Redis [Advanced]
**Implement using Redis Sorted Set. Write the Lua script.**

```lua
local key = KEYS[1]
local now = tonumber(ARGV[1])
local window = tonumber(ARGV[2])
local limit = tonumber(ARGV[3])

-- Remove expired entries
redis.call('ZREMRANGEBYSCORE', key, 0, now - window)

-- Count remaining
local count = redis.call('ZCARD', key)

if count < limit then
    -- Add current request
    redis.call('ZADD', key, now, now .. '-' .. math.random())
    redis.call('EXPIRE', key, window)
    return 1  -- allowed
else
    return 0  -- denied
end
```

**Why atomic?** Without atomicity, two concurrent requests could both see count=99 (limit=100), both add → 101.

---

### Q12. Optimizing Sliding Window Log [Advanced]
**How to reduce memory while keeping accuracy?**

- Bucket timestamps by second (not millisecond) → 60 entries per minute max instead of thousands
- Trade-off: lose sub-second precision
- Hybrid: use per-second counters with sliding window math

---

## Section E: Sliding Window Counter (Q13-Q14)

### Q13. Sliding Window Counter - Concept [Advanced]
**How does it combine Fixed Window efficiency with Sliding Window accuracy?**

Formula:
```
estimated_count = current_window_count + (previous_window_count * overlap_percentage)
```

Example: limit=100/min, previous window had 80 requests, current window has 30, we're 25% into current window:
```
estimated = 30 + (80 * 0.75) = 30 + 60 = 90 → ALLOWED (< 100)
```

**When it breaks:** Very uneven traffic within a window (e.g., all requests at window start/end).

---

### Q14. Sliding Window Counter - Implementation [Advanced]
**Implement with O(1) memory per client.**

```python
import time

class SlidingWindowCounter:
    def __init__(self, limit: int, window_seconds: int):
        self.limit = limit
        self.window = window_seconds
        self.prev_count = 0
        self.curr_count = 0
        self.curr_window_start = time.monotonic()

    def allow_request(self) -> bool:
        now = time.monotonic()
        elapsed = now - self.curr_window_start

        if elapsed >= self.window:
            self.prev_count = self.curr_count
            self.curr_count = 0
            self.curr_window_start = now
            elapsed = 0

        overlap = 1 - (elapsed / self.window)
        estimated = self.curr_count + (self.prev_count * overlap)

        if estimated < self.limit:
            self.curr_count += 1
            return True
        return False
```

---

## Section F: Distributed Rate Limiting (Q15-Q18)

### Q15. Design Distributed Rate Limiter [Advanced - System Design]
**1M req/sec, 100+ API nodes. Full design.**

**Components:**
1. **Where:** API Gateway layer (before hitting application servers)
2. **Store:** Redis cluster, sharded by client_id
3. **Algorithm:** Sliding Window Counter (best memory/accuracy trade-off)
4. **SPOF mitigation:** Redis Sentinel/Cluster with replication
5. **Network partition:** Fail-open with local rate limiting (degraded accuracy)
6. **Rule storage:** Config service with push-based updates to all nodes

---

### Q16. Race Condition in Distributed Counter [Advanced]
**Two nodes read "5 tokens" simultaneously, both allow, both write "4". Only 1 token deducted instead of 2. Fix it.**

**Options:**
1. **Redis Lua script** (atomic read-check-decrement) -- best performance, single-threaded Redis
2. **WATCH/MULTI/EXEC** (optimistic locking) -- retries on conflict
3. **Redlock** (distributed lock) -- overkill for this, adds latency

**Best choice:** Lua script -- guaranteed atomic, no round-trips.

---

### Q17. Global Rate Limiting Across Data Centers [Advanced]
**5 data centers worldwide. Strong consistency vs eventual consistency?**

**Option A: Strong consistency**
- Central coordinator, all DCs check before allowing
- Accurate but adds ~100-300ms cross-DC latency

**Option B: Eventual consistency with local borrowing**
- Each DC gets token allocation (e.g., 1000/5 = 200 per DC)
- DC tracks locally, requests more from coordinator when running low
- Fast but allows ~5-20% over-admission

**Google/Amazon preference:** Option B -- slightly over-admitting is better than adding latency to every request.

---

### Q18. Redis Goes Down - Fallback Strategy [Advanced]
**Redis is unreachable for 30 seconds. What do you do?**

| Strategy | Risk |
|----------|------|
| Fail-open (allow all) | Abuse, overload downstream |
| Fail-closed (block all) | Full outage for legitimate users |
| Local in-memory rate limiting | Inaccurate (per-instance, not global) |
| Circuit breaker | Switch to local limiter, periodically retry Redis |

**Best practice:** Circuit breaker + local in-memory limiting with relaxed limits. Most companies (Amazon, Google) prefer slight over-admission over full outage.

---

## Section G: API Design & Multi-tenant (Q19-Q21)

### Q19. Multi-tier Rate Limiting [Advanced]
**Design per-user, per-API-key, per-IP, and global limits. How do layers interact?**

Check order: Global → Per-IP → Per-API-key → Per-user
- If ANY layer denies → reject with `429` + tell client WHICH limit was hit
- Global limit protects infrastructure
- Per-IP catches DDoS
- Per-API-key enforces plan limits
- Per-user prevents abuse within a team

---

### Q20. Multi-tenant SaaS Rate Limiting [Advanced]
**Enterprise (10K/min), Startup (500/min), Free (50/min). Free tier bot shouldn't affect Enterprise.**

- **Per-tenant isolation:** Separate counters per tenant
- **Priority queuing:** Enterprise requests processed first under load
- **Noisy neighbor prevention:** Free tier gets hard cap + IP-level limiting
- **Graceful degradation:** Under extreme load, shed free tier first

---

### Q21. Per-endpoint Rate Limiting [Advanced]
**POST /payments = 10/min, GET /products = 1000/min. Design the config + middleware.**

```python
RATE_LIMITS = {
    ("POST", "/payments"): {"limit": 10, "window": 60},
    ("GET", "/products"): {"limit": 1000, "window": 60},
    ("*", "*"): {"limit": 100, "window": 60},  # default
}

def rate_limit_middleware(request):
    key = (request.method, request.path)
    config = RATE_LIMITS.get(key, RATE_LIMITS[("*", "*")])

    client_key = f"{request.user_id}:{key}"
    if not limiter.allow(client_key, config["limit"], config["window"]):
        return Response(status=429, headers={
            "Retry-After": str(config["window"]),
            "X-RateLimit-Limit": str(config["limit"]),
        })
    return handle_request(request)
```

---

## Section H: System Design Aspects (Q22-Q23)

### Q22. Full System Design: API Rate Limiter [Advanced]
**Design from scratch. 100M DAU, 1M req/sec peak.**

Cover:
1. **Placement:** API gateway (before app servers)
2. **Algorithm:** Sliding Window Counter
3. **Data store:** Redis Cluster (sharded by client_id hash)
4. **Rule engine:** Config service (rules stored in DB, cached locally)
5. **Monitoring:** Track 429 rates, alert on spikes
6. **Rule propagation:** Push via pub/sub when rules change
7. **Scaling:** Horizontal scaling of gateway nodes, Redis cluster auto-sharding

---

### Q23. Gateway vs Sidecar vs Middleware [Advanced]
**Compare placement options. When would you choose each?**

| Placement | Latency | Accuracy | Ops Complexity |
|-----------|---------|----------|---------------|
| API Gateway (Kong, Nginx) | Lowest (before app) | Global counters | Low |
| Sidecar (Envoy) | Low | Per-pod, needs sync | Medium (service mesh) |
| App Middleware | Higher (inside app) | App-level context available | Low |

- **Gateway:** Default choice for most APIs
- **Sidecar:** Microservices with service mesh (Istio)
- **Middleware:** When you need app-level context (e.g., user tier, subscription plan)

---

## Section I: Edge Cases & Race Conditions (Q24-Q27)

### Q24. Distributed Abuse Detection [Advanced]
**Attacker rotates 10K API keys, each under the per-key limit. Total traffic overwhelms you.**

- Per-key limits are insufficient alone
- Add **global rate limit** (total requests from all keys)
- **Anomaly detection:** flag clients with unusual patterns (many keys from same IP)
- **IP fingerprinting:** rate limit by IP in addition to API key
- **CAPTCHA challenges:** for suspicious patterns

---

### Q25. Clock Skew & Time Issues [Advanced]
**What happens during NTP clock corrections, DST transitions, or clock skew across servers?**

- **Problem:** `time.time()` can jump backward during NTP sync
- **Fix:** Use `time.monotonic()` for elapsed-time calculations
- **Distributed:** Use logical timestamps or Redis server time (`TIME` command)
- **DST:** Irrelevant if using UTC everywhere (which you should)

---

### Q26. Concurrent Rate Limiter [Advanced]
**Implement thread-safe rate limiter. Show naive version with race condition, then fix it.**

```python
# NAIVE (race condition):
class BrokenLimiter:
    def __init__(self, limit):
        self.counts = {}  # client_id -> count
        self.limit = limit

    def allow(self, client_id):
        count = self.counts.get(client_id, 0)  # Thread A reads 99
        # Thread B also reads 99 here (race!)
        if count < self.limit:
            self.counts[client_id] = count + 1  # Both write 100
            return True
        return False

# FIXED (atomic with lock):
class SafeLimiter:
    def __init__(self, limit):
        self.counts = {}
        self.limit = limit
        self.lock = threading.Lock()

    def allow(self, client_id):
        with self.lock:
            count = self.counts.get(client_id, 0)
            if count < self.limit:
                self.counts[client_id] = count + 1
                return True
            return False

# BETTER (per-client locks for less contention):
# Use ConcurrentHashMap equivalent or per-key locks
```

---

### Q27. WebSocket Rate Limiting [Advanced]
**HTTP: each request is independent. WebSocket: persistent connection, continuous messages. How does this change your design?**

- Can't use HTTP middleware (no per-request interceptor)
- Rate limit at **message level** within the connection handler
- Also limit **payload size** (not just frequency)
- Track per-connection AND per-user (user may have multiple connections)
- Use Token Bucket per connection: allows small bursts of messages, then throttles

```python
class WebSocketRateLimiter:
    def __init__(self, messages_per_second: int, max_payload_kb: int):
        self.msg_limiter = TokenBucket(messages_per_second, messages_per_second)
        self.max_payload = max_payload_kb * 1024

    def allow_message(self, payload: bytes) -> bool:
        if len(payload) > self.max_payload:
            return False
        return self.msg_limiter.allow_request()
```
