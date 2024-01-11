import os
import discord

from discord.ext import commands

from keep_alive import keep_alive

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')


@bot.command()
async def hello(ctx):
  await ctx.send('Hello there!')


keep_alive()
bot.run(os.getenv("token"))
