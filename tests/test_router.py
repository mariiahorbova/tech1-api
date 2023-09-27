from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_token_for_signin():
    response = client.post("/users/signin")
    assert response.status_code == 200


def test_get_users_by_age():
    token = client.post("/users/signin").json()["access"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/30", headers=headers)
    assert response.status_code == 200


def test_get_users_by_article_color():
    token = client.post("/users/signin").json()["access"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users/articles/red", headers=headers)
    assert response.status_code == 200


def test_get_unique_names_with_more_than_3_articles():
    token = client.post("/users/signin").json()["access"]
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/users-qt-3-articles", headers=headers)
    assert response.status_code == 200


def test_create_user():
    token = client.post("/users/signin").json()["access"]
    headers = {"Authorization": f"Bearer {token}"}
    user_data = {"name": "TestUser", "age": 25}
    response = client.post("/users", headers=headers, json=user_data)
    assert response.status_code == 200


def test_create_article():
    token = client.post("/users/signin").json()["access"]
    headers = {"Authorization": f"Bearer {token}"}
    article_data = {"text": "Test Article", "color": "green", "author_id": 1}
    response = client.post("/articles", headers=headers, json=article_data)
    assert response.status_code == 200
