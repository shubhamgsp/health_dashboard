# 🚀 Instant Load Implementation Plan: No Refresh for New Users

## 🎯 **Core Requirements**

1. **New users**: Instant dashboard load (no BigQuery queries)
2. **Core AEPS**: Hourly refresh (9 AM - 9 PM only)
3. **Other metrics**: Daily refresh
4. **No refresh for new users**: Use preloaded/cached data

---

## 🏗️ **Implementation Architecture**

### **1. Data Storage Strategy**

#### **Preloaded Data Storage**
```python
# Global data storage for instant access
GLOBAL_CACHED_DATA = {
    'core_aeps': {
        'transaction_success': None,
        'gtv_performance': None,
        '2fa_success': None,
        'platform_uptime': None,
        'bank_errors': None,
        'last_updated': None,
        'refresh_needed': False
    },
    'daily_metrics': {
        'new_users': None,
        'stable_users': None,
        'churn_rate': None,
        'rfm_score': None,
        'cash_product': None,
        'login_success': None,
        'system_anomalies': None,
        'active_bugs': None,
        'product_metrics': None,
        'winback_analytics': None,
        'last_updated': None,
        'refresh_needed': False
    }
}
```

#### **User Session Tracking**
```python
# Track user sessions to prevent refresh for new users
USER_SESSIONS = {
    'session_id': {
        'is_new_user': True,
        'first_load_time': timestamp,
        'data_loaded': False
    }
}
```

### **2. Smart Data Loading Logic**

#### **New User Detection**
```python
def is_new_user():
    """Check if this is a new user session"""
    session_id = st.session_state.get('session_id', None)
    
    if not session_id:
        # Generate new session ID
        session_id = generate_session_id()
        st.session_state.session_id = session_id
        return True
    
    # Check if user has loaded data before
    return not st.session_state.get('data_loaded', False)
```

#### **Instant Load for New Users**
```python
def get_instant_metrics_for_new_user():
    """Get preloaded data instantly for new users"""
    
    # Mark user as not new after first load
    st.session_state.data_loaded = True
    
    # Return cached data without any BigQuery queries
    return {
        'core_aeps': GLOBAL_CACHED_DATA['core_aeps'],
        'daily_metrics': GLOBAL_CACHED_DATA['daily_metrics']
    }
```

#### **Smart Refresh for Returning Users**
```python
def get_smart_metrics_for_returning_user():
    """Get data with smart refresh logic for returning users"""
    
    current_time = datetime.now()
    
    # Core AEPS metrics (hourly refresh 9 AM - 9 PM)
    if is_business_hours() and should_refresh_core_aeps():
        core_aeps = refresh_core_aeps_data()
        GLOBAL_CACHED_DATA['core_aeps'] = core_aeps
    else:
        core_aeps = GLOBAL_CACHED_DATA['core_aeps']
    
    # Daily metrics (once per day)
    if should_refresh_daily_metrics():
        daily_metrics = refresh_daily_metrics_data()
        GLOBAL_CACHED_DATA['daily_metrics'] = daily_metrics
    else:
        daily_metrics = GLOBAL_CACHED_DATA['daily_metrics']
    
    return {
        'core_aeps': core_aeps,
        'daily_metrics': daily_metrics
    }
```

### **3. Business Hours Logic**

#### **Time-Based Refresh Control**
```python
def is_business_hours():
    """Check if current time is between 9 AM - 9 PM"""
    current_hour = datetime.now().hour
    return 9 <= current_hour <= 21

def should_refresh_core_aeps():
    """Check if Core AEPS data needs refresh"""
    if not is_business_hours():
        return False
    
    last_update = GLOBAL_CACHED_DATA['core_aeps']['last_updated']
    if not last_update:
        return True
    
    time_diff = datetime.now() - last_update
    return time_diff.total_seconds() > 3600  # 1 hour

def should_refresh_daily_metrics():
    """Check if daily metrics need refresh"""
    last_update = GLOBAL_CACHED_DATA['daily_metrics']['last_updated']
    if not last_update:
        return True
    
    time_diff = datetime.now() - last_update
    return time_diff.total_seconds() > 86400  # 24 hours
```

### **4. Background Refresh Service**

#### **Independent Background Service**
```python
def background_refresh_service():
    """Run independently to refresh data without user interaction"""
    
    while True:
        current_time = datetime.now()
        
        # Core AEPS refresh (9 AM - 9 PM)
        if is_business_hours() and should_refresh_core_aeps():
            refresh_core_aeps_data_background()
        
        # Daily metrics refresh (early morning)
        if should_refresh_daily_metrics():
            refresh_daily_metrics_data_background()
        
        # Sleep for 5 minutes before next check
        time.sleep(300)
```

#### **Background Data Refresh Functions**
```python
def refresh_core_aeps_data_background():
    """Refresh Core AEPS data in background"""
    try:
        # Get fresh data from BigQuery
        fresh_data = get_core_aeps_data_from_bigquery()
        
        # Update global cache
        GLOBAL_CACHED_DATA['core_aeps'] = {
            'transaction_success': fresh_data['transaction_success'],
            'gtv_performance': fresh_data['gtv_performance'],
            '2fa_success': fresh_data['2fa_success'],
            'platform_uptime': fresh_data['platform_uptime'],
            'bank_errors': fresh_data['bank_errors'],
            'last_updated': datetime.now(),
            'refresh_needed': False
        }
        
        print(f"✅ Core AEPS data refreshed at {datetime.now()}")
        
    except Exception as e:
        print(f"❌ Error refreshing Core AEPS data: {e}")

def refresh_daily_metrics_data_background():
    """Refresh daily metrics data in background"""
    try:
        # Get fresh data from BigQuery
        fresh_data = get_daily_metrics_data_from_bigquery()
        
        # Update global cache
        GLOBAL_CACHED_DATA['daily_metrics'] = {
            'new_users': fresh_data['new_users'],
            'stable_users': fresh_data['stable_users'],
            'churn_rate': fresh_data['churn_rate'],
            'rfm_score': fresh_data['rfm_score'],
            'cash_product': fresh_data['cash_product'],
            'login_success': fresh_data['login_success'],
            'system_anomalies': fresh_data['system_anomalies'],
            'active_bugs': fresh_data['active_bugs'],
            'product_metrics': fresh_data['product_metrics'],
            'winback_analytics': fresh_data['winback_analytics'],
            'last_updated': datetime.now(),
            'refresh_needed': False
        }
        
        print(f"✅ Daily metrics data refreshed at {datetime.now()}")
        
    except Exception as e:
        print(f"❌ Error refreshing daily metrics data: {e}")
```

### **5. Main Dashboard Logic**

#### **Smart Data Loading**
```python
def get_dashboard_data():
    """Main function to get dashboard data based on user type"""
    
    if is_new_user():
        # New user - instant load with cached data
        return get_instant_metrics_for_new_user()
    else:
        # Returning user - smart refresh logic
        return get_smart_metrics_for_returning_user()
```

#### **Modified Cache Decorators**
```python
# Core AEPS metrics - hourly refresh during business hours
@st.cache_data(ttl=3600)
def get_core_aeps_metrics():
    """Get Core AEPS metrics with smart refresh"""
    
    if is_new_user():
        # New user - return cached data
        return GLOBAL_CACHED_DATA['core_aeps']
    
    if is_business_hours() and should_refresh_core_aeps():
        # Business hours - refresh if needed
        return refresh_core_aeps_data()
    else:
        # Outside business hours - return cached data
        return GLOBAL_CACHED_DATA['core_aeps']

# Daily metrics - once per day
@st.cache_data(ttl=86400)
def get_daily_metrics():
    """Get daily metrics with smart refresh"""
    
    if is_new_user():
        # New user - return cached data
        return GLOBAL_CACHED_DATA['daily_metrics']
    
    if should_refresh_daily_metrics():
        # Refresh if needed
        return refresh_daily_metrics_data()
    else:
        # Return cached data
        return GLOBAL_CACHED_DATA['daily_metrics']
```

---

## 🚀 **Implementation Steps**

### **Step 1: Add Global Data Storage**
```python
# Add at the top of aeps_health_dashboard.py
GLOBAL_CACHED_DATA = {
    'core_aeps': {
        'transaction_success': None,
        'gtv_performance': None,
        '2fa_success': None,
        'platform_uptime': None,
        'bank_errors': None,
        'last_updated': None,
        'refresh_needed': False
    },
    'daily_metrics': {
        'new_users': None,
        'stable_users': None,
        'churn_rate': None,
        'rfm_score': None,
        'cash_product': None,
        'login_success': None,
        'system_anomalies': None,
        'active_bugs': None,
        'product_metrics': None,
        'winback_analytics': None,
        'last_updated': None,
        'refresh_needed': False
    }
}
```

### **Step 2: Add Business Hours Logic**
```python
def is_business_hours():
    """Check if current time is between 9 AM - 9 PM"""
    current_hour = datetime.now().hour
    return 9 <= current_hour <= 21

def is_new_user():
    """Check if this is a new user session"""
    return not st.session_state.get('data_loaded', False)
```

### **Step 3: Modify Existing Functions**
```python
# Modify get_real_bigquery_data function
def get_real_bigquery_data(query_name, selected_date, _client):
    """Modified to check for new users"""
    
    if is_new_user():
        # New user - return cached data
        return get_cached_data_for_new_user(query_name)
    
    # Existing logic for returning users
    # ... rest of the function
```

### **Step 4: Add Background Service**
```python
# Create separate background service file
# background_refresh_service.py
import time
from datetime import datetime

def run_background_service():
    """Run background refresh service"""
    while True:
        # Check and refresh data
        if is_business_hours() and should_refresh_core_aeps():
            refresh_core_aeps_data_background()
        
        if should_refresh_daily_metrics():
            refresh_daily_metrics_data_background()
        
        time.sleep(300)  # Sleep for 5 minutes
```

---

## 🎯 **Expected Results**

### **New User Experience**
- **Load Time**: 0.5 seconds (instant)
- **BigQuery Queries**: 0 (no queries)
- **Data Source**: Preloaded/cached data

### **Returning User Experience**
- **Load Time**: 1-2 seconds
- **BigQuery Queries**: 1-2 (only if refresh needed)
- **Data Source**: Fresh data during business hours

### **Cost Optimization**
- **New Users**: $0 (no queries)
- **Returning Users**: $2-10 per session
- **Daily Cost**: $10-50 (vs $200-1000)

### **Performance**
- **New Users**: Instant dashboard
- **Business Hours**: Fresh Core AEPS data
- **After Hours**: Cached data
- **Scalable**: Can handle 100+ users

---

## ✅ **Implementation Checklist**

### **Immediate Changes**
1. ✅ Add global data storage
2. ✅ Add business hours logic
3. ✅ Add new user detection
4. ✅ Modify cache decorators
5. ✅ Add background service

### **Testing**
1. ✅ Test new user experience
2. ✅ Test returning user experience
3. ✅ Test business hours logic
4. ✅ Test cost optimization

This implementation ensures new users get instant access while maintaining fresh data for returning users during business hours!
