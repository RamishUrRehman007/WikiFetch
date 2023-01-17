
from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session

import dto
from domains import article_domain
from models.common import get_db

router = APIRouter()


@router.get(
    "/articles",
    response_model=dto.PagedResult[dto.Article],
    tags=["articles"],
)
async def get_articles(
    db_session: Session = Depends(get_db),
) -> dto.PagedResult[dto.Article]:
    """
    List view for getting Articles.
    \f
    :return:
    """
    return await article_domain.get_articles(db_session)


@router.get(
    "/articles/{page_id}",
    response_model=dto.Article,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "model": dto.ErrorResponse,
            "description": "Article not found.",
        },
    },
    tags=["articles"],
)
async def get_article(
    page_id: dto.PageID = Path(
        ..., title="Page ID", description="The Page ID of the Article to get."
    ),
    db_session: Session = Depends(get_db),
) -> dto.Article:
    """
    Getting Article by Page ID.

    \f
    :return:
    """
    article_filter = dto.ArticleFilter(page_id=dto.PageID(page_id))

    article = await article_domain.get_article(db_session, article_filter)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Article not found.")

    return article