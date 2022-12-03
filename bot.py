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
    
bot.run("MTA0NjMzODYxMjc5MjQwNjAxNg.G2d3_G.gead5YgK6u8CJB7xLihigog310K4POgLsqN5tg")
### Reset Token ของ Bot ต้องทักมาเอาส่วนตัว ###
