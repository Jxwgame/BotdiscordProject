import discord
from discord.ext import commands

intents = discord.Intents.default()

intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix= '$', intents = intents)


#Bot standby
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


#Send private message to new members

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


#Sever message responding

@client.event
async def on_message(message):
    if message.author == client.user: #Client check (prevent responding to itself)
        return
    if 'hello' in message.content.lower(): #respond to 'hello' in chat
        await message.add_reaction('\U0001F618')
        await message.channel.send(f'Good morning!, {message.author.display_name}')

    if 'goodbye' in message.content.lower(): #respond to 'goodbye' in chat
        await message.channel.send(f'See you later!, {message.author.display_name}')

    if 'happy birthday' in message.content.lower(): #respond to 'happy birthday' in chat
        await message.add_reaction('\U0001F973')
        await message.channel.send('Happy Birthday! 🎈🎉')

    if 'dolph' in message.content.lower(): #little easter egg
        await message.add_reaction('\U0001F42C')


client.run('put token here')
