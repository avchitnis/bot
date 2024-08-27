import google.generativeai as genai
from discord.ext import commands
import discord
import os

genai.configure(api_key = os.environ['GEMINI'])
model = genai.GenerativeModel('gemini-pro')

class Gemini(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        """
        Called when a message is created and sent.
        """

        if message.author == self.bot.user:
            return
        
        if self.bot.user.mentioned_in(message):
            try:
                async with message.channel.typing():
                    response = model.generate_content(message.content)
                    await message.reply(response.text)

            except discord.errors.HTTPException:
                await message.reply('Response exceeded the character limit of 2,000.')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Gemini(bot))