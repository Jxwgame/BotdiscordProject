from asyncio import sleep
import discord
from discord.ext import commands
import random
import math
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()

intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix= '$', intents = intents)


#Function

@client.event
async def on_ready():
	print('Ready.')

def add(n: float, n2: float):
	return n + n2

def sub(n: float, n2: float):
	return n - n2

def rando(n: float, n2: float):
	return random.randfloat(n, n2)

def div(n: float, n2: float):
	return n / n2

def sqrt(n: float):
	return math.sqrt(n)

def mult(n: float, n2: float):
	return n * n2


#Command

@client.command()
async def mathadd(ctx, x: float, y: float):
	try:
		result = add(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathsub(ctx, x: float, y: float):
	try:
		result = sub(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathrando(ctx, x: float, y: float):
	try:
		result = rando(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathdiv(ctx, x: float, y: float):
	try:
		result = div(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathmult(ctx, x: float, y: float):
	try:
		result = mult(x, y)
		await ctx.send(result)

	except:
		pass

@client.command()
async def mathsqrt(ctx, x: float):
	try:
		result = sqrt(x)
		await ctx.send(result)

	except:
		pass

client.run('')
