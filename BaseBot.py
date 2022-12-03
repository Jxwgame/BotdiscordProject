import discord
from discord.ext import commands

intents = discord.Intents.default()

intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix= '$', intents = intents)

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

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

client.run('Token Bot')
