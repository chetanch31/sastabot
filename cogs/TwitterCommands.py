import discord
from discord.ext import commands

class TwitterCommands(commands.Cog):

    def __ini__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("TwitterCommands online")

    @commands.command()
    async def test(self, ctx):
        await ctx.send("Test Success")

async def setup(bot):
    await bot.add_cog(TwitterCommands(bot))
