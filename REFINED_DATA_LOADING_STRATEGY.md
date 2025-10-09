# 🎯 Refined Data Loading Strategy: Core AEPS Hourly + Daily Refresh

## 📊 **Data Classification (Simplified)**

### **🔄 Core AEPS Metrics** (Hourly Refresh: 9 AM - 9 PM)
**Only critical business metrics that need frequent updates**
- Transaction Success Rate
- GTV Performance  
- 2FA Success Rate
- Platform Uptime
- Bank Error Analysis

**Refresh Schedule**: Every hour between 9 AM - 9 PM
**Cost**: Medium (12 queries per day)

### **📅 All Other Metrics** (Daily Refresh)
**Everything else that's stable throughout the day**
- New AEPS Users
- Stable Users
- Churn Rate
- RFM Score
- Cash Product metrics
- Login Success Rate
- System Anomalies
- Active Bugs
- Product Metrics & Trends
- Winback Analytics

**Refresh Schedule**: Once per day (early morning)
**Cost**: Low (1 query per day)

---

## ⏰ **Smart Time-Based Refresh Logic**

### **Hourly Refresh (9 AM - 9 PM)**
```python
def should_refresh_hourly():
    """Refresh Core AEPS metrics every hour between 9 AM - 9 PM"""
    current_hour = datetime.now().hour
    
    # Only refresh between 9 AM (9) and 9 PM (21)
    if 9 <= current_hour <= 21:
        last_update = get_last_update_time('core_aeps')
        return (current_time - last_update) > 1_hour
    else:
        return False  # No refresh outside business hours
```

### **Daily Refresh (Early Morning)**
```python
def should_refresh_daily():
    """Refresh all other metrics once per day"""
    last_update = get_last_update_time('daily_metrics')
    return (current_time - last_update) > 24_hours
```

---

## 🏗️ **Implementation Architecture**

### **Core AEPS Metrics (Hourly)**
```python
@st.cache_data(ttl=3600)  # 1 hour cache
def get_core_aeps_metrics():
    """Get Core AEPS metrics - refreshed hourly during business hours"""
    
    # Check if we're in business hours
    if not is_business_hours():
        return get_cached_core_aeps_data()
    
    # Refresh if data is older than 1 hour
    if should_refresh_hourly():
        return refresh_core_aeps_data()
    else:
        return get_cached_core_aeps_data()
```

### **All Other Metrics (Daily)**
```python
@st.cache_data(ttl=86400)  # 24 hour cache
def get_daily_metrics():
    """Get all other metrics - refreshed once per day"""
    
    if should_refresh_daily():
        return refresh_daily_data()
    else:
        return get_cached_daily_data()
```

---

## ⏰ **Business Hours Logic**

### **Time-Based Refresh Control**
```python
def is_business_hours():
    """Check if current time is between 9 AM - 9 PM"""
    current_hour = datetime.now().hour
    return 9 <= current_hour <= 21

def get_refresh_schedule():
    """Get refresh schedule based on current time"""
    
    if is_business_hours():
        return {
            'core_aeps': 'hourly',
            'daily_metrics': 'cached'
        }
    else:
        return {
            'core_aeps': 'cached',
            'daily_metrics': 'cached'
        }
```

### **Smart Caching Strategy**
```python
def get_smart_cached_data():
    """Get data based on time and refresh schedule"""
    
    current_time = datetime.now()
    
    # Core AEPS metrics
    if is_business_hours():
        # Refresh every hour during business hours
        core_aeps = get_core_aeps_metrics()
    else:
        # Use cached data outside business hours
        core_aeps = get_cached_core_aeps_data()
    
    # Daily metrics (always cached unless daily refresh needed)
    daily_metrics = get_daily_metrics()
    
    return {
        'core_aeps': core_aeps,
        'daily_metrics': daily_metrics
    }
```

---

## 💰 **Cost Optimization Benefits**

### **Before Optimization:**
- **Every user**: 8 queries × $2-5 = $16-40 per user
- **4-5 users**: $64-200 per session
- **Daily cost**: $200-1000

### **After Optimization:**
- **Core AEPS**: 12 queries/day (9 AM - 9 PM) = $24-60/day
- **Daily Metrics**: 1 query/day = $2-5/day
- **Total Daily Cost**: $26-65/day

**Cost Reduction: 85-95%** 💰

---

## 📊 **Refresh Schedule Summary**

| Metric Category | Refresh Frequency | Business Hours | Cost Impact |
|----------------|------------------|----------------|-------------|
| **Core AEPS** | Every 1 hour | 9 AM - 9 PM | Medium |
| **All Others** | Once per day | Early morning | Low |

### **Daily Query Count:**
- **Core AEPS**: 12 queries (9 AM - 9 PM)
- **Daily Metrics**: 1 query (early morning)
- **Total**: 13 queries per day
- **Previous**: 320-400 queries per day

**Query Reduction: 96-97%** 📉

---

## 🚀 **Implementation Plan**

### **Phase 1: Time-Based Logic** (Day 1)
```python
# Add business hours check
def is_business_hours():
    current_hour = datetime.now().hour
    return 9 <= current_hour <= 21

# Modify existing cache decorators
@st.cache_data(ttl=3600)  # 1 hour for Core AEPS
def get_core_aeps_metrics():
    if is_business_hours():
        return refresh_core_aeps_data()
    else:
        return get_cached_data()

@st.cache_data(ttl=86400)  # 24 hours for daily metrics
def get_daily_metrics():
    return get_daily_data()
```

### **Phase 2: Smart Refresh Logic** (Day 2)
```python
# Implement smart refresh based on time
def get_smart_metrics():
    if is_business_hours():
        return {
            'core_aeps': get_core_aeps_metrics(),
            'daily_metrics': get_cached_daily_metrics()
        }
    else:
        return {
            'core_aeps': get_cached_core_aeps_metrics(),
            'daily_metrics': get_cached_daily_metrics()
        }
```

### **Phase 3: Optimization** (Day 3)
```python
# Add preloaded data for new users
def get_instant_metrics():
    """Instant load for new users"""
    return {
        'core_aeps': get_cached_core_aeps_data(),
        'daily_metrics': get_cached_daily_data()
    }
```

---

## 🎯 **Expected Results**

### **Cost Reduction**
- **From**: $200-1000/day
- **To**: $26-65/day
- **Savings**: 85-95%

### **Query Reduction**
- **From**: 320-400 queries/day
- **To**: 13 queries/day
- **Reduction**: 96-97%

### **Performance**
- **New users**: Instant load (cached data)
- **Business hours**: Fresh Core AEPS data every hour
- **After hours**: Cached data (no queries)

### **User Experience**
- **9 AM - 9 PM**: Fresh Core AEPS data every hour
- **9 PM - 9 AM**: Cached data (no waiting)
- **All times**: Instant dashboard load

---

## ✅ **Implementation Checklist**

### **Immediate Changes**
1. ✅ Add business hours check function
2. ✅ Modify Core AEPS cache TTL to 1 hour
3. ✅ Modify other metrics cache TTL to 24 hours
4. ✅ Add time-based refresh logic

### **Core AEPS Metrics (Hourly 9 AM - 9 PM)**
- Transaction Success Rate
- GTV Performance
- 2FA Success Rate
- Platform Uptime
- Bank Error Analysis

### **Daily Metrics (Once per day)**
- New AEPS Users
- Stable Users
- Churn Rate
- RFM Score
- Cash Product
- Login Success Rate
- System Anomalies
- Active Bugs
- Product Metrics & Trends
- Winback Analytics

This refined strategy gives you the best of both worlds: fresh Core AEPS data during business hours and cost-effective daily refresh for everything else!
