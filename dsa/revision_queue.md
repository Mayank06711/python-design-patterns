# DSA Revision Queue

> Problems scored ≤ 6/10 come here. Revisit after 3-5 days. Must score ≥ 8/10 to clear.

---

| # | Problem | LC# | Original Score | Original Date | Due Date | Revision Score | Status |
|---|---------|-----|---------------|---------------|----------|---------------|--------|
| 1 | 3Sum | 15 | 5/10 | Mar 18, 2026 | Mar 22, 2026 | **10/10** | ✅ Cleared |
| 2 | Product of Array Except Self | 238 | 5/10 | Mar 22, 2026 | Mar 25, 2026 | **10/10** | ✅ Cleared |
| 3 | Sliding Window Maximum (OPTIMAL) | 239 | 7/10 (brute only) | Mar 26, 2026 | S17 (Apr 11) | **7/10** | ✅ Cleared (all 12/12 with own MyDeque) |
| 4 | Maximum Product Subarray | 152 | 5/10 | Mar 28, 2026 | Mar 31, 2026 | **10/10** | ✅ Cleared |
| 5 | Trapping Rain Water (O(1) space) | 42 | 6/10 | Apr 1, 2026 | Apr 4, 2026 | **8/10** | ✅ Cleared |
| 6 | Search in Rotated Sorted Array | 33 | 4/10 | Apr 3, 2026 | Apr 7, 2026 | **8/10** | ✅ Cleared (Apr 11, fresh file, 7 min under budget) |

### Revision Notes
- **#3 Sliding Window Max**: Brute force O(n*k) solved (7/10). Optimal O(n) requires **monotonic deque** — user knows deque exists but not comfortable using it. Identified max heap O(n log k) as intermediate approach (lazy deletion for out-of-window elements). **Priority: HIGH** — revisit once deque data structure is covered in DSA plan. Key insight user already has: "if outgoing element isn't the max, just compare incoming with previous max."
- **#4 Max Product Subarray**: Struggled with: (1) negatives flip min↔max, (2) need 3 candidates (start fresh, extend best, extend worst), (3) global maxi must never decrease, (4) simultaneous update of prev_max/prev_min. Key pattern: at each position, new_max = max(nums[i], prev_max*nums[i], prev_min*nums[i]).
- **#6 Search in Rotated Sorted Array**: Core issues: (1) initially proposed wrong "two pass" approach instead of single-pass, (2) didn't understand WHY one half is always sorted (only 1 pivot → only 1 half has the break), (3) boundary bugs: strict `<`/`>` instead of `<=`/`>=` missed elements AT boundaries, (4) missing `else` in right-sorted branch caused infinite loop, (5) `while(left < right)` instead of `<=` skipped single-element case. **Must internalize:** rotated array has exactly 1 break point; `nums[left] <= nums[mid]` → left sorted; check if target in sorted range, if not → go other side.
