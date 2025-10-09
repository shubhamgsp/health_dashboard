#!/usr/bin/env python3
"""
Test Google Sheets Access - Quick Verification Script
This script tests if all required Google Sheets are accessible with the current credentials.
"""

import os
import sys

def test_google_sheets_access():
    """Test access to all Google Sheets used by the dashboard"""
    
    print("🔍 Testing Google Sheets Access...")
    print("=" * 50)
    
    # Required Google Sheets with their purposes
    sheets = {
        "1HaW-pC5niZNm0_ii4zoXG-xR781dmDmbPjQf6W_b7Y8": "Anomaly Dashboard",
        "1XyTNR14JlkM_7uHEeoQa68mLgeiAZTaCq9vR-VCff4o": "Login Data", 
        "1DLU87T3DW9ruoR_U_jVCTV8hvuVCRSw8VMWLaN1PUBU": "Bugs Data",
        "1LMDeoOLzfMaLfuVown4If6ffI1agZlEzjTHzFgBuqRw": "Product Metrics (NEW)"
    }
    
    try:
        import pygsheets
        print("✅ pygsheets library is available")
    except ImportError:
        print("❌ pygsheets library not found. Install with: pip install pygsheets")
        return False
    
    try:
        # Try to get credentials (same logic as the main app)
        from google.oauth2 import service_account
        import tempfile
        import json
        
        # Check if running in Streamlit environment
        try:
            import streamlit as st
            if "gcp_service_account" in st.secrets:
                print("✅ Using Streamlit secrets for authentication")
                # Create temp file for pygsheets
                with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as temp_file:
                    json.dump(dict(st.secrets["gcp_service_account"]), temp_file)
                    credentials_path = temp_file.name
            else:
                print("❌ No Streamlit secrets found")
                return False
        except:
            # Not in Streamlit environment, try local file
            credentials_path = "spicemoney-dwh.json"
            if not os.path.exists(credentials_path):
                print("❌ No credentials file found locally")
                return False
            print("✅ Using local credentials file")
        
        # Test Google Sheets access
        gc = pygsheets.authorize(service_file=credentials_path)
        print("✅ Google Sheets authentication successful")
        
        # Test each sheet
        for sheet_id, purpose in sheets.items():
            try:
                url = f"https://docs.google.com/spreadsheets/d/{sheet_id}"
                sh = gc.open_by_url(url)
                print(f"✅ {purpose}: Accessible")
            except Exception as e:
                if "403" in str(e) or "permission" in str(e).lower():
                    print(f"❌ {purpose}: Permission denied - Sheet not shared with service account")
                    print(f"   Fix: Share {url} with: mrunalinee-patole@spicemoney-dwh.iam.gserviceaccount.com")
                else:
                    print(f"❌ {purpose}: Error - {str(e)}")
        
        # Clean up temp file if created
        if 'temp_file' in locals():
            try:
                os.unlink(credentials_path)
            except:
                pass
                
        return True
        
    except Exception as e:
        print(f"❌ Authentication failed: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Google Sheets Access Test")
    print("This script tests if all required Google Sheets are accessible.")
    print()
    
    success = test_google_sheets_access()
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 All tests completed!")
        print("Check the results above to see which sheets need to be shared.")
    else:
        print("❌ Test failed - check your credentials setup.")
    
    print("\n📋 Next Steps:")
    print("1. Share any sheets showing 'Permission denied' with the service account")
    print("2. Service account email: mrunalinee-patole@spicemoney-dwh.iam.gserviceaccount.com")
    print("3. Give 'Viewer' access to the service account")
    print("4. Wait 30 seconds, then refresh your Streamlit app")
