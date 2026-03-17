"""
Scraper Test Script
Ye script scraper ko test karta hai
"""

from scraper import scrape_job_skills

def test_scraper():
    """Test the scraper with a sample job title"""
    
    print("🧪 Testing Web Scraper...")
    print("="*60)
    
    # Test job titles
    test_jobs = [
        "Python Developer",
        "Web Developer",
        "Data Scientist"
    ]
    
    for job in test_jobs:
        print(f"\n🔍 Testing: {job}")
        print("-"*60)
        
        result = scrape_job_skills(job)
        
        print(f"\n📊 Results:")
        print(f"   Skills found: {len(result['skills'])}")
        print(f"   Jobs analyzed: {result['job_count']}")
        print(f"   Sources: {', '.join(result['sources'])}")
        print(f"\n💡 Top Skills:")
        for skill in result['skills'][:10]:
            print(f"   • {skill}")
        
        print("\n" + "="*60)

if __name__ == "__main__":
    test_scraper()