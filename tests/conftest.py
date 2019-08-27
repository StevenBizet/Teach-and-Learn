import pytest
import sys

sys.path.append('.')
from __init__ import create_app # <<==== A CHANGER

@pytest.fixture
def app():
    app = create_app()  # <<=== A CHANGER
    return app

@pytest.fixture
def client():
    app = create_app()      # <<=== A CHANGER
    client = app.test_client()
    yield client
