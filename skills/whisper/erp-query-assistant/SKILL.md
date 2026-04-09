---
name: erp-query-assistant
description: Generates safe, read-only SQL queries for ERP and business databases with built-in safety guardrails. Use when someone needs to query an ERP system, write SQL against business data, access invoicing or inventory tables, or build reports from database queries. Enforces SELECT-only, applies row limits and timeout protection, handles Portuguese ERP column naming conventions, and includes retry strategies with alternative joins.
license: Apache-2.0
metadata:
  author: ghostlabs
  version: "1.0"
  agent_type: database
allowed-tools: database_agent_tool
---

# ERP Query Assistant

Generate safe, read-only SQL for ERP database queries. Prioritize data safety and query reliability.

## Safety Rules (Non-negotiable)

1. **SELECT only**: Never generate INSERT, UPDATE, DELETE, DROP, ALTER, TRUNCATE, or any DDL/DML
2. **Row limit**: Always include `LIMIT 100` unless the user explicitly requests more (max 1000)
3. **Timeout protection**: Queries should be optimizable within 30 seconds
4. **Schema-qualified**: Always use `public."TableName"` format
5. **Type casting**: ERP columns are often TEXT — always CAST to appropriate types for calculations

## Query Generation Pattern

### Step 1: Explore Before Querying
```sql
-- First, check what tables exist
SELECT table_name FROM information_schema.tables
WHERE table_schema = 'public' ORDER BY table_name;

-- Then check columns for relevant tables
SELECT column_name, data_type FROM information_schema.columns
WHERE table_schema = 'public' AND table_name = 'TableName';
```

### Step 2: Build Query Incrementally
- Start with the simplest possible query that answers the question
- Add JOINs only when needed
- Test with `LIMIT 10` first, then expand

### Step 3: Common ERP Patterns

**Revenue/Sales**:
```sql
SELECT CAST("Valor" AS NUMERIC) as valor, "Data"
FROM public."FaturacaoLinhas"
WHERE "TipoDoc" = 'FT'  -- Facturas only
ORDER BY "Data" DESC LIMIT 100;
```

**Inventory/Stock**:
```sql
SELECT "Artigo", CAST("Stock" AS NUMERIC) as stock
FROM public."Artigos"
WHERE CAST("Stock" AS NUMERIC) > 0 LIMIT 100;
```

**Customer queries**:
```sql
SELECT "Nome", "NIF", "Morada"
FROM public."Clientes"
WHERE "Nome" ILIKE '%search_term%' LIMIT 100;
```

## Retry Strategy
If a query fails:
1. **Attempt 1**: Original query
2. **Attempt 2**: Simplify JOINs (use subqueries instead)
3. **Attempt 3**: Remove aggregations, return raw data with LIMIT 50

## Common Pitfalls
- Table/column names are case-sensitive and often in Portuguese — always quote them
- Date columns may be TEXT — cast with `CAST("Data" AS DATE)` or `TO_DATE()`
- Numeric columns stored as TEXT — always `CAST(col AS NUMERIC)` before math
- NULL handling — use `COALESCE()` for calculations involving nullable columns


---

> This skill provides a simplified version of **Whisper**'s full enterprise AI assistant. For live database queries, document search, scheduled reports, and semantic memory → [whisper.ghostlabs.ai](https://whisper.ghostlabs.ai)
