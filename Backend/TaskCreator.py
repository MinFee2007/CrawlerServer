from Backend.Crawler.PortalCrawler import PortalCrawler
from Backend.Crawler.MoodleCrawler import MoodleCrawler


class TaskCreator():
    def __init__(self):
        self.MoodleCrawler = MoodleCrawler()
        self.PortalCrawler = PortalCrawler()
    
    def crawl_raw_text(self):
        """Start the crawling process"""
        raw_tasks = {"Portal": [], "Moodle": []}
        
        # Crawl Portal data
        try: raw_tasks["Portal"] = self.PortalCrawler.fetch_data()
        except Exception as e: print(f"An error occurred while crawling Portal data: {e}")
        
        # Crawl Moodle data
        try: raw_tasks["Moodle"] = self.MoodleCrawler.fetch_data()
        except Exception as e: print(f"An error occurred while crawling Moodle data: {e}")
        
        return raw_tasks
    
    def create_task(self):
        """Create structured data from website data"""
        raw_tasks = self.crawl_raw_text()
        print(raw_tasks)