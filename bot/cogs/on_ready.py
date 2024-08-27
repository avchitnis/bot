from discord.ext import commands

class Ready(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """
        Called when the client is done preparing the data received from Discord.
        """

        print(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')
        print('------')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ready(bot))