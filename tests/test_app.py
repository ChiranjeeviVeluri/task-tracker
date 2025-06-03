import pytest


from app import app, tasks


@pytest.fixture(autouse=True)
def clear_tasks():
    """Reset the in-memory task list before each test."""
    tasks.clear()


def test_list_tasks_empty():
    client = app.test_client()
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert resp.json == []


def test_add_and_list_tasks():
    client = app.test_client()

    # Add a new task
    resp1 = client.post("/tasks", json={"title": "Buy groceries"})
    assert resp1.status_code == 201
    assert resp1.json["title"] == "Buy groceries"
    assert resp1.json["id"] == 1

    # Now GET /tasks should return a list with that single task
    resp2 = client.get("/tasks")
    assert resp2.status_code == 200
    tasks_list = resp2.json
    assert isinstance(tasks_list, list)
    assert len(tasks_list) == 1
    assert tasks_list[0]["title"] == "Buy groceries"
    assert tasks_list[0]["id"] == 1


def test_add_task_without_title():
    client = app.test_client()
    resp = client.post("/tasks", json={})
    assert resp.status_code == 400
    assert "error" in resp.json
