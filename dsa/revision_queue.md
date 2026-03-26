# DSA Revision Queue

> Problems scored ≤ 6/10 come here. Revisit after 3-5 days. Must score ≥ 8/10 to clear.

---

| # | Problem | LC# | Original Score | Original Date | Due Date | Revision Score | Status |
|---|---------|-----|---------------|---------------|----------|---------------|--------|
| 1 | 3Sum | 15 | 5/10 | Mar 18, 2026 | Mar 22, 2026 | **10/10** | ✅ Cleared |
| 2 | Product of Array Except Self | 238 | 5/10 | Mar 22, 2026 | Mar 25, 2026 | **10/10** | ✅ Cleared |
| 3 | Sliding Window Maximum (OPTIMAL) | 239 | 7/10 (brute only) | Mar 26, 2026 | After Deque learned | — | ⏳ Blocked — need monotonic deque |

### Revision Notes
- **#3 Sliding Window Max**: Brute force O(n*k) solved (7/10). Optimal O(n) requires **monotonic deque** — user knows deque exists but not comfortable using it. Identified max heap O(n log k) as intermediate approach (lazy deletion for out-of-window elements). **Priority: HIGH** — revisit once deque data structure is covered in DSA plan. Key insight user already has: "if outgoing element isn't the max, just compare incoming with previous max."
