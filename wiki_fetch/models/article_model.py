from sqlalchemy import select

import dto
from models.common import Article, result_to_article
from session import AsyncSessionLocal


async def get_articles(
    db_session: AsyncSessionLocal
) -> dto.PagedResult[dto.Article]:
    query = select(Article).order_by(Article.id.desc())
    results = await db_session.execute(query)
    return dto.PagedResult(
        results=[result_to_article(result[0]) for result in results]
    )


async def get_article(
    db_session: AsyncSessionLocal,
    article_filter: dto.ArticleFilter
) -> dto.Article:
    query = select(Article).order_by(Article.id.desc())
    query = query.where(Article.page_id == article_filter.page_id)
    result = await db_session.execute(query)

    rows = result.first()
    if rows is None:
        return None

    return result_to_article(rows[0])


async def create_article(db_session: AsyncSessionLocal, unsaved_article: dto.UnsavedArticle):
    article = Article(**unsaved_article.dict())
    db_session.add(article)
    await db_session.flush()
