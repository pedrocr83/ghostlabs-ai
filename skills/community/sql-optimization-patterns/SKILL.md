---
name: sql-optimization-patterns
description: Optimizes PostgreSQL queries using proven patterns for indexing, joins, CTEs, and pagination. Use when someone has a slow query, needs to read an EXPLAIN plan, wants index strategy advice, is choosing between CTE and subquery, or needs keyset pagination. Covers B-tree/GIN/GiST index selection, join optimization (nested loop vs hash vs merge), CTE vs subquery trade-offs, offset vs keyset pagination, and common SQL anti-patterns with fixes.
license: Apache-2.0
metadata:
  author: community
  version: "1.0"
  original_source: wshobson/sql-optimization-patterns
allowed-tools: database_agent_tool
---

# SQL Optimization Patterns

Practical patterns for writing efficient PostgreSQL queries and diagnosing performance issues.

## Query Analysis with EXPLAIN

Always analyze before optimizing:
```sql
EXPLAIN (ANALYZE, BUFFERS, FORMAT TEXT)
SELECT ... FROM ... WHERE ...;
```

### Reading EXPLAIN Output
- **Seq Scan**: Full table scan — consider adding an index if table is large
- **Index Scan**: Using index — good for selective queries (<5% of rows)
- **Index Only Scan**: Best case — all data from index, no table access
- **Bitmap Index Scan**: Good for medium selectivity (5-20% of rows)
- **Nested Loop**: Efficient for small inner tables (<1000 rows)
- **Hash Join**: Efficient for medium-large equi-joins
- **Merge Join**: Efficient when both sides are pre-sorted
- **Sort**: Check if index can eliminate sort
- **actual time**: First number = first row, second = all rows

## Index Strategy

### When to Create Indexes
- Columns in WHERE clauses queried frequently
- Columns in JOIN conditions
- Columns in ORDER BY (eliminates sort)
- Columns in GROUP BY with aggregations

### When NOT to Create Indexes
- Tables with < 1000 rows (seq scan is often faster)
- Columns with low cardinality (boolean, status with 3 values)
- Tables with heavy write load (indexes slow writes)
- Columns rarely queried

### Index Types
```sql
-- B-tree (default, most common)
CREATE INDEX idx_name ON table(column);

-- Partial index (only index rows matching condition)
CREATE INDEX idx_active ON users(email) WHERE is_active = TRUE;

-- Composite index (multi-column, order matters)
CREATE INDEX idx_comp ON orders(customer_id, created_at DESC);

-- GIN index (for JSONB, arrays, full-text)
CREATE INDEX idx_json ON products USING GIN(metadata);

-- GiST index (for geometric, range, full-text)
CREATE INDEX idx_geo ON locations USING GiST(coordinates);
```

## Join Optimization

### Use Explicit JOIN over Subqueries
```sql
-- Prefer this (JOIN)
SELECT o.id, c.name
FROM orders o
JOIN customers c ON o.customer_id = c.id;

-- Over this (subquery)
SELECT o.id, (SELECT name FROM customers WHERE id = o.customer_id)
FROM orders o;
```

### Join Order Matters
- Put the smaller table first in JOINs (PostgreSQL optimizer handles this, but helps readability)
- Filter early: Apply WHERE conditions before joining when possible

## CTE vs Subquery

### Use CTE When
- Query is referenced multiple times
- Complex logic benefits from named intermediate steps
- Recursive queries needed

### Use Subquery When
- Single-use intermediate result
- Performance-critical (CTEs were optimization barriers before PG 12)
- Simple filtering or existence checks

```sql
-- CTE for complex, multi-reference queries
WITH monthly_revenue AS (
    SELECT DATE_TRUNC('month', created_at) AS month,
           SUM(amount) AS revenue
    FROM orders
    WHERE created_at >= NOW() - INTERVAL '1 year'
    GROUP BY month
)
SELECT month, revenue,
       LAG(revenue) OVER (ORDER BY month) AS prev_revenue,
       revenue - LAG(revenue) OVER (ORDER BY month) AS growth
FROM monthly_revenue;

-- Subquery for single-use filters
SELECT * FROM products
WHERE category_id IN (SELECT id FROM categories WHERE is_featured = TRUE);
```

## Pagination Patterns

### Offset Pagination (Simple, Gets Slow)
```sql
SELECT * FROM products ORDER BY id LIMIT 20 OFFSET 100;
-- Problem: DB scans 120 rows, discards 100
```

### Keyset Pagination (Fast, Consistent)
```sql
SELECT * FROM products
WHERE id > :last_seen_id
ORDER BY id LIMIT 20;
-- Always fast: index seek directly to starting point
```

### Rule: Use keyset pagination when possible. Use offset only for admin UIs where exact page numbers matter.

## Common Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| `SELECT *` | Select only needed columns |
| `WHERE col LIKE '%term%'` | Use full-text search (tsvector) or trigram index |
| `WHERE function(col) = value` | Create expression index or restructure |
| `COUNT(*)` on large tables | Use `pg_class.reltuples` for estimates |
| `NOT IN (subquery)` with NULLs | Use `NOT EXISTS` instead |
| Repeated identical subqueries | Extract to CTE |
| Missing LIMIT on unbounded queries | Always LIMIT, especially in APIs |
