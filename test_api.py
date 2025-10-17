#!/usr/bin/env python
"""
Test script to verify the /me endpoint
Run: python test_api.py
"""
import requests
import json
from datetime import datetime

def test_endpoint(url="http://localhost:8000/me"):
    print(f" Testing: {url}\n")
    try:
        response = requests.get(url, timeout=10)
        print(f"✅ Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("\n📦 Response:")
            print(json.dumps(data, indent=2))
            
            # Validate structure
            assert 'status' in data
            assert 'user' in data
            assert 'timestamp' in data
            assert 'fact' in data
            print("\n✨ All checks passed!")
            return True
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Connection failed. Is the server running?")
        print(" Start with: python manage.py runserver")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("=" * 50)
    print("Backend Wizards Stage 0 - API Test")
    print("=" * 50 + "\n")
    test_endpoint()