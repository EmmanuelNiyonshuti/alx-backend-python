"""
Run multiple database queries concurrently using asyncio.gather.
"""
import asyncio
import aiosqlite

DB = "users.db"


async def async_fetch_users():
    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT * FROM users") as cursor:
            users = await cursor.fetchall()
            return users


async def async_fetch_older_users():
    async with aiosqlite.connect(DB) as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            users = await cursor.fetchall()
            return users


async def fetch_concurrently():
    users, older_users = await asyncio.gather(
        async_fetch_users(), async_fetch_older_users()
    )
    print("All users:", users)
    print("Old Users:", older_users)


if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
