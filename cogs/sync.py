from typing import Literal, Optional
from discord.ext import commands
import discord

class Sync(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def sync(self, 
        ctx: commands.Context, 
        guilds: commands.Greedy[discord.Object],
        spec: Optional[Literal["~", "*", "^"]] = None
    ) -> None:
        """
        [p]sync
            Takes all global commands within the CommandTree and sends them to Discord.

        [p]sync ~
            Syncs all guild commands for the current context’s guild.

        [p]sync *
            Copies all global commands to the current guild (within the CommandTree) and syncs.

        [p]sync ^
            Removes all guild commands from the CommandTree and syncs, effectively removing all commands from the guild.

        [p]sync 123 456 789
            Syncs the 3 guild ids passed: 123, 456 and 789. Only their guilds and guild-bound commands.
        """
        
        if not guilds:
            match spec:
                case '~':
                    synced = await self.bot.tree.sync(guild = ctx.guild)

                case '*':
                    self.bot.tree.copy_global_to(guild = ctx.guild)
                    synced = await self.bot.tree.sync(guild = ctx.guild)

                case '^':
                    self.bot.tree.clear_commands(guild = ctx.guild)
                    await self.bot.tree.sync(guild = ctx.guild)
                    synced = []

                case _:
                    synced = await self.bot.tree.sync()

            await ctx.send(
                f'Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}'
            )
            return

        ret = 0
        for guild in guilds:
            try:
                await self.bot.tree.sync(guild = guild)

            except discord.HTTPException:
                pass
            
            else:
                ret += 1

        await ctx.send(f'Synced the tree to {ret}/{len(guilds)}.')

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Sync(bot))