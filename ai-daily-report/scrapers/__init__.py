"""
爬虫模块
"""
from .government import GovernmentScraper
from .company import CompanyScraper
from .news import NewsScraper
from .wechat import WechatScraper
from .global_research import GlobalResearchScraper, ResearchReport
from .aihot import AIHOTScraper, fetch_aihot_data

__all__ = [
    'GovernmentScraper',
    'CompanyScraper', 
    'NewsScraper',
    'WechatScraper',
    'GlobalResearchScraper',
    'ResearchReport',
    'AIHOTScraper',
    'fetch_aihot_data'
]