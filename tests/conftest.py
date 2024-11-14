import pytest
from unittest.mock import patch
from app.config import settings
from app.init import redis_manager
from app.database import Base, engine_null_pool, async_session_maker_null_pool
from app.main import app
from app.models import *
from app.services.base import BaseService
from httpx import AsyncClient

data_url = 'tests/data/'
base_url = 'http://127.0.0.1:8000/'


@pytest.fixture(scope="session", autouse=True)
def test_check_mode():
    assert settings.MODE == "TEST"


@pytest.fixture(scope="session", autouse=True)
async def test_setup_database(test_check_mode):
    async with engine_null_pool.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
