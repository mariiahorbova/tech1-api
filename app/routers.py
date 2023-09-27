from fastapi import APIRouter, Depends
from sqlalchemy import func
from sqlalchemy.orm import Session

from app import schemas
from database_tech.database import get_db
from app.models import User, ColorEnum, Article
from app.auth_token.token_handler import create_jwt
from app.auth_token.token_bearer import JWTBearer

router = APIRouter()


@router.post("/users/signin")
def create_token_for_signin():
    return create_jwt()


@router.get("/users/{age}", dependencies=[Depends(JWTBearer())])
def get_users_by_age(age: int, db: Session = Depends(get_db)):
    users = db.query(User).filter(User.age > age).all()
    return users


@router.get("/users/articles/{color}", dependencies=[Depends(JWTBearer())])
def get_users_by_article_color(
    color: ColorEnum,
    db: Session = Depends(get_db)
):
    users = db.query(User).join(Article).filter(Article.color == color).all()
    return users


@router.get("/users-qt-3-articles", dependencies=[Depends(JWTBearer())])
def get_unique_names_with_more_than_3_articles(db: Session = Depends(get_db)):
    users = db.query(User.id).join(Article).group_by(User.id).having(
        func.count(Article.id) > 3)

    distinct_users = db.query(User.name).filter(
        User.id.in_(users)).distinct().all()

    return [name[0] for name in distinct_users]


@router.post("/users", dependencies=[Depends(JWTBearer())])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        name=user.name,
        age=user.age
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.post("/articles", dependencies=[Depends(JWTBearer())])
def create_article(
    article: schemas.ArticleCreate,
    db: Session = Depends(get_db)
):
    new_article = Article(
        text=article.text,
        color=article.color,
        author_id=article.author_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
