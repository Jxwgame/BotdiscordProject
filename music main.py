import discord
from discord.ext import commands
import os

#import all of the cogs
from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.default()

intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix= '$', intents = intents)


#remove the default help command so that we can write out own
client.remove_command('help')

#register the class with the bot
client.add_cog(help_cog(client))
client.add_cog(music_cog(client))

#start the bot with our token
client.run('MTA0ODUxMjEzNTc3ODUzMzQ2Ng.G1zRGb.-6kXVkIbFp1kk7WmbRFpOs1XQ8XlrFwwbUVJYk')
