import json

from unittest.mock import patch, call

from worker import create_task

def test_index(test_app):
    response = test_app.get("/")
    assert response.status_code == 200
