"""Test configuration for Networking Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "networking-agent", "category": "Cloud Engineering"}
