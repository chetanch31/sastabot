from dotenv import load_dotenv
import os
import asyncio
import discord
from discord.ext import commands

load_dotenv()
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True
intents.guilds = True

prefix = ";"
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.listen('on_message')
async def bot_mentioned(message):
    if bot.user.mentioned_in(message):
        await message.channel.send(f"You can type `{prefix}help` for more info")
    await bot.process_commands(message)  

@bot.event 
async def on_command_error(ctx, error): 
    if isinstance(error, commands.CommandNotFound): 
        em = discord.Embed()
        em.title = "Command not found"
        em.description = f"The command you are looking for is not found. Use **{prefix}help** to get a list of all available commands."
        em.color = ctx.author.color
        await ctx.send(embed=em)

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load_cogs()
    await bot.start(token)

asyncio.run(main=main())