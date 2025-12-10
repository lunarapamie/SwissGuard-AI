"""
SWISSGUARD AI - Day 1: Threat Data Collection
Author: [Your Name]
Date: [Today's Date]
"""

print("🇨🇭 SWISSGUARD AI - THREAT INTELLIGENCE PLATFORM")
print("=" * 60)

def fetch_cisa_threats():
    """Fetch real threat data from CISA"""
    import requests
    import pandas as pd
    
    print("📡 Connecting to CISA Known Exploited Vulnerabilities database...")
    
    url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        threats = data.get('vulnerabilities', [])[:10]
        
        print(f"✅ Successfully fetched {len(threats)} threats")
        
        # Display first 3 threats
        print("\n🔐 RECENT THREATS:")
        print("-" * 50)
        for i, threat in enumerate(threats[:3], 1):
            print(f"{i}. {threat.get('cveID', 'Unknown')}")
            print(f"   {threat.get('shortDescription', 'No description')[:80]}...")
            print(f"   Date: {threat.get('dateAdded', 'Unknown')}")
            print()
        
        # Save to CSV
        df = pd.DataFrame(threats)
        df.to_csv('threats.csv', index=False)
        print("💾 Data saved to 'threats.csv'")
        
        return threats
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Using sample data for demonstration...")
        return []

if __name__ == "__main__":
    fetch_cisa_threats()
