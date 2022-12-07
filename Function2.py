import discord
from discord.ext import commands
import datetime, asyncio

intents = discord.Intents.default()

intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix= '!', intents = intents)

#@client.command()
#async def embed(ctx):
#    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0x0b1442)
#    await ctx.send(embed=embed)

@client.command(description="Mutes user.") # Function Mute สำหรับการทำผิดกฎหรือป้องกันการสแปม
@commands.has_permissions(manage_message=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.creat_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_message=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} reason : {reason}")
    await member.send(f"You were muted in the server {guild.name} reason {reason}")

@client.command(description="Unmutes user.") # สำหรับ Unmuted
@commands.has_permissions(manage_message=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were muted in the server {ctx.guild.name}")

@client.command()
async def move(ctx, member : discord.Member, channel : discord.VoiceChannel):
    await member.move_to(channel)
    print("move started")

@client.command() ### คำสั่ง Help จะแสดง Function ของตัวบอทที่เพิ่มเข้ามา
async def helpme(ctx):
    emBed=discord.Embed(title="Toturial Bot help", description="All available bot commands", color=0x080c30)
    emBed.add_field(name="help", value="Get help command", inline=False)
    emBed.add_field(name="test", value="Respond messasge that you've send", inline=False)
    emBed.add_field(name="send", value="Send hello message to user", inline=False)
    emBed.set_thumbnail(url="https://media.discordapp.net/attachments/964948925293404180/1048895134676295700/107478505_183669600023893_5611812722437419751_n.jpg?width=342&height=456")
    await ctx.send(embed=emBed)

@client.command()
async def schedule_daily_message():
    now = datetime.datetime.now()
    #then = now+datetime.timedelta(days=1)
    then = now.replace(hour=19, minute=13)
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)

    channel = client.get_channel(1046306958124273727)

    await channel.send("Time's Up!")

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
#async def reminder(ctx, time: int, *, msg):
#    while True:
#        await (time)
#        await ctx.send(f'{msg}, {ctx.author.mention}')

client.run('MTA0ODQ4NDQzMDUxMzE4ODkxNA.Gsmyvt.tLKHDc9jzyYtJ1BSB9m7KZKswGjXu0Ba9XhN-8')
