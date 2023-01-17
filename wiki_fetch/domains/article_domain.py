from typing import List

import dto
from session import AsyncSessionLocal
from models import article_model


async def get_articles(
    db_session: AsyncSessionLocal
) -> dto.PagedResult[dto.Article]:
    return await article_model.get_articles(db_session)


async def get_article(
    db_session: AsyncSessionLocal,
    article_filter: dto.ArticleFilter
) -> dto.Article:
    return await article_model.get_article(db_session, article_filter)