import pytest
from httpx import AsyncClient
from sqlalchemy import select

from app.main import app
from app.database import async_session_maker_null_pool
from tests.conftest import base_url


async def test_test_setup_database():
    # async with AsyncClient(app=app, base_url=base_url) as ac:
    #     await ac.post("/v1/suspicious_event/", params={})
    #     suspicious_event = await get_player("testplayer")
    #     assert suspicious_event
    pass