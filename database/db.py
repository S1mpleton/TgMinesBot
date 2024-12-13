import aiosqlite


class DB():

    async def on_startup(self):
        self.con = await aiosqlite.connect("database/user.db")

        await self.con.execute(
            "CREATE TABLE IF NOT EXISTS users(verifed TEXT, user_id BIGINT PRIMARY KEY)")

    async def register(self, user_id, verifed="verifed"):
        try:
            query = "INSERT INTO users(verifed, user_id) VALUES(?,?)"

            await self.con.execute(query, (verifed, user_id))
            await self.con.commit()
        except aiosqlite.IntegrityError:
            pass

    async def update_verifed(self, user_id, verifed="verifed"):
        query = "UPDATE users SET verifed = ? WHERE user_id = ?"
        await self.con.execute(query, (verifed, user_id))
        await self.con.commit()

    async def update_language(self, user_id, language=0):
        query = "UPDATE users SET language = ? WHERE user_id = ?"
        await self.con.execute(query, (language, user_id))
        await self.con.commit()

    async def get_language(self, user_id):
        query = f'SELECT language FROM users WHERE user_id = {user_id}'
        result = await self.con.execute(query)
        return await result.fetchone()

    async def get_user(self, user_id):
        ver = "verifed"
        query = 'SELECT * FROM users WHERE user_id = ? AND verifed = ?'

        result = await self.con.execute(query, (user_id, ver))
        return await result.fetchone()
    
    async def get_users(self):
        query = "SELECT * FROM users"

        result = await self.con.execute(query)
        return await result.fetchall()


DataBase = DB()
