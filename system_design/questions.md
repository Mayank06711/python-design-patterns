# System Design Interview Questions (27 Questions - Mid to Advanced)

> Curated from Google, Amazon, Meta, Netflix, Uber interviews
> Focus: How to structure answers + key concepts per problem

---

## How to Answer Any System Design Question (Framework)

**Step 1: Requirements (3-5 min)**
- Functional: What does the system do?
- Non-functional: Scale, latency, availability, consistency
- Ask clarifying questions!

**Step 2: High-Level Design (10-15 min)**
- Draw core components, data flow, APIs
- Identify the database, cache, queue

**Step 3: Deep Dive (15-20 min)**
- Go deep on 2-3 critical components
- Discuss trade-offs, not just solutions

**Step 4: Wrap-up (5 min)**
- Bottlenecks, monitoring, failure scenarios

---

## Section A: Classic Problems (Q1-Q6)

### Q1. Design a URL Shortener (TinyURL/Bitly) [Mid]
**Key decisions:**
- **Encoding:** Base-62 of auto-increment ID vs MD5/SHA hash truncation
- **Database:** NoSQL (DynamoDB) for key-value lookups at scale
- **Read:Write ratio:** ~100:1 (read-heavy → cache aggressively)
- **Cache:** Redis/Memcached for hot URLs
- **Analytics:** Async event logging to Kafka → analytics pipeline
- **Scale:** 100M URLs/month, 10B redirects/month

**API:**
```
POST /shorten  { long_url } → { short_url }
GET  /:code    → 301 Redirect to long_url
```

---

### Q2. Design a Chat System (WhatsApp/Slack) [Advanced]
**Key decisions:**
- **Protocol:** WebSocket for real-time bidirectional communication
- **1:1 chat:** Sender → Chat Server → Message Queue → Receiver's Chat Server → Receiver
- **Group chat:** Fan-out to all group members (small groups: push to each; large groups: pull model)
- **Message storage:** Per-user message queue (Cassandra/HBase) + message ID for ordering
- **Presence:** Heartbeat-based online/offline status (publish to friends via pub/sub)
- **Delivery receipts:** sent/delivered/read status via ack messages
- **Scale:** 1B users, 100B messages/day

---

### Q3. Design a News Feed (Facebook/Twitter) [Advanced]
**The classic fan-out question:**

| Approach | Pros | Cons |
|----------|------|------|
| Fan-out on Write | Feed pre-computed, fast reads | Slow writes for users with millions of followers |
| Fan-out on Read | Fast writes | Slow reads, compute feed on every request |
| Hybrid (best) | Fast reads + manageable writes | More complex |

**Hybrid approach:**
- Regular users: fan-out on write (pre-compute followers' feeds)
- Celebrity users (>10K followers): fan-out on read (compute on request, cache)
- Feed stored in Redis sorted sets (score = timestamp)

---

### Q4. Design a Video Streaming Platform (YouTube/Netflix) [Advanced]
**Key components:**
1. **Upload pipeline:** Video → Transcoding service (multiple resolutions/formats) → Object storage (S3)
2. **CDN:** Serve videos from edge locations closest to users
3. **Adaptive bitrate:** Client switches quality based on bandwidth (HLS/DASH)
4. **Metadata:** SQL database for video info, NoSQL for comments
5. **Recommendation:** ML pipeline (offline batch processing)
6. **Scale:** 1B daily video views, 500 hours uploaded/min

---

### Q5. Design a Ride-Sharing Service (Uber/Lyft) [Advanced]
**Key components:**
1. **Location service:** Drivers send GPS every 3-5 sec → geospatial index (geohash/quadtree)
2. **Matching:** When rider requests → find nearby drivers in geohash cells → rank by ETA
3. **ETA calculation:** Graph algorithms (Dijkstra/A*) on road network
4. **Surge pricing:** Real-time supply/demand ratio per zone
5. **Trip tracking:** WebSocket connection for real-time updates
6. **Database:** PostgreSQL (trips, users) + Redis (driver locations) + Kafka (events)

---

### Q6. Design Cloud File Storage (Dropbox/Google Drive) [Advanced]
**Key decisions:**
- **Chunked upload:** Split large files into 4MB chunks → upload in parallel
- **Deduplication:** Hash each chunk → store only unique chunks
- **Sync:** Client tracks local file changes → sends delta to server → server notifies other clients
- **Conflict resolution:** Last-write-wins or branching (like git)
- **Metadata:** SQL database (file tree, permissions, versions)
- **Block storage:** S3 for actual file chunks

---

## Section B: Scalability & Infrastructure (Q7-Q10)

### Q7. Design a Rate Limiter [Mid-Advanced]
*See [rate_limiting/questions.md](../rate_limiting/questions.md) for full deep dive (27 questions).*

Quick recap: Token Bucket for API gateway, Redis for distributed state, Sliding Window Counter for accuracy/memory balance.

---

### Q8. Design a CDN [Advanced]
**Key concepts:**
- **Edge servers:** Cache content geographically close to users
- **Cache hierarchy:** Edge → Regional → Origin
- **Invalidation:** TTL-based, purge API, versioned URLs
- **Routing:** DNS-based (GeoDNS) or Anycast
- **Pull vs Push:** Pull (cache on first request) vs Push (pre-populate edges)
- **Cache key:** URL + headers (Accept-Encoding, etc.)

---

### Q9. Design a Distributed Cache (Redis) [Advanced]
**Key decisions:**
- **Partitioning:** Consistent hashing (add/remove nodes without full rehash)
- **Eviction:** LRU (most common), LFU, TTL-based
- **Patterns:**
  - Cache-aside: App checks cache → miss → read DB → write cache
  - Write-through: App writes cache → cache writes DB
  - Write-behind: App writes cache → cache async writes DB (risk: data loss)
- **Cache stampede:** When cache expires, 1000 requests hit DB simultaneously
  - Fix: Locking (only 1 request rebuilds cache), probabilistic early expiry

---

### Q10. Design a Load Balancer [Mid]
**Layers:**
- **L4 (Transport):** Routes by IP/port, fast, no content inspection
- **L7 (Application):** Routes by URL/headers/cookies, content-aware

**Algorithms:**
- Round-robin (simple, equal distribution)
- Weighted round-robin (more traffic to stronger servers)
- Least connections (route to least busy server)
- Consistent hashing (for sticky sessions / caching)

**Health checks:** Periodic HTTP/TCP probes, remove unhealthy nodes

---

## Section C: Database Design (Q11-Q13)

### Q11. Design a Key-Value Store (DynamoDB) [Advanced]
**Key concepts:**
- **Partitioning:** Consistent hashing across nodes
- **Replication:** N replicas per key (configurable read/write quorum)
- **Conflict resolution:** Vector clocks + last-write-wins
- **Consistency:** Tunable (R + W > N for strong consistency)
- **Failure detection:** Gossip protocol
- **Read repair + anti-entropy:** Catch stale replicas

---

### Q12. Design Search Autocomplete [Advanced]
**Key decisions:**
- **Data structure:** Trie (prefix tree) for fast prefix matching
- **Ranking:** Store frequency/score at each node → return top-K
- **Scale:** Trie too large for one machine → shard by first 2 characters
- **Update:** Offline batch job updates trie periodically (not real-time)
- **Latency target:** < 100ms (users expect instant results)
- **Personalization:** Blend global popular + user's search history

---

### Q13. Design a Web Crawler [Advanced]
**Key components:**
1. **Seed URLs** → URL Frontier (priority queue)
2. **Fetcher:** Download pages (respect robots.txt, rate limit per domain)
3. **Parser:** Extract content + new URLs
4. **Deduplication:** URL bloom filter + content fingerprint (SimHash)
5. **Storage:** Raw HTML in object storage, parsed content in search index
6. **Politeness:** Don't overwhelm any single domain
7. **Scale:** Crawl billions of pages, BFS traversal

---

## Section D: Microservices & Distributed Systems (Q14-Q16)

### Q14. Design a Notification System [Advanced]
**Components:**
1. **API:** Receives notification requests
2. **Validation + Rate Limiting:** Don't spam users
3. **User Preferences:** Check opt-in/out per channel
4. **Channel Workers:** Email worker, SMS worker, Push worker (separate queues)
5. **Message Queue:** Kafka/SQS for decoupling + retry
6. **Dead Letter Queue:** For failed deliveries after N retries
7. **Analytics:** Track delivery, open, click rates

---

### Q15. Design a Distributed Task Scheduler [Advanced]
**Like cron at scale.**

- **Job storage:** Database (job definition, schedule, last_run, next_run)
- **Scheduler:** Polls for due jobs, pushes to message queue
- **Workers:** Pull from queue, execute, report status
- **Idempotency:** Jobs must be safe to retry (use idempotency keys)
- **Exactly-once:** Hard! Use at-least-once + idempotent jobs
- **Priority:** Multiple queues (high/medium/low priority)
- **Failure handling:** Retry with exponential backoff → dead letter queue

---

### Q16. Design E-Commerce Microservices [Advanced]
**Service decomposition:**
- Product Catalog Service
- Shopping Cart Service
- Order Service
- Payment Service
- Inventory Service
- Notification Service

**Key patterns:**
- **API Gateway:** Single entry point, routes to services
- **Saga Pattern:** Distributed transaction (Order → Payment → Inventory → Notify)
  - If Payment fails → compensating action (cancel order)
- **Circuit Breaker:** If Payment service is down, fail fast
- **Event-driven:** Order publishes "OrderCreated" → other services react

---

## Section E: Message Queues & Events (Q17-Q18)

### Q17. Design a Message Queue (Kafka) [Advanced]
**Key concepts:**
- **Topics + Partitions:** Messages sharded across partitions for parallelism
- **Consumer Groups:** Each partition consumed by exactly one consumer in a group
- **Ordering:** Guaranteed WITHIN a partition, not across partitions
- **Delivery semantics:**
  - At-most-once: Don't retry (may lose messages)
  - At-least-once: Retry on failure (may duplicate)
  - Exactly-once: Idempotent producers + transactional consumers
- **Retention:** Time-based or size-based (Kafka keeps messages on disk)

---

### Q18. Design Real-Time Analytics Dashboard [Advanced]
**Pipeline:**
1. **Ingestion:** Events from apps → Kafka topics
2. **Stream processing:** Flink/Spark Streaming → windowed aggregations
3. **Storage:** Time-series DB (InfluxDB) or pre-aggregated in Redis
4. **Serving:** API serves dashboard queries from pre-computed results
5. **Approximate counting:** HyperLogLog for unique visitors (saves memory)
6. **Windowing:** Tumbling (fixed), Sliding, Session windows

---

## Section F: CAP Theorem & Consistency (Q19-Q20)

### Q19. CAP Theorem in Practice [Advanced]
**You can't have all three: Consistency, Availability, Partition Tolerance.**

Since network partitions WILL happen, you choose between:
- **CP (Consistency + Partition Tolerance):** Reject requests during partition. Examples: ZooKeeper, HBase, MongoDB (default)
- **AP (Availability + Partition Tolerance):** Serve potentially stale data. Examples: Cassandra, DynamoDB, CouchDB

**Real-world:** Most systems are a spectrum, not strictly CP or AP. DynamoDB lets you choose per-query (strong vs eventual reads).

---

### Q20. Design a Unique ID Generator (Snowflake) [Advanced]
**Requirements:** Globally unique, roughly time-ordered, 64-bit, no coordination.

**Snowflake structure (64 bits):**
```
| 1 bit unused | 41 bits timestamp | 10 bits machine ID | 12 bits sequence |
```

- **41 bits timestamp:** ~69 years from epoch
- **10 bits machine ID:** 1024 machines
- **12 bits sequence:** 4096 IDs per millisecond per machine
- **Total:** ~4M IDs/sec/machine with no coordination
- **Clock drift:** If clock goes backward, wait or reject until caught up

---

## Section G: API Design (Q21-Q22)

### Q21. REST API Design Best Practices [Mid]
**Key principles:**
- **Resources as nouns:** `/users`, `/orders` (not `/getUsers`, `/createOrder`)
- **HTTP verbs:** GET (read), POST (create), PUT (replace), PATCH (partial update), DELETE
- **Pagination:** Cursor-based (not offset) for large datasets
- **Versioning:** URL-based (`/v1/users`) or header-based (`Accept: v1`)
- **Idempotency:** POST with idempotency key, PUT is naturally idempotent
- **Error format:** Consistent JSON with error code + message

**REST vs GraphQL vs gRPC:**
| | REST | GraphQL | gRPC |
|--|------|---------|------|
| Best for | Public APIs | Complex frontend queries | Internal microservices |
| Over-fetching | Common | Solved | N/A |
| Performance | Good | Good | Best (binary protocol) |

---

### Q22. Design an API Gateway [Advanced]
**Responsibilities:**
1. Authentication / Authorization
2. Rate limiting
3. Request routing
4. Load balancing
5. Response caching
6. Request/response transformation
7. Circuit breaking
8. Logging / monitoring

---

## Section H: Real-World Scenarios (Q23-Q27)

### Q23. Design Google Maps [Advanced]
**Key components:**
- **Map rendering:** Pre-rendered tiles at multiple zoom levels
- **Routing:** Dijkstra/A* on road graph (billions of edges)
  - Optimization: Contraction Hierarchies for fast shortest-path
- **Real-time traffic:** Aggregate GPS data from phones → update edge weights
- **Geospatial index:** S2 cells or geohash for nearby searches
- **ETAs:** ML model (road type, time-of-day, weather, events)

---

### Q24. Design a Payment System (Stripe) [Advanced]
**Critical requirements:** Exactly-once processing, auditability, security.

**Key concepts:**
- **Idempotency key:** Client sends unique key → server deduplicates
- **Two-phase commit:** Reserve funds → confirm after fulfillment
- **Saga pattern:** Order → Payment → Inventory (with compensating rollback)
- **Audit trail:** Append-only event log of all transactions
- **PCI compliance:** Tokenize card data, never store raw card numbers
- **Retry:** Exponential backoff with jitter for failed payment API calls

---

### Q25. Design a Ticket Booking System (Ticketmaster) [Advanced]
**The concurrency challenge:**
- **Problem:** 10M users trying to buy 50K tickets simultaneously
- **Optimistic locking:** `UPDATE seats SET status='booked' WHERE id=X AND status='available'`
  - If 0 rows affected → someone else booked it
- **Queue-based:** Put users in virtual queue, process sequentially
- **Temporary hold:** Lock seat for 10 min while user completes payment
- **Flash sale pattern:** Pre-generate inventory tokens, distribute via queue

---

### Q26. Design a Collaborative Editor (Google Docs) [Advanced]
**The hardest problem: concurrent edits.**

**Approaches:**
- **Operational Transformation (OT):** Transform operations based on concurrent edits
  - Used by Google Docs
  - Complex to implement correctly (especially with >2 users)
- **CRDTs (Conflict-free Replicated Data Types):** Data structures that mathematically guarantee convergence
  - Used by Figma, Apple Notes
  - Simpler to reason about, but larger data size

**Architecture:** Client → WebSocket → Server → broadcast to other clients

---

### Q27. Design a Stock Trading Platform [Advanced]
**Key requirements:** Ultra-low latency, strict ordering, audit trail.

- **Order matching engine:** Price-time priority matching (limit order book)
- **Event sourcing:** All state changes stored as immutable events
- **CQRS:** Separate write (order placement) from read (portfolio view)
- **Latency:** <1ms for matching (in-memory, single-threaded)
- **Consistency:** Strong consistency for order book, eventual for portfolio views
- **Risk management:** Pre-trade risk checks (margin, position limits)

---

## Key Concepts Cheat Sheet

| Concept | One-Line Summary |
|---------|-----------------|
| Horizontal scaling | Add more machines (preferred for distributed systems) |
| Vertical scaling | Bigger machine (simpler but has limits) |
| Load balancing | Distribute traffic across servers (L4/L7) |
| Caching | Store hot data close to consumer (Redis/Memcached) |
| Sharding | Split database by key (hash or range-based) |
| Replication | Copy data to multiple nodes (leader-follower, leaderless) |
| CAP theorem | Pick 2 of 3: Consistency, Availability, Partition Tolerance |
| Consistent hashing | Distribute data across nodes with minimal reshuffling |
| Message queue | Decouple producers and consumers (Kafka/SQS/RabbitMQ) |
| Circuit breaker | Stop calling failing service, fail fast, recover |
| Saga pattern | Distributed transaction via compensating actions |
| CQRS | Separate read and write models |
| Event sourcing | Store events, not state (append-only log) |
| CDN | Serve static content from edge locations near users |
| Bloom filter | Space-efficient "probably yes / definitely no" membership test |
| HyperLogLog | Approximate count of unique elements (tiny memory) |
