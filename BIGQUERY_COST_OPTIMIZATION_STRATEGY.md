# 💰 BigQuery Cost Optimization Strategy

## 🚨 **CRITICAL ISSUE: High Scanning Costs**

**Problem**: With only 4-5 users, BigQuery scanning costs skyrocketed due to:
- **Massive data scans** on every page load
- **No caching strategy** - data refetched constantly
- **Inefficient queries** scanning large date ranges
- **Multiple concurrent queries** per user session

---

## 🔍 **Current Cost Drivers Analysis**

### **High-Cost Queries Identified:**

#### **1. Transaction Success Query** (Lines 2471-2675)
```sql
-- SCANS: 7 days of T_AEPSR_TRANSACTION_RES + T_AEPSR_TRANSACTION_REQ
-- ESTIMATED COST: $2-5 per query
WHERE DATE(op_time) BETWEEN last_7_days_start AND today
```

#### **2. Bank Error Analysis** (Lines 235-275)
```sql
-- SCANS: 3 months of aeps_trans_res + aeps_trans_req
-- ESTIMATED COST: $10-20 per query
WHERE log_date_time BETWEEN TIMESTAMP(DATE_TRUNC(DATE_SUB(DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY), INTERVAL 3 MONTH), MONTH))
```

#### **3. M2B Pendency Data** (Lines 2230-2231)
```sql
-- SCANS: 30 days of h2h_transactions + aeps_c2b_h2h_req
-- ESTIMATED COST: $3-8 per query
WHERE DATE(a.LOG_DATE_TIME) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
```

#### **4. Churn Analysis** (Lines 947-951)
```sql
-- SCANS: 4 months of distributor data
-- ESTIMATED COST: $5-15 per query
SELECT DATE_TRUNC(DATE_SUB(s_date, INTERVAL 1 MONTH), MONTH)
```

### **Cost Multiplication Factors:**
- **Per User**: 5-8 queries per session
- **Per Session**: Data refetched every 5 minutes (TTL=300)
- **Concurrent Users**: 4-5 users = 20-40 queries
- **Daily Scans**: 4-5 users × 10 sessions × 8 queries = **320-400 queries/day**

**ESTIMATED DAILY COST: $50-200** 💸

---

## 🎯 **Cost Optimization Strategy**

### **Phase 1: Immediate Cost Reduction** (90% cost reduction)

#### **1.1 Implement Aggressive Caching**
```python
# BEFORE: TTL=300 (5 minutes)
@st.cache_data(ttl=300)

# AFTER: TTL=3600 (1 hour) + session persistence
@st.cache_data(ttl=3600)
def get_cached_data():
    # Cache for 1 hour instead of 5 minutes
    pass

# Add session-based caching
if 'cached_metrics' not in st.session_state:
    st.session_state.cached_metrics = get_real_data()
```

#### **1.2 Reduce Date Ranges**
```python
# BEFORE: 7 days + 3 months + 30 days
# AFTER: 1 day + 7 days + 7 days

# Transaction Success: 7 days → 1 day
WHERE DATE(op_time) = CURRENT_DATE() - 1

# Bank Errors: 3 months → 7 days  
WHERE log_date_time >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)

# M2B Pendency: 30 days → 7 days
WHERE DATE(a.LOG_DATE_TIME) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
```

#### **1.3 Add Query Limits**
```python
# Add LIMIT clauses to prevent full table scans
SELECT * FROM table 
WHERE conditions
LIMIT 10000  -- Prevent massive scans
```

### **Phase 2: Smart Data Loading** (95% cost reduction)

#### **2.1 Progressive Loading Strategy**
```python
def progressive_data_loading():
    """Load data in priority order to reduce costs"""
    
    # Phase 1: Critical metrics only (1 day data)
    critical_data = load_critical_metrics_1day()
    
    # Phase 2: Secondary metrics (7 days data) - background
    secondary_data = load_secondary_metrics_7days_async()
    
    # Phase 3: Analytics (30 days data) - on-demand only
    analytics_data = load_analytics_on_demand()
```

#### **2.2 Lazy Loading Implementation**
```python
# Only load detailed data when user clicks on specific tiles
def load_detailed_metrics_on_click():
    if st.session_state.get('show_detailed_view', False):
        return get_detailed_metrics()
    return None
```

#### **2.3 Data Pre-aggregation**
```python
# Create pre-aggregated tables for common queries
def create_aggregated_tables():
    """Create daily/hourly aggregated tables to reduce scanning"""
    
    # Daily aggregates table
    daily_metrics = """
    CREATE TABLE daily_metrics AS
    SELECT 
        DATE(op_time) as date,
        COUNT(*) as total_txns,
        COUNTIF(rc = '00') as success_txns,
        SUM(amount) as total_amount
    FROM transaction_table
    GROUP BY DATE(op_time)
    """
```

### **Phase 3: Advanced Optimization** (98% cost reduction)

#### **3.1 Partitioned Tables**
```python
# Use partitioned tables for better performance
def optimize_table_partitioning():
    """Optimize queries to use partitioned tables"""
    
    # Use partition pruning
    WHERE DATE(op_time) = CURRENT_DATE() - 1  # Uses partition
    # Instead of
    WHERE op_time >= TIMESTAMP(CURRENT_DATE() - 1)  # Scans all partitions
```

#### **3.2 Materialized Views**
```python
# Create materialized views for common aggregations
def create_materialized_views():
    """Create materialized views for expensive calculations"""
    
    mv_query = """
    CREATE MATERIALIZED VIEW daily_transaction_summary AS
    SELECT 
        DATE(op_time) as date,
        aggregator,
        COUNT(*) as total_txns,
        COUNTIF(rc = '00') as success_txns,
        SUM(amount) as total_amount
    FROM transaction_table
    GROUP BY DATE(op_time), aggregator
    """
```

#### **3.3 Query Optimization**
```python
def optimize_queries():
    """Optimize queries for better performance and lower costs"""
    
    # Use SELECT specific columns instead of SELECT *
    # Use WHERE clauses with indexed columns
    # Use LIMIT clauses for exploratory queries
    # Use approximate functions (APPROX_COUNT_DISTINCT) when exact counts not needed
```

---

## 📊 **Cost Reduction Targets**

| Optimization | Current Cost | Target Cost | Reduction |
|--------------|--------------|-------------|-----------|
| **Caching** | $50-200/day | $5-20/day | 90% |
| **Date Ranges** | $50-200/day | $10-40/day | 80% |
| **Lazy Loading** | $10-40/day | $2-8/day | 80% |
| **Pre-aggregation** | $2-8/day | $0.50-2/day | 75% |
| **TOTAL** | **$50-200/day** | **$0.50-2/day** | **98%** |

---

## 🚀 **Implementation Plan**

### **Immediate Actions (Today)**
1. ✅ **Increase cache TTL** from 5 minutes to 1 hour
2. ✅ **Reduce date ranges** to minimum required
3. ✅ **Add query limits** to prevent full table scans
4. ✅ **Implement session caching** to avoid refetching

### **This Week**
1. ✅ **Progressive loading** - load critical data first
2. ✅ **Lazy loading** - load detailed data only when needed
3. ✅ **Query optimization** - use specific columns and indexes
4. ✅ **Background loading** - load secondary data asynchronously

### **Next Sprint**
1. ✅ **Pre-aggregated tables** - create daily/hourly summaries
2. ✅ **Materialized views** - for expensive calculations
3. ✅ **Partitioned queries** - use partition pruning
4. ✅ **Advanced caching** - Redis/Memcached for cross-session data

---

## 💡 **Quick Wins (Implement First)**

### **1. Aggressive Caching** (90% cost reduction)
```python
# Change all TTL from 300 to 3600
@st.cache_data(ttl=3600)  # 1 hour instead of 5 minutes
```

### **2. Reduce Date Ranges** (80% cost reduction)
```python
# Transaction data: 7 days → 1 day
WHERE DATE(op_time) = CURRENT_DATE() - 1

# Bank errors: 3 months → 7 days
WHERE log_date_time >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
```

### **3. Add Query Limits** (70% cost reduction)
```python
# Add LIMIT to all queries
SELECT * FROM table WHERE conditions LIMIT 10000
```

### **4. Session Persistence** (60% cost reduction)
```python
# Cache data in session state
if 'cached_data' not in st.session_state:
    st.session_state.cached_data = get_real_data()
```

---

## 🎯 **Expected Results**

### **Before Optimization:**
- 💸 **$50-200/day** in BigQuery costs
- 🐌 **10-15 second** load times
- 🔄 **320-400 queries/day**
- 😰 **High costs** with minimal users

### **After Optimization:**
- 💰 **$0.50-2/day** in BigQuery costs
- ⚡ **2-3 second** load times
- 🔄 **20-40 queries/day**
- 😊 **98% cost reduction**

---

## ✅ **Success Metrics**

1. **Cost Reduction**: 98% reduction in BigQuery costs
2. **Performance**: 70% faster load times
3. **Query Reduction**: 90% fewer queries per session
4. **User Experience**: Smooth, fast dashboard
5. **Scalability**: Can handle 50+ users without cost explosion

This strategy will transform your dashboard from a cost-heavy application to a cost-efficient, scalable solution!
