from wikipedia_service import WikipediaService
from web_service import WebService
from time_service import TimeKeeper
from models import article_model as AM
import dto
from models.common import get_db
import asyncio
from session import AsyncSessionLocal
import re

class AddArticle:

    def __init__(self, wikipedia_obj, article_model_obj):
        self.wikipedia_articles = wikipedia_obj
        self.articles_table = article_model_obj

    async def add_articles(self):
        it = get_db()
        db_session = await it.__anext__()
        for article in self.wikipedia_articles(TimeKeeper(), WebService()).get_articles():

            if self.filter_article(article):
                await self.process_articles(article, db_session)
        
        await db_session.commit()

    
    async def process_articles(self, article, db_session):
        await self.articles_table.create_article(
            db_session=db_session, 
            unsaved_article=dto.UnsavedArticle(
                page_id=dto.PageID(article['id']),
                title=article['title'],
                article_extract=article['excerpt'],
                thumbnail_image_url=article['thumbnail']['url'] if article['thumbnail'] else ""
            )
        )
    
    def filter_article(self, article):
        if 'war' in article['excerpt'] or 'military' in article['excerpt']:
            return None
        else:
            return article



if __name__ == '__main__':
    asyncio.run(AddArticle(WikipediaService, AM).add_articles())
