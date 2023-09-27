from pydantic import BaseModel
from app.models import ColorEnum


class UserBase(BaseModel):
    name: str
    age: int


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class ConfigDict:
        from_attributes = True


class ArticleBase(BaseModel):
    text: str
    color: ColorEnum
    author_id: int


class ArticleCreate(ArticleBase):
    pass


class Article(ArticleBase):
    id: int
    author: User

    class ConfigDict:
        from_attributes = True
