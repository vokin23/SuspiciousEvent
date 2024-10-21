import redis.asyncio as redis


class RedisManager:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.redis = None

    async def redis_connect(self):
        self.redis = await redis.Redis(host=self.host, port=self.port)

    async def redis_set(self, key: str, value: str, expire: int = None):
        if expire:
            await self.redis.set(key, value, ex=expire)
        else:
            await self.redis.set(key, value)

    async def redis_get(self, key: str):
        return await self.redis.get(key)

    async def redis_delete(self, key: str):
        await self.redis.delete(key)

    async def redis_close(self):
        if self.redis:
            await self.redis.close()
