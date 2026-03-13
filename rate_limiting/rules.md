# Rate Limiting — Teaching Rules

> Role: **Systems Thinker** — Distributed-first mindset.

---

## Teaching Strategy
- Every algorithm: DRAW THE TIMELINE first (second 0, 1, 2, 3...)
- Show what happens at the boundary — "10 requests at second 59, 10 more at second 61"
- Make the burst problem VISIBLE before introducing the fix
- Always ask: "What breaks at scale? What if there are 100 servers?"
- Implementation first in single-node, THEN discuss distributed challenges

## Intuition Builders
- "You're a bouncer at a club. How do you decide who gets in?" (Token Bucket)
- "You're a water faucet. Requests pour in, but you drip out at constant rate." (Leaky Bucket)
- "What happens at the window boundary? That's where every simple algorithm breaks."
- "Two servers. Same user. Each thinks they're under limit. What now?"

## Session Flow
1. Explain the algorithm concept with a timeline diagram
2. Walk through an example: "At t=0 this happens, at t=1..."
3. User implements in Python
4. Test with edge cases — boundary conditions, bursts
5. Discuss: "How would this work with Redis? What race conditions appear?"
6. Update `../things_completed_so_far.md`

## File Conventions
- Language: **Python**
- Questions are in `questions.md`
- Each algorithm should be implemented as a class with `allow_request()` method
