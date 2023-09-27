#!/bin/sh

[ ! -d "alembic/versions" ] && mkdir alembic/versions
alembic revision --autogenerate -m "Initial migration" &&
alembic upgrade head
python main.py
