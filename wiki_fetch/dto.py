from typing import List, Optional, Dict, Any, NewType
from datetime import datetime
from typing import Generic, List, NewType, Optional, TypeVar
from pydantic import BaseModel
from pydantic.generics import GenericModel

ArticleID = NewType("ArticleID", int)
PageID = NewType("PageID", int)
ResponseT = TypeVar("ResponseT")
JSON = Dict[str, Any]


class UnsavedArticle(BaseModel):
    page_id: PageID
    title: str
    article_extract: str
    thumbnail_image_url: Optional[Any]


class Article(UnsavedArticle):
    id: ArticleID
    page_id: PageID
    title: str
    article_extract: str
    thumbnail_image_url: str
    created_at: datetime
    updated_at: datetime


class ArticleFilter(BaseModel):
    page_id: PageID


class PagedResult(GenericModel, Generic[ResponseT]):
    results: List[ResponseT]
    total_count: Optional[int] = 0


class ErrorResponse(BaseModel):
    detail: str



class LinkResponse(BaseModel):
    href: str
    rel: str
    type: str


class StatusViewResponse(BaseModel):
    service: str
    version: str
    environment: str
    links: Optional[List[LinkResponse]]