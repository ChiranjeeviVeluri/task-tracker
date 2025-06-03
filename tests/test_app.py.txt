import pytest
from app import app, tasks

@pytest.fixture(autouse=True)
def clear_tasks():
    # Reset the in-memory list before each test
    tasks.clear()

def test_list_tasks_empty():
    client = app.test_client()
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert resp.json == []

def test_add_and_list_tasks():
    client = app.test_client()
    # POST a new task
    resp1 = client.post("/tasks", json={"title": "Buy groceries"})
    assert resp1.status_code == 201
    assert resp1.json["title"] == "Buy groceries"
    assert resp1.json["id"] == 1

    # Now GET /tasks should return a list with that one task
    resp2 = client.get("/tasks")
    assert resp2.status_code == 200
    assert isinstance(resp2.json, list)
    assert len(resp2.json) == 1
    assert resp2.json[0]["title"] == "Buy groceries"
    assert resp2.json[0]["id"] == 1

def test_add_task_without_title():
    client = app.test_client()
    resp = client.post("/tasks", json={})
    assert resp.status_code == 400
    assert "error" in resp.json
