import discord
from discord.ext import commands

intents = discord.Intents.default()

intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix= '$', intents = intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

#Send private message to new members
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

#Responding to the message
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'hello' in message.content.lower():
        await message.channel.send(f'Good morning!, {message.author.display_name}')

#Blocking word
block_words = ['peepee', 'poopoo', 'sex', 'obama']

@client.event
async def on_message(message):
    if message.author is client.user:
        for text in block_words:
            if text in str(message.content.lower()):
                await message.delete()
                return

#@client.command()
#async def embed(ctx):
#    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0x0b1442)
#    await ctx.send(embed=embed)

@client.command() ### คำสั่ง Help จะแสดง Function ของตัวบอทที่เพิ่มเข้ามา
async def helpme(ctx):
    emBed=discord.Embed(title="Toturial Bot help", description="All available bot commands", color=0x080c30)
    emBed.add_field(name="help", value="Get help command", inline=False)
    emBed.add_field(name="test", value="Respond messasge that you've send", inline=False)
    emBed.add_field(name="send", value="Send hello message to user", inline=False)
    emBed.set_thumbnail(url="https://media.discordapp.net/attachments/964949321789362177/1048291659907092510/image.png?width=818&height=456")
    await ctx.send(embed=emBed)

client.run('')
