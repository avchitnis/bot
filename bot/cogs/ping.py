from discord.ext import commands
import datetime
import discord

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @discord.app_commands.command()
    async def ping(self, interaction: discord.Interaction) -> None:
        """
        Responds with the bot's latency.
        """

        latency = round(self.bot.latency * 1000)

        embed = discord.Embed(
            title = f'🏓 Pong!',
            description = f'The bot\'s latency is `{latency}`ms',
            timestamp = datetime.datetime.now(datetime.UTC)
        )

        if  latency <= 50:
            embed.colour = 0x44ff44

        elif latency <= 100:
            embed.color = 0xffd000

        elif latency <= 200:
            embed.color = 0xff6600

        else:
            embed.color = 0x990000

        await interaction.response.send_message(embed = embed)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Ping(bot))