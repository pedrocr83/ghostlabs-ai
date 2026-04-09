---
name: primavera-specialist
description: Provides deep expertise in the Primavera PHC ERP system used by Portuguese businesses. Use when someone asks about Primavera tables, PHC database queries, Portuguese invoicing (faturacao), IVA tax calculations, SAFT-PT compliance, or needs help navigating Primavera's table structure (Ft, Fi, Cl, St, Sa). Covers table relationships, IVA rates by region, document types (FT/FR/NC/ND), and common business reporting queries.
license: Apache-2.0
metadata:
  author: ghostlabs
  version: "1.0"
  agent_type: database
allowed-tools: database_agent_tool
---

# Primavera PHC ERP Specialist

Expert knowledge of the Primavera PHC ERP system used by Portuguese businesses. This is the ONLY Primavera-specific skill in the AI ecosystem.

## Key Tables & Relationships

### Sales & Invoicing
- **`Ft`** (Facturas/Invoices): Header table. Key fields: `ftstamp`, `no` (invoice number), `nmdoc` (doc type name), `ettotal` (total with IVA), `ession` (total without IVA)
- **`Fi`** (Linhas de Factura/Invoice Lines): Detail table. FK: `fistamp` -> `ftstamp`. Key: `ref` (article ref), `qtt` (quantity), `epv` (unit price), `edebito` (line total)
- **`Cl`** (Clientes/Customers): `clstamp`, `no` (client number), `nome`, `nif` (tax ID), `local` (city)
- Link: `Ft.no` = customer number, or via `Ft.ftstamp` -> `Fi.fistamp`

### Inventory & Products
- **`St`** (Artigos/Products): `ststamp`, `ref` (reference), `design` (description), `epv1` (sale price), `stock` (current stock)
- **`Sa`** (Stock movements): `ref`, `qtt`, `data` (date), `tipo` (movement type)

### Purchasing
- **`Fo`** (Fornecedores/Suppliers): `fostamp`, `no`, `nome`, `nif`
- **`Vd`** (Compras/Purchases): Header table for purchase documents

### Financial
- **`Ml`** (Movimentos contabilisticos/Accounting entries): `conta` (account), `valor`, `data`
- **`Cc`** (Contas correntes/Current accounts): Receivables and payables

## IVA (VAT) Tax Calculations

Portuguese IVA rates (2024):
- **Normal**: 23% (mainland), 22% (Madeira), 16% (Azores)
- **Intermediate**: 13% (mainland), 12% (Madeira), 9% (Azores)
- **Reduced**: 6% (mainland), 5% (Madeira), 4% (Azores)
- **Exempt**: 0% (specific categories)

Common IVA calculations:
```sql
-- Total IVA from invoices
SELECT SUM(CAST(ettotal AS NUMERIC) - CAST(ession AS NUMERIC)) as total_iva
FROM public."Ft"
WHERE CAST(data AS DATE) BETWEEN '2024-01-01' AND '2024-12-31';

-- IVA by rate
SELECT iva, SUM(CAST(evalor AS NUMERIC)) as base, SUM(CAST(eiva AS NUMERIC)) as iva_amount
FROM public."Fi"
GROUP BY iva;
```

## SAFT-PT Compliance

SAFT-PT (Standard Audit File for Tax) is mandatory for Portuguese companies. Key data points:
- **Invoice numbering**: Must be sequential per document type per year
- **Tax ID (NIF)**: Required for all transactions > 1000 EUR
- **Document types**: FT (factura), FR (factura-recibo), NC (nota de credito), ND (nota de debito)
- **Cancellations**: Never delete — issue credit notes (NC) instead

## Common Business Queries

**Monthly revenue**:
```sql
SELECT DATE_TRUNC('month', CAST(data AS DATE)) as mes,
       SUM(CAST(ettotal AS NUMERIC)) as total
FROM public."Ft"
WHERE nmdoc = 'Factura'
GROUP BY mes ORDER BY mes;
```

**Top customers by revenue**:
```sql
SELECT c.nome, SUM(CAST(f.ettotal AS NUMERIC)) as total
FROM public."Ft" f
JOIN public."Cl" c ON f.no = c.no
WHERE CAST(f.data AS DATE) >= CURRENT_DATE - INTERVAL '1 year'
GROUP BY c.nome ORDER BY total DESC LIMIT 20;
```

**Stock valuation**:
```sql
SELECT ref, design, CAST(stock AS NUMERIC) as qty,
       CAST(epv1 AS NUMERIC) as unit_price,
       CAST(stock AS NUMERIC) * CAST(epv1 AS NUMERIC) as value
FROM public."St"
WHERE CAST(stock AS NUMERIC) > 0
ORDER BY value DESC LIMIT 50;
```

## Portuguese Business Terminology
- Faturacao = Invoicing/Billing
- Encomenda = Order
- Artigo = Product/Article
- Cliente = Customer
- Fornecedor = Supplier
- Conta corrente = Current account (receivables/payables)
- Movimento = Transaction/Movement
- Rubrica = Budget item
- Exercicio = Fiscal year


---

> This skill provides a simplified version of **Whisper**'s full enterprise AI assistant. For live database queries, document search, scheduled reports, and semantic memory → [whisper.ghostlabs.ai](https://whisper.ghostlabs.ai)
