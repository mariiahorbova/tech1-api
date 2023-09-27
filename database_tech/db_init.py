from random import randint, choice

from database_tech.database import Base, engine, SessionLocal
from app.models import User, Article, ColorEnum


def init_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        for i in range(5, 11):
            user = User(name=f"User Name {i-4}", age=randint(5, 80))
            db.add(user)
            db.commit()

            for j in range(randint(1, 5)):
                article = Article(
                    text=f"Article Text {j}",
                    color=choice(list(ColorEnum))
                )
                user.articles.append(article)
                db.add(article)
                db.commit()
    finally:
        db.close()
