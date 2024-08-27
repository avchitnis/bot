from discord.ext import commands
from dotenv import load_dotenv
import aiosqlite
import discord
import logging
import asyncio
import os

class MyBot(commands.Bot):
    def __init__(self, command_prefix: str, intents: discord.Intents, **kwargs):
        super().__init__(command_prefix, intents = intents, **kwargs)

    async def setup_hook(self) -> None:
        """
        A coroutine to be called to setup the bot, by default this is blank.
        """
        
        self.connection = await aiosqlite.connect('users.db')
        cursor = await self.connection.cursor()
        await self.connection.commit()
        await self.connection.close()

        loaded_cogs: list[str] = []
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                loaded_cogs.append(filename[:-3])

            else:
                print('Unable to load pycache folder.')

        print(f'Loaded cogs: {', '.join(loaded_cogs)}' )

intents = discord.Intents.all()
bot = MyBot(
    command_prefix = '>',
    intents = intents,
    owner_id = 811527737881002024
)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename = 'bot.log',
    encoding = 'utf-8',
    mode = 'w'
)
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
))
logger.addHandler(handler)

async def main() -> None:
    async with bot:
        await bot.start(os.environ['TOKEN'])

if __name__ == '__main__':
    load_dotenv()
    asyncio.run(main())