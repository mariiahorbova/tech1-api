import uvicorn
from fastapi import FastAPI

from database_tech.db_init import init_db
from app.routers import router


app = FastAPI()

app.include_router(router)


if __name__ == "__main__":
    init_db()
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
