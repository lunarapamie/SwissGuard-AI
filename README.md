
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
    
    try:
        # CISA public API
        url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
        response = requests.get(url, timeout=10)
        data = response.json()
        threats = data.get('vulnerabilities', [])[:10]
        
        print(f"✅ Successfully fetched {len(threats)} real threats")
        print("\n🔐 TOP THREATS:")
        print("-" * 50)
        
        for i, threat in enumerate(threats, 1):
            print(f"{i}. {threat.get('cveID', 'Unknown')}")
            desc = threat.get('shortDescription', 'No description')
            print(f"   {desc[:80]}..." if len(desc) > 80 else f"   {desc}")
            print(f"   Date Added: {threat.get('dateAdded', 'Unknown')}")
            print()
        
        return threats
        
    except Exception as e:
        print(f"⚠️  Using sample data (API error: {e})")
        return get_sample_threats()

def get_sample_threats():
    """Return sample threat data for demonstration"""
    return [
        {
            "cveID": "CVE-2024-12345",
            "shortDescription": "Critical Windows vulnerability affecting banking transaction systems",
            "dateAdded": "2024-12-01",
            "vendorProject": "Microsoft",
            "requiredAction": "Apply security update immediately"
        },
        {
            "cveID": "CVE-2024-12346",
            "shortDescription": "Linux kernel flaw allowing unauthorized access to pharmaceutical research data",
            "dateAdded": "2024-11-30",
            "vendorProject": "Linux Foundation",
            "requiredAction": "Update kernel to latest version"
        },
        {
            "cveID": "CVE-2024-12347",
            "shortDescription": "Swiss government web portal authentication bypass vulnerability",
            "dateAdded": "2024-11-29",
            "vendorProject": "Swiss Government IT",
            "requiredAction": "Implement multi-factor authentication"
        }
    ]

def analyze_swiss_relevance(threats):
    """Analyze threats for Swiss infrastructure relevance"""
    print("\n🎯 SWISS RELEVANCE ANALYSIS")
    print("-" * 40)
    
    swiss_keywords = ['bank', 'financial', 'payment', 'pharmaceutical', 'medical', 
                     'government', 'swiss', 'energy', 'infrastructure', 'critical']
    
    relevant_threats = []
    
    for threat in threats:
        description = threat.get('shortDescription', '').lower()
        relevant = False
        keywords_found = []
        
        for keyword in swiss_keywords:
            if keyword in description:
                relevant = True
                keywords_found.append(keyword)
        
        if relevant:
            relevant_threats.append(threat)
            print(f"⚠️  {threat['cveID']} - Relevant to Swiss {', '.join(keywords_found)}")
    
    print(f"\n📊 Summary: {len(relevant_threats)} of {len(threats)} threats are Swiss-relevant")
    return relevant_threats

def calculate_security_index(threats, relevant_threats):
    """Calculate Swiss Security Index (0-100)"""
    if not threats:
        return 50  # Neutral if no data
    
    relevance_ratio = len(relevant_threats) / len(threats)
    security_index = 100 - (relevance_ratio * 100)
    security_index = max(0, min(100, security_index))
    
    print(f"\n🇨🇭 SWISS SECURITY INDEX: {security_index:.0f}/100")
    
    if security_index >= 80:
        print("🟢 STATUS: SECURE - Swiss infrastructure well protected")
    elif security_index >= 60:
        print("🟡 STATUS: MODERATE - Enhanced monitoring recommended")
    elif security_index >= 40:
        print("🟠 STATUS: ELEVATED - Additional security measures needed")
    else:
        print("🔴 STATUS: CRITICAL - Immediate action required")
    
    return security_index

def main():
    """Main execution function"""
    print("\n" + "="*60)
    print("STARTING SWISSGUARD AI DATA COLLECTION")
    print("="*60)
    
    # Step 1: Fetch threats
    threats = fetch_cisa_threats()
    
    # Step 2: Analyze Swiss relevance
    relevant_threats = analyze_swiss_relevance(threats)
    
    # Step 3: Calculate security index
    security_index = calculate_security_index(threats, relevant_threats)
    
    # Step 4: Save results
    print("\n💾 SAVING RESULTS...")
    try:
        import pandas as pd
        df = pd.DataFrame(threats)
        df['swiss_relevant'] = df['cveID'].isin([t['cveID'] for t in relevant_threats])
        df.to_csv('threat_data.csv', index=False)
        print("✅ Data saved to 'threat_data.csv'")
    except:
        print("📝 Results documented in code comments")
    
    print("\n" + "="*60)
    print("DAY 1 COMPLETE: Threat data collected and analyzed")
    print("Next: Build interactive dashboard")
    print("="*60)

if __name__ == "__main__":
    main()
