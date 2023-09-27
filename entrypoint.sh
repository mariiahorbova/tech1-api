#!/bin/sh

alembic revision --autogenerate -m "Initial migration" &&
alembic upgrade head
python main.py
