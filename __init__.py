"""
Web Scraper for Tech Skills Checker
Ye file job sites se skills extract karti hai
"""

import requests
from bs4 import BeautifulSoup
import time
import re
from typing import List, Dict, Set

class SkillScraper:
    """
    Main scraper class jo different job sites se skills extract karta hai
    """
    
    def __init__(self):
        """Initialize scraper with headers"""
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        # Common tech skills list (backup ke liye)
        self.common_skills = {
            'Python', 'JavaScript', 'Java', 'C++', 'C#', 'PHP', 'Ruby', 'Go', 'Swift', 'Kotlin',
            'React', 'Angular', 'Vue.js', 'Node.js', 'Django', 'Flask', 'Spring', 'Express',
            'HTML', 'CSS', 'SQL', 'MongoDB', 'PostgreSQL', 'MySQL', 'Redis', 'Docker',
            'Kubernetes', 'AWS', 'Azure', 'GCP', 'Git', 'Linux', 'REST API', 'GraphQL',
            'Machine Learning', 'AI', 'Data Science', 'DevOps', 'Agile', 'Scrum'
        }
    
    def extract_skills_from_text(self, text: str) -> Set[str]:
        """
        Text se skills extract karta hai
        
        Args:
            text: Job description ya any text
            
        Returns:
            Set of skills found
        """
        found_skills = set()
        text_lower = text.lower()
        
        # Common skills check karo
        for skill in self.common_skills:
            # Case-insensitive match
            if skill.lower() in text_lower:
                found_skills.add(skill)
        
        return found_skills
    
    def scrape_indeed(self, job_title: str, location: str = "India") -> Dict:
        """
        Indeed se job skills scrape karta hai
        
        Args:
            job_title: Job title to search
            location: Location to search
            
        Returns:
            Dictionary with skills and job count
        """
        try:
            # Indeed URL
            url = f"https://in.indeed.com/jobs?q={job_title.replace(' ', '+')}&l={location.replace(' ', '+')}"
            
            print(f"🔍 Scraping Indeed for: {job_title}")
            
            # Request bhejo
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                print(f"❌ Indeed request failed: {response.status_code}")
                return self._get_fallback_data(job_title)
            
            # Parse HTML
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Job descriptions find karo
            job_cards = soup.find_all('div', class_='job_seen_beacon')
            
            all_skills = set()
            job_count = 0
            
            # Har job card se skills extract karo
            for card in job_cards[:10]:  # First 10 jobs check karo
                job_text = card.get_text()
                skills = self.extract_skills_from_text(job_text)
                all_skills.update(skills)
                job_count += 1
            
            print(f"✅ Found {len(all_skills)} skills from {job_count} jobs")
            
            return {
                'skills': list(all_skills),
                'job_count': job_count,
                'source': 'Indeed'
            }
            
        except Exception as e:
            print(f"❌ Indeed scraping error: {str(e)}")
            return self._get_fallback_data(job_title)
    
    def scrape_linkedin(self, job_title: str) -> Dict:
        """
        LinkedIn se job skills scrape karta hai
        
        Note: LinkedIn scraping difficult hai (login required)
        Isliye ye fallback data use karega
        
        Args:
            job_title: Job title to search
            
        Returns:
            Dictionary with skills
        """
        print(f"🔍 Analyzing LinkedIn trends for: {job_title}")
        
        # LinkedIn direct scraping mushkil hai
        # Isliye common patterns use karenge
        return self._get_fallback_data(job_title)
    
    def scrape_naukri(self, job_title: str) -> Dict:
        """
        Naukri.com se job skills scrape karta hai
        
        Args:
            job_title: Job title to search
            
        Returns:
            Dictionary with skills
        """
        try:
            # Naukri URL
            search_term = job_title.replace(' ', '-').lower()
            url = f"https://www.naukri.com/{search_term}-jobs"
            
            print(f"🔍 Scraping Naukri for: {job_title}")
            
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                print(f"❌ Naukri request failed: {response.status_code}")
                return self._get_fallback_data(job_title)
            
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Job listings find karo
            job_listings = soup.find_all('article', class_='jobTuple')
            
            all_skills = set()
            job_count = 0
            
            for listing in job_listings[:10]:
                job_text = listing.get_text()
                skills = self.extract_skills_from_text(job_text)
                all_skills.update(skills)
                job_count += 1
            
            print(f"✅ Found {len(all_skills)} skills from {job_count} jobs")
            
            return {
                'skills': list(all_skills),
                'job_count': job_count,
                'source': 'Naukri'
            }
            
        except Exception as e:
            print(f"❌ Naukri scraping error: {str(e)}")
            return self._get_fallback_data(job_title)
    
    def _get_fallback_data(self, job_title: str) -> Dict:
        """
        Agar scraping fail ho jaye to fallback data return karta hai
        
        Args:
            job_title: Job title
            
        Returns:
            Dictionary with common skills for that role
        """
        print(f"ℹ️  Using fallback data for: {job_title}")
        
        # Role-based common skills
        role_skills = {
            'python developer': ['Python', 'Django', 'Flask', 'SQL', 'REST API', 'Git'],
            'web developer': ['HTML', 'CSS', 'JavaScript', 'React', 'Node.js', 'Git'],
            'data scientist': ['Python', 'Machine Learning', 'SQL', 'Pandas', 'TensorFlow'],
            'java developer': ['Java', 'Spring', 'SQL', 'REST API', 'Maven', 'Git'],
            'devops engineer': ['Docker', 'Kubernetes', 'AWS', 'Linux', 'Git', 'CI/CD'],
            'frontend developer': ['HTML', 'CSS', 'JavaScript', 'React', 'Vue.js', 'Git'],
            'backend developer': ['Python', 'Node.js', 'SQL', 'REST API', 'MongoDB', 'Git']
        }
        
        # Job title ko lowercase mein convert karo
        job_lower = job_title.lower()
        
        # Match karo
        for role, skills in role_skills.items():
            if role in job_lower:
                return {
                    'skills': skills,
                    'job_count': 0,
                    'source': 'Fallback Data'
                }
        
        # Default skills
        return {
            'skills': ['Python', 'JavaScript', 'SQL', 'Git', 'HTML', 'CSS'],
            'job_count': 0,
            'source': 'Fallback Data'
        }
    
    def scrape_all_sources(self, job_title: str) -> Dict:
        """
        Saare sources se data scrape karta hai aur combine karta hai
        
        Args:
            job_title: Job title to search
            
        Returns:
            Combined dictionary with all skills
        """
        print(f"\n{'='*50}")
        print(f"🚀 Starting scraping for: {job_title}")
        print(f"{'='*50}\n")
        
        all_skills = set()
        total_jobs = 0
        sources_used = []
        
        # Indeed scrape karo
        indeed_data = self.scrape_indeed(job_title)
        all_skills.update(indeed_data['skills'])
        total_jobs += indeed_data['job_count']
        sources_used.append(indeed_data['source'])
        
        time.sleep(2)  # Rate limiting
        
        # Naukri scrape karo
        naukri_data = self.scrape_naukri(job_title)
        all_skills.update(naukri_data['skills'])
        total_jobs += naukri_data['job_count']
        sources_used.append(naukri_data['source'])
        
        time.sleep(2)  # Rate limiting
        
        # LinkedIn (fallback)
        linkedin_data = self.scrape_linkedin(job_title)
        all_skills.update(linkedin_data['skills'])
        sources_used.append(linkedin_data['source'])
        
        print(f"\n{'='*50}")
        print(f"✅ Scraping Complete!")
        print(f"📊 Total skills found: {len(all_skills)}")
        print(f"📝 Total jobs analyzed: {total_jobs}")
        print(f"🌐 Sources used: {', '.join(set(sources_used))}")
        print(f"{'='*50}\n")
        
        return {
            'skills': sorted(list(all_skills)),
            'job_count': total_jobs,
            'sources': list(set(sources_used))
        }


# Helper function
def scrape_job_skills(job_title: str) -> Dict:
    """
    Main function to scrape job skills
    
    Args:
        job_title: Job title to search
        
    Returns:
        Dictionary with skills data
    """
    scraper = SkillScraper()
    return scraper.scrape_all_sources(job_title)