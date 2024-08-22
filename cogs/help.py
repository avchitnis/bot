from discord.ext import commands

class HelpCommand(commands.DefaultHelpCommand):
    """
    The base implementation for help command formatting.
    """

class Help(commands.Cog):
    """
    Sets bot.help_command to the subclassed HelpCommand.
    """

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

        help_command = HelpCommand()
        help_command.cog = self
        bot.help_command = help_command

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Help(bot))