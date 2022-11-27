import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('You logged in ')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")
    
bot.run("MTA0NjMzODYxMjc5MjQwNjAxNg.G8f6yg.00p1pJES14OFNoGCJDTpVAdp69H6ZqEmLP5eiY")
