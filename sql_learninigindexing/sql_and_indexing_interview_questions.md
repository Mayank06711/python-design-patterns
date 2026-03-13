# SQL & Database Indexing Interview Questions
## Top Tech Companies (Google, Amazon, Meta, Stripe, Uber, Apple)
### Mid to Advanced Level -- 30 Questions

---

## SECTION A: Complex SQL Queries (JOINs, Subqueries, CTEs, Window Functions)

---

### Q1. Find the Nth Highest Salary Per Department (Amazon, Google)

Given an `employees` table:

```
employees(employee_id, name, department_id, salary)
```

**Problem:** Write a query to find the **3rd highest distinct salary** in each department. If a department has fewer than 3 distinct salaries, return NULL for that department.

```sql
-- Approach: DENSE_RANK inside a CTE
WITH ranked AS (
    SELECT
        department_id,
        name,
        salary,
        DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT department_id, name, salary
FROM ranked
WHERE rnk = 3;
```

**Follow-up:** Why use `DENSE_RANK()` instead of `RANK()` or `ROW_NUMBER()` here? What changes if there are ties?

---

### Q2. Detect Gaps in a Sequence (Google)

Given a `bookings` table:

```
bookings(booking_id INT AUTO_INCREMENT, customer_id, booking_date)
```

**Problem:** Find all missing `booking_id` values (gaps) in the sequence. For example, if IDs are 1, 2, 4, 7, the gaps are 3, 5, 6.

```sql
-- Using a recursive CTE to generate the full sequence then LEFT JOIN
WITH RECURSIVE seq AS (
    SELECT MIN(booking_id) AS id FROM bookings
    UNION ALL
    SELECT id + 1 FROM seq WHERE id < (SELECT MAX(booking_id) FROM bookings)
)
SELECT s.id AS missing_booking_id
FROM seq s
LEFT JOIN bookings b ON s.id = b.booking_id
WHERE b.booking_id IS NULL;
```

**Follow-up:** How would you solve this without a recursive CTE? (Hint: Use `LEAD()`)

```sql
-- Alternative with LEAD()
SELECT booking_id + 1 AS gap_start,
       LEAD(booking_id) OVER (ORDER BY booking_id) - 1 AS gap_end
FROM bookings
WHERE LEAD(booking_id) OVER (ORDER BY booking_id) - booking_id > 1;
```

---

### Q3. Running Total and Moving Average (Amazon, Stripe)

Given a `daily_sales` table:

```
daily_sales(sale_date DATE, revenue DECIMAL)
```

**Problem:** Write a query that returns each date along with:
- A cumulative running total of revenue
- A 7-day trailing moving average of revenue

```sql
SELECT
    sale_date,
    revenue,
    SUM(revenue) OVER (ORDER BY sale_date
                       ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS running_total,
    AVG(revenue) OVER (ORDER BY sale_date
                       ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS moving_avg_7d
FROM daily_sales
ORDER BY sale_date;
```

**Follow-up:** What is the difference between `ROWS BETWEEN` and `RANGE BETWEEN`? When does it matter?

---

### Q4. Customers Who Bought Product A and B but NOT C (Amazon)

Given:

```
customers(customer_id, name)
orders(order_id, customer_id, product_name)
```

**Problem:** Find all customers who purchased both 'Product A' AND 'Product B', but have never purchased 'Product C'.

```sql
SELECT c.customer_id, c.name
FROM customers c
WHERE c.customer_id IN (SELECT customer_id FROM orders WHERE product_name = 'Product A')
  AND c.customer_id IN (SELECT customer_id FROM orders WHERE product_name = 'Product B')
  AND c.customer_id NOT IN (SELECT customer_id FROM orders WHERE product_name = 'Product C');
```

**Follow-up:** Rewrite this using JOINs only (no subqueries). Then rewrite using `GROUP BY` / `HAVING` with conditional aggregation.

```sql
-- GROUP BY / HAVING approach
SELECT c.customer_id, c.name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(CASE WHEN o.product_name = 'Product A' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN o.product_name = 'Product B' THEN 1 ELSE 0 END) > 0
   AND SUM(CASE WHEN o.product_name = 'Product C' THEN 1 ELSE 0 END) = 0;
```

---

### Q5. Identify Consecutive Login Streaks (Google, Meta)

Given:

```
user_logins(user_id, login_date DATE)  -- one row per user per day they logged in
```

**Problem:** For each user, find the longest streak of consecutive daily logins.

```sql
WITH grouped AS (
    SELECT
        user_id,
        login_date,
        login_date - INTERVAL (ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date)) DAY AS grp
    FROM user_logins
)
SELECT user_id, MAX(streak) AS longest_streak
FROM (
    SELECT user_id, grp, COUNT(*) AS streak
    FROM grouped
    GROUP BY user_id, grp
) streaks
GROUP BY user_id
ORDER BY longest_streak DESC;
```

**Follow-up:** How would you find users who had a streak of 7+ days in the last 30 days?

---

### Q6. Repeated Payments Detection (Stripe)

Given:

```
transactions(transaction_id, merchant_id, credit_card_id, amount, transaction_timestamp)
```

**Problem:** Identify transactions where the same credit card made a payment to the same merchant for the same amount within 10 minutes of a previous payment. Flag these as potential duplicates.

```sql
WITH flagged AS (
    SELECT
        *,
        LAG(transaction_timestamp) OVER (
            PARTITION BY merchant_id, credit_card_id, amount
            ORDER BY transaction_timestamp
        ) AS prev_txn_time
    FROM transactions
)
SELECT *
FROM flagged
WHERE TIMESTAMPDIFF(MINUTE, prev_txn_time, transaction_timestamp) <= 10;
```

---

### Q7. Year-over-Year Revenue Growth Per Product (Google, Amazon)

Given:

```
orders(order_id, product_id, order_date, revenue)
```

**Problem:** Calculate the year-over-year percentage revenue growth for each product. Show product_id, year, current_year_revenue, previous_year_revenue, and yoy_growth_pct.

```sql
WITH yearly AS (
    SELECT
        product_id,
        EXTRACT(YEAR FROM order_date) AS yr,
        SUM(revenue) AS total_revenue
    FROM orders
    GROUP BY product_id, EXTRACT(YEAR FROM order_date)
)
SELECT
    product_id,
    yr,
    total_revenue AS current_year_revenue,
    LAG(total_revenue) OVER (PARTITION BY product_id ORDER BY yr) AS prev_year_revenue,
    ROUND(
        100.0 * (total_revenue - LAG(total_revenue) OVER (PARTITION BY product_id ORDER BY yr))
        / LAG(total_revenue) OVER (PARTITION BY product_id ORDER BY yr),
        2
    ) AS yoy_growth_pct
FROM yearly
ORDER BY product_id, yr;
```

---

### Q8. Median Calculation Without Built-in MEDIAN() (Google)

Given:

```
search_frequency(searches INT, num_users INT)
-- e.g., (1, 2) means 2 users each made 1 search
```

**Problem:** Find the median number of searches made per user. Round to 1 decimal place. Note: there is no built-in `MEDIAN()` in MySQL/PostgreSQL standard.

```sql
WITH expanded AS (
    SELECT searches
    FROM search_frequency
    CROSS JOIN LATERAL generate_series(1, num_users)  -- PostgreSQL
),
ordered AS (
    SELECT
        searches,
        ROW_NUMBER() OVER (ORDER BY searches) AS rn,
        COUNT(*) OVER () AS total
    FROM expanded
)
SELECT ROUND(AVG(searches), 1) AS median
FROM ordered
WHERE rn IN (FLOOR((total + 1) / 2.0), CEIL((total + 1) / 2.0));
```

---

## SECTION B: Query Optimization & EXPLAIN Plans

---

### Q9. Reading and Interpreting EXPLAIN Output

**Problem:** You are given this query on a table with 10 million rows:

```sql
SELECT * FROM orders WHERE customer_email = 'user@example.com' AND status = 'shipped';
```

Running `EXPLAIN ANALYZE` returns:

```
Seq Scan on orders  (cost=0.00..285432.00 rows=1 width=120)
  Filter: ((customer_email = 'user@example.com') AND (status = 'shipped'))
  Rows Removed by Filter: 9999999
  Planning Time: 0.1 ms
  Execution Time: 2450.3 ms
```

**Questions:**
- (a) What does "Seq Scan" indicate, and why is it a problem here?
- (b) What index(es) would you create to optimize this query?
- (c) After creating a composite index on `(customer_email, status)`, what would you expect the EXPLAIN output to look like?
- (d) Would `(status, customer_email)` be equally effective? Why or why not?

---

### Q10. Why Is My Indexed Column Not Being Used? (Google, Amazon)

**Problem:** You have an index on `orders.created_at`, but this query does a full table scan:

```sql
SELECT * FROM orders WHERE YEAR(created_at) = 2024;
```

- (a) Explain why the index is NOT used (non-sargable predicate).
- (b) Rewrite the query so the index IS used.

```sql
-- Sargable version
SELECT * FROM orders
WHERE created_at >= '2024-01-01' AND created_at < '2025-01-01';
```

- (c) Give 3 other examples of non-sargable predicates that prevent index usage.

```
-- Examples of non-sargable predicates:
--   WHERE LOWER(email) = 'user@example.com'   -- function on column
--   WHERE price + 10 > 100                    -- expression on column
--   WHERE name LIKE '%smith'                  -- leading wildcard
```

---

### Q11. Optimizing a Slow JOIN Query

**Problem:** This query takes 45 seconds on production:

```sql
SELECT c.name, COUNT(o.order_id) AS order_count, SUM(o.amount) AS total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_date >= '2024-01-01'
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 100;
```

**Questions:**
- (a) The `LEFT JOIN` + `WHERE` on the right table effectively becomes an INNER JOIN. Explain why and fix it.
- (b) What indexes would you add?
- (c) The `SELECT *` anti-pattern is avoided, but `GROUP BY c.name` can be problematic. Why?
- (d) Rewrite this query for optimal performance.

```sql
-- Optimized version
SELECT c.name, sub.order_count, sub.total_spent
FROM (
    SELECT customer_id, COUNT(*) AS order_count, SUM(amount) AS total_spent
    FROM orders
    WHERE order_date >= '2024-01-01'
    GROUP BY customer_id
    ORDER BY total_spent DESC
    LIMIT 100
) sub
JOIN customers c ON c.customer_id = sub.customer_id
ORDER BY sub.total_spent DESC;
-- Aggregate first on the smaller set, then JOIN for names
```

---

### Q12. SELECT * vs. SELECT Specific Columns -- Why Does It Matter?

**Problem:** Explain the performance implications of:

```sql
-- Query A
SELECT * FROM users WHERE status = 'active';

-- Query B
SELECT user_id, name FROM users WHERE status = 'active';
```

Assuming there is a covering index on `(status, user_id, name)`:
- Which query can be satisfied entirely from the index (index-only scan)?
- Which query must do a heap/table lookup?
- What is the I/O cost difference on a table with 50 million rows and 10 million active users?

---

## SECTION C: Indexing Strategies (B-Tree, Hash, Composite, Covering)

---

### Q13. B-Tree vs. Hash Index -- When to Use Each

**Problem:** Explain the differences and answer:
- (a) You need to support `WHERE price BETWEEN 10 AND 50`. Which index type and why?
- (b) You need to support `WHERE session_token = 'abc123'` (exact match only, millions of lookups/sec). Which index type and why?
- (c) Why are B-tree indexes the default in most RDBMS?
- (d) Can a hash index support `ORDER BY`? Why or why not?
- (e) What is the time complexity of lookup for each type?

**Key answers:**
- B-tree: O(log n), supports range queries, ORDER BY, LIKE 'prefix%'
- Hash: O(1) average for equality, cannot support ranges, sorting, or partial matches

---

### Q14. Composite Index Column Order Matters

**Problem:** Given these three queries on a `products` table:

```sql
-- Query 1
SELECT * FROM products WHERE category = 'Electronics' AND price > 100;

-- Query 2
SELECT * FROM products WHERE price > 100;

-- Query 3
SELECT * FROM products WHERE category = 'Electronics';
```

You create this composite index:

```sql
CREATE INDEX idx_cat_price ON products(category, price);
```

- (a) Which of the three queries will use this index effectively?
- (b) Why won't Query 2 benefit from this index? (leftmost prefix rule)
- (c) Would an index on `(price, category)` change the answers? How?
- (d) What is the "leftmost prefix rule" for composite indexes?

---

### Q15. Covering Index Design Challenge

**Problem:** Your application's most critical query is:

```sql
SELECT employee_id, first_name, last_name, department
FROM employees
WHERE department = 'Engineering' AND hire_date > '2023-01-01'
ORDER BY hire_date DESC;
```

- (a) Design a covering index that satisfies this query entirely from the index.
- (b) Explain why column order in the index matters for this specific query.
- (c) What are the downsides of making this a covering index (extra columns = larger index)?

```sql
-- Optimal covering index
CREATE INDEX idx_covering ON employees(department, hire_date DESC, employee_id, first_name, last_name);
-- department: equality filter (first)
-- hire_date: range filter + ORDER BY (second)
-- remaining columns: covering (avoid table lookup)
```

---

### Q16. How Does a Clustered Index Differ from a Non-Clustered Index?

**Problem:**
- (a) A table can have only ONE clustered index. Why?
- (b) What happens to non-clustered index lookups when the table has no clustered index (heap table)?
- (c) If a clustered index is on `order_date` and most queries filter by `customer_id`, what is the performance implication?
- (d) In PostgreSQL, there is no true clustered index (only `CLUSTER` command). How does this differ from SQL Server's approach?

---

### Q17. Index Intersection and Its Trade-offs

**Problem:** Instead of a composite index on `(A, B)`, you have two separate indexes:

```sql
CREATE INDEX idx_a ON orders(customer_id);
CREATE INDEX idx_b ON orders(order_date);
```

For the query:

```sql
SELECT * FROM orders WHERE customer_id = 42 AND order_date > '2024-01-01';
```

- (a) Can the database use both indexes simultaneously? (Index Intersection / Bitmap AND)
- (b) When is index intersection effective, and when is a composite index strictly better?
- (c) What does the EXPLAIN plan look like for an index intersection vs. a composite index scan?

---

## SECTION D: When to Use and When NOT to Use Indexes

---

### Q18. Scenarios Where Adding an Index Hurts Performance

**Problem:** For each scenario, explain whether adding an index helps, hurts, or is irrelevant:

- (a) A table with 50 rows used as a lookup/reference table
- (b) A column with only 2 distinct values (e.g., `gender CHAR(1)`) on a table with 100M rows
- (c) A table that receives 10,000 INSERTs per second but is queried only once per hour
- (d) A column that is updated on 80% of all UPDATE operations
- (e) A `TEXT`/`BLOB` column used in `WHERE ... LIKE '%keyword%'`

**Key principles:**
- Small tables: sequential scan is faster than index overhead
- Low cardinality: index scan reads nearly all rows anyway (consider partial/filtered index instead)
- Write-heavy tables: every INSERT/UPDATE/DELETE must also update all indexes
- Frequently updated columns: constant index reorganization
- Full-text search on TEXT: use full-text indexes, not B-tree

---

### Q19. Over-Indexing: Diagnosing and Fixing

**Problem:** A table has 15 indexes but INSERT performance has degraded by 70%.

- (a) How would you identify which indexes are unused? (Query `pg_stat_user_indexes` in PostgreSQL or `sys.dm_db_index_usage_stats` in SQL Server)
- (b) What is the write amplification cost of maintaining 15 indexes?
- (c) How do you decide which indexes to drop without breaking production queries?
- (d) What monitoring would you set up going forward?

---

### Q20. Partial (Filtered) Indexes

**Problem:** You have an `orders` table where 95% of rows have `status = 'completed'` and only 5% have `status = 'pending'`. Queries almost always filter for pending orders.

- (a) Why is a regular index on `status` inefficient?
- (b) Write a partial (filtered) index that only indexes pending orders.

```sql
-- PostgreSQL
CREATE INDEX idx_pending_orders ON orders(order_date)
WHERE status = 'pending';

-- SQL Server
CREATE INDEX idx_pending_orders ON orders(order_date)
WHERE status = 'pending';
-- (SQL Server calls these "filtered indexes")
```

- (c) What are the limitations of partial indexes?

---

## SECTION E: Normalization and Denormalization

---

### Q21. Identify the Normal Form and Normalize

**Problem:** Given this table:

```
student_courses(student_id, student_name, student_email,
                course_id, course_name, instructor_name, instructor_email, grade)
```

- (a) What normal form is this table currently in? Identify all violations.
- (b) Decompose it into 3NF (Third Normal Form). Show all resulting tables with their keys.
- (c) Decompose into BCNF if there are further violations.
- (d) What are the trade-offs of normalizing this table for a read-heavy reporting workload?

---

### Q22. When and Why to Denormalize

**Problem:** You have a fully normalized e-commerce schema (3NF) with these tables:

```
users, orders, order_items, products, categories, shipping_addresses, payments
```

Your analytics dashboard needs to show: "Top 100 customers by total spend in the last 90 days, with their most-purchased category and shipping city."

- (a) Write the normalized query (it will require 5+ JOINs).
- (b) Explain why this query is expensive at scale (100M+ orders).
- (c) Propose a denormalized solution (materialized view or summary table).
- (d) How do you keep the denormalized data consistent? (triggers, scheduled refresh, CDC)
- (e) When is a materialized view preferable to a manually maintained summary table?

---

### Q23. OLTP vs. OLAP Schema Design

**Problem:**
- (a) Explain why OLTP systems favor normalized schemas (3NF).
- (b) Explain why OLAP/data warehouse systems favor star schemas (denormalized).
- (c) Given a star schema with a `fact_sales` table and dimensions `dim_product`, `dim_customer`, `dim_date`, `dim_store`, write a query to find the top 10 stores by revenue in Q4 2024, broken down by product category.
- (d) What indexes would you put on the fact table vs. dimension tables?

---

## SECTION F: Real-World Query Problems

---

### Q24. Find Employees Earning More Than Their Manager (Amazon, Google)

Given:

```
employees(employee_id, name, salary, manager_id)
-- manager_id references employee_id (self-referencing)
```

**Problem:** Write a query to return all employees who earn more than their direct manager.

```sql
SELECT e.name AS employee, e.salary AS emp_salary,
       m.name AS manager, m.salary AS mgr_salary
FROM employees e
JOIN employees m ON e.manager_id = m.employee_id
WHERE e.salary > m.salary;
```

**Follow-up:** Extend this to find employees who earn more than their manager's manager (skip-level).

---

### Q25. Pivot Table: Rows to Columns (Amazon, Meta)

Given:

```
exam_scores(student_id, subject, score)
-- subjects: 'Math', 'Science', 'English'
```

**Problem:** Pivot this into a single row per student with columns for each subject.

```sql
SELECT
    student_id,
    MAX(CASE WHEN subject = 'Math' THEN score END) AS math_score,
    MAX(CASE WHEN subject = 'Science' THEN score END) AS science_score,
    MAX(CASE WHEN subject = 'English' THEN score END) AS english_score
FROM exam_scores
GROUP BY student_id;
```

**Follow-up:** How would you do this dynamically if the number of subjects is unknown? (Hint: dynamic SQL / `CROSSTAB` in PostgreSQL)

---

### Q26. User Retention / Cohort Analysis (Google, Meta)

Given:

```
user_activity(user_id, activity_date DATE)
users(user_id, signup_date DATE)
```

**Problem:** Calculate Day-1, Day-7, and Day-30 retention rates for each weekly signup cohort.

```sql
WITH cohorts AS (
    SELECT
        user_id,
        DATE_TRUNC('week', signup_date) AS cohort_week
    FROM users
),
activity AS (
    SELECT
        c.cohort_week,
        c.user_id,
        a.activity_date - u.signup_date AS days_since_signup
    FROM cohorts c
    JOIN users u ON c.user_id = u.user_id
    JOIN user_activity a ON c.user_id = a.user_id
)
SELECT
    cohort_week,
    COUNT(DISTINCT user_id) AS cohort_size,
    COUNT(DISTINCT CASE WHEN days_since_signup = 1 THEN user_id END) * 100.0 /
        COUNT(DISTINCT user_id) AS day1_retention_pct,
    COUNT(DISTINCT CASE WHEN days_since_signup = 7 THEN user_id END) * 100.0 /
        COUNT(DISTINCT user_id) AS day7_retention_pct,
    COUNT(DISTINCT CASE WHEN days_since_signup = 30 THEN user_id END) * 100.0 /
        COUNT(DISTINCT user_id) AS day30_retention_pct
FROM activity
GROUP BY cohort_week
ORDER BY cohort_week;
```

---

### Q27. Delete Duplicate Rows, Keep One (Amazon, Google)

Given:

```
contacts(id, email, name, created_at)
-- duplicates exist on email
```

**Problem:** Delete all duplicate rows (by email), keeping only the row with the earliest `created_at`.

```sql
-- PostgreSQL
DELETE FROM contacts
WHERE id NOT IN (
    SELECT MIN(id)
    FROM contacts
    GROUP BY email
);

-- Alternative using CTE + window function
WITH ranked AS (
    SELECT id, ROW_NUMBER() OVER (PARTITION BY email ORDER BY created_at ASC, id ASC) AS rn
    FROM contacts
)
DELETE FROM contacts
WHERE id IN (SELECT id FROM ranked WHERE rn > 1);
```

**Follow-up:** How would you do this on a 500M-row table without locking it for hours? (Hint: batched deletes)

---

### Q28. Cumulative Distribution / Percentile Calculation (Stripe, Google)

Given:

```
payments(payment_id, merchant_id, amount)
```

**Problem:** For each payment, compute what percentile it falls into within its merchant's payment distribution. Also find the median payment amount per merchant.

```sql
SELECT
    payment_id,
    merchant_id,
    amount,
    PERCENT_RANK() OVER (PARTITION BY merchant_id ORDER BY amount) AS percentile,
    PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY amount)
        OVER (PARTITION BY merchant_id) AS median_amount
FROM payments;
```

---

### Q29. Recursive CTE: Organizational Hierarchy Traversal (Amazon, Google)

Given:

```
employees(employee_id, name, manager_id)
-- CEO has manager_id = NULL
```

**Problem:** Display the full organizational hierarchy showing each employee's level and the path from CEO to them.

```sql
WITH RECURSIVE org_tree AS (
    -- Base case: CEO (no manager)
    SELECT
        employee_id,
        name,
        manager_id,
        0 AS level,
        CAST(name AS VARCHAR(1000)) AS path
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive case: employees with managers
    SELECT
        e.employee_id,
        e.name,
        e.manager_id,
        ot.level + 1,
        CAST(ot.path || ' > ' || e.name AS VARCHAR(1000))
    FROM employees e
    JOIN org_tree ot ON e.manager_id = ot.employee_id
)
SELECT * FROM org_tree ORDER BY level, name;
```

**Follow-up:** How do you limit recursion depth to prevent infinite loops if there is a cycle in the data?

---

### Q30. Concurrent Transaction Isolation Problem (Google, Amazon)

**Problem (conceptual):** Two transactions run simultaneously:

```
-- Transaction A                    -- Transaction B
BEGIN;                              BEGIN;
SELECT balance FROM accounts
  WHERE id = 1; -- returns 1000
                                    SELECT balance FROM accounts
                                      WHERE id = 1; -- returns 1000
UPDATE accounts SET balance =
  balance - 500 WHERE id = 1;
                                    UPDATE accounts SET balance =
                                      balance - 800 WHERE id = 1;
COMMIT;                             COMMIT;
```

- (a) What is the final balance under READ COMMITTED isolation? Under SERIALIZABLE?
- (b) Explain the "lost update" problem illustrated here.
- (c) How does `SELECT ... FOR UPDATE` prevent this issue?
- (d) What is the performance trade-off of SERIALIZABLE vs. READ COMMITTED?
- (e) How do optimistic locking vs. pessimistic locking approaches differ in solving this?

---

## BONUS: Quick-Fire Conceptual Questions

**B1.** What is a correlated subquery? How does its execution differ from a non-correlated subquery? Give an example where a correlated subquery is the cleanest solution.

**B2.** Explain the difference between `EXISTS` and `IN`. When does `EXISTS` outperform `IN`? (Hint: NULL handling and short-circuit evaluation with large subquery results)

**B3.** What are the different types of table scan operations (Sequential Scan, Index Scan, Index-Only Scan, Bitmap Index Scan)? When does the optimizer choose each?

**B4.** You have a query that uses `ORDER BY RANDOM() LIMIT 1` to select a random row from a 100M-row table. Why is this catastrophically slow, and what are better alternatives?

**B5.** Explain write amplification in the context of database indexes. If a table has 8 indexes and you INSERT one row, how many write operations actually occur?

---

## Sources

- [InterviewBit SQL Interview Questions (2026)](https://www.interviewbit.com/sql-interview-questions/)
- [DataLemur SQL Interview Questions](https://datalemur.com/questions)
- [DataLemur: Google SQL Interview Questions](https://datalemur.com/blog/google-sql-interview-questions)
- [DataLemur: SQL Window Functions Interview Questions](https://datalemur.com/blog/sql-window-functions-interview-questions)
- [GeeksforGeeks: Amazon SQL Interview Questions](https://www.geeksforgeeks.org/sql/amazon-sql-interview-questions/)
- [GeeksforGeeks: Storage, Indexing & Advanced Topics Interview Questions](https://www.geeksforgeeks.org/dbms/storage-indexing-advanced-topics-interview-questions/)
- [GeeksforGeeks: Top 100 SQL Interview Questions (2025)](https://www.geeksforgeeks.org/sql/sql-interview-questions/)
- [Hello Interview: Database Indexing for System Design](https://www.hellointerview.com/learn/system-design/core-concepts/db-indexing)
- [DbVisualizer: SQL Performance Tuning Interview Questions](https://www.dbvis.com/thetable/top-sql-performance-tuning-interview-questions-and-answers/)
- [DataCamp: Top 84 SQL Interview Questions (2026)](https://www.datacamp.com/blog/top-sql-interview-questions-and-answers-for-beginners-and-intermediate-practitioners)
- [InterviewQuery: Google SQL Interview Questions (2025)](https://www.interviewquery.com/p/google-sql-interview-questions)
- [InterviewQuery: Amazon SQL Interview Questions (2025)](https://www.interviewquery.com/p/amazon-sql-interview-questions)
- [DataInterview: Top 100 SQL Interview Questions (FAANGs, Startups)](https://www.datainterview.com/blog/top-100-sql-interview-questions)
- [DesignGurus: SQL Query Optimization Interview Questions](https://www.designgurus.io/answers/detail/what-are-sql-query-optimization-interview-questions)
- [DataCamp: Denormalization in Databases](https://www.datacamp.com/tutorial/denormalization)
- [Medium: Data Engineering Interview Prep - Indexing in SQL](https://medium.com/@gokhale.nikit/data-engineering-interview-prep-challenge-day-11-indexing-in-sql-ca14d429fdfc)
