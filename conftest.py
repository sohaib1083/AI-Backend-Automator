import pytest
from app import create_app  # Import create_app, not app directly

@pytest.fixture
def client():
    app = create_app()  # This will create a new Flask app instance
    with app.test_client() as client:
        yield client  # Return the test client for use in the tests
