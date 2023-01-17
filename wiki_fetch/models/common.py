from typing import Any

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    Text,
    text,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import dto
from session import AsyncSessionLocal

Base = declarative_base()  # type: Any


async def get_db() -> AsyncSessionLocal:
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    page_id = Column(Integer, nullable=False)
    title = Column(Text, nullable=False)
    article_extract = Column(Text)
    thumbnail_image_url = Column(Text)
    created_at = Column(
        DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    updated_at = Column(
        DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP")
    )
    deleted_at = Column(DateTime(timezone=True))


def result_to_article(result: Article) -> dto.Article:
    return dto.Article(
        id=dto.ArticleID(result.id),
        page_id=dto.PageID(result.page_id),
        title=result.title,
        article_extract=result.article_extract,
        thumbnail_image_url=result.thumbnail_image_url,
        created_at=result.created_at,
        updated_at=result.updated_at
    )