import json
import aiofiles

from app.utils.db_manager import DBManager


class BaseService:
    db: DBManager | None

    def __init__(self, db: DBManager | None = None) -> None:
        self.db = db

    async def read_json_async(self, file_path):
        async with aiofiles.open(file_path, mode='r', encoding='utf-8') as f:
            contents = await f.read()
            return json.loads(contents)

    async def write_json_async(self, file_path, data):
        async with aiofiles.open(file_path, mode='w', encoding='utf-8') as f:
            await f.write(json.dumps(data, ensure_ascii=False, indent=4))
