from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as EnumField, ForeignKey
from sqlalchemy.orm import relationship
from database_tech.database import Base


class ColorEnum(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)

    articles = relationship("Article", back_populates="author")


class Article(Base):
    __tablename__ = "articles"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String)
    color = Column(EnumField(ColorEnum))

    author_id = Column(Integer, ForeignKey("users.id"))
    author = relationship("User", back_populates="articles")
