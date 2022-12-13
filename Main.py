import discord
from discord.ext import commands
import datetime, asyncio
import random
import math
from help_cog import help_cog
from music_cog import music_cog

intents = discord.Intents.default()

intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix= '!', intents = intents)
url = 'https://www.tmd.go.th/forecast/daily'

def add(n: float, n2: float):
    return n + n2
def sub(n: float, n2: float):
    return n - n2
def rando(n: float, n2: float):
    return random.randfloat(n, n2)
def div(n: float, n2:float):
    return n/n2
def sqrt(n: float):
    return math.sqrt(n)
def mult(n: float, n2: float):
    return n * n2

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
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
        await ctx.semd(result)
    except:
        pass
@client.command()
async def mathrandom(ctx, x: float, y: float):
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
        await ctx.semd(result)
    except:
        pass

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
    emBed.add_field(name="Music Command", value="Commman_A_B", inline="True")
    emBed.add_field(name="Math Commands", value="Math", inline="True")
    emBed.set_thumbnail(url="https://media.discordapp.net/attachments/964948925293404180/1048895134676295700/107478505_183669600023893_5611812722437419751_n.jpg?width=342&height=456")
    await ctx.send(embed=emBed)

#@client.command()
#async def schedule_daily_message():
#    now = datetime.datetime.now()
#    #then = now+datetime.timedelta(days=1)
#    then = now.replace(hour=19, minute=13)
#    wait_time = (then-now).total_seconds()
#    await asyncio.sleep(wait_time)

#    channel = client.get_channel(1046306958124273727)

#    await channel.send("Time's Up!")

@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member : discord.Member, reason="Not specified"):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        await guild.create_role(name="Muted")
    if member == ctx.author:
        await ctx.send("You can't mute your self.")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_message=False, read_message_history=True, read_message=False)
    embed = discord.Embed(title="Muted", description=f"{member.mention} was muted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"You have been muted from: {guild.name} reason: {reason}")

@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member : discord.Member, reason="Not specified"):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Unmuted")
    embed = discord.Embed(title="Unmuted", description=f"{member.mention} was unmuted ", colour=discord.Colour.light_gray())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"You have been unmuted from: {guild.name} reason: {reason}")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason"):
    try:
        await user.kick(reason=reason)
        embed = discord.Embed(color=discord.Colour.red(), title="", description="")
        embed.add_field(name="Kicked:", value=f"", inline=True)
    except:
        embed = discord.Embed(color=discord.Color.red(), title="", description="")
        embed.add_field(name="Kicked:", value=f"", inline=True)
@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member, *, reason="No reason"):
    try:
        await user.ban(reason=reason)
        embed = discord.Embed(color=discord.Colour.red(), title="", description="")
        embed.add_field(name="Banned", value=f"The user **{user}** has been banned", inline=True)
        await ctx.reply(embed=embed)
    except:
        embed = discord.Embed(color=discord.Colour.red(), title="", description="")
        embed.add_field(name="Error.", value="Error", inline=True)

@client.command()
async def upload(ctx, attachment: discord.Attachment):
    if attachment in None:
        await ctx.send('You did not upload anything!')
    else:
        await ctx.send(f'You have uploaded <{attachment.url}>')

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    try:
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(color=discord.Colour.red(), title="", description="")
                embed.add_field(name="unbanned:", value=f"The user **{user}** has been unbanned.", inline=True)
    except:
        embed = discord.Embed(color=discord.Colour.red(), title="", description="")
        embed.add_field(name="Error:", value=f"Error", inline=True)
        await ctx.reply(embed=embed)

@client.command()
async def countdown(ctx):
    current_time = datetime.now()
    new_year = datetime(2023, 1, 1)
    diff = new_year - current_time
    if diff == 0:
        await ctx.send("Welcome New Year 2023 !!")
    else:
        await ctx.send(diff)

client.run('MTA0ODQ4NDQzMDUxMzE4ODkxNA.G-57R-.hTLprs1UTEN5dGuSoinvUN66IQIstdtDmYiELU')
