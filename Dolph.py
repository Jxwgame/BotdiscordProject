#discord
import discord
from discord.ext import commands
#datetime , time
import datetime
import asyncio
#math
import random
import math
#music
from help_cog import help_cog
from music_cog import music_cog
#weather report
from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup

#intents
intents = discord.Intents.default()

intents.members = True
intents.message_content = True
client = commands.Bot(command_prefix= '!', intents = intents)

#Import music cogs
client.remove_command('help')
client.add_cog(help_cog(client))
client.add_cog(music_cog(client))



#WEATHER REPORT

url = 'https://www.tmd.go.th/forecast/daily'

#function
def weather(x):
    web_req = req(url)
    page_html = web_req.read()
    web_req.close()

    #-Convert page_html to Soup Object 
    data = soup(page_html,'html.parser')
    #print(data) #view page sroce

    #-Find Element (td:'')
    temp = data.findAll('p',{'class':'sub-content'})
    #print((temp))

    province = data.findAll('p',{'class','sub-title'})

    result_temp = temp[x].text.replace(' ','') #data
    result_pv = province[x].text.replace(' ','') #position
    return('{} : {}'.format(result_pv,result_temp))

#command
@client.command()
async def onweather_north(ctx):
    try:
        result = weather(0)
        await ctx.send(f"{result}")
    except:
        pass

@client.command()
async def onweather_isan(ctx):
    try:
        result = weather(1)
        await ctx.send(f"{result}")
    except:
        pass

@client.command()
async def onweather_mid(ctx):
    try:
        result = weather(2)
        await ctx.send(f"{result}")
    except:
        pass

@client.command()
async def onweather_east(ctx):
    try:
        result = weather(3)
        await ctx.send(f"{result}")
    except:
        pass

@client.command()
async def onweather_southeast(ctx):
    try:
        result = weather(4)
        await ctx.send(f"{result}")
    except:
        pass

@client.command()
async def onweather_southwest(ctx):
    try:
        result = weather(5)
        await ctx.send(f"{result}")
    except:
        pass

@client.command()
async def onweather_bangkok(ctx):
    try:
        result = weather(6)
        await ctx.send(f"{result}")
    except:
        pass

def timezone(zone): # TimeZone
  '''Timezone'''
  from pytz import timezone
  from datetime import datetime
  time_format = '%d-%m-%Y %H:%S'
  now = datetime.now().strftime(time_format)
  dt = datetime.now(timezone(zone)).strftime(time_format)
  return(f"Time zone in {zone} is {dt}")

@client.command()
async def check_timezone_USA(ctx):
    try:
        result = timezone('US/Central')
        await ctx.send(f"{result}")
    except:
        pass

@client.command()
async def check_timezone_EU(ctx):
    try:
        result = timezone('Europe/London')
        await ctx.send(f"{result}")
    except:
        pass

@client.command()
async def check_timezone_Tokyo(ctx):
    try:
        result = timezone('Asia/Tokyo')
        await ctx.send(f"{result}")
    except:
        pass

@client.command()
async def check_timezone_Bangkok(ctx):
    try:
        result = timezone('Asia/Bangkok')
        await ctx.send(f"{result}")
    except:
        pass
@client.command()
async def check_timezone_UTC(ctx):
    try:
        result = timezone('UTC')
        await ctx.send(f"{result}")
    except:
        pass

#STATUS 

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

#CALCULATOR

#function
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

#command
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

#SERVER MANAGERMENT

@client.command()
async def move(ctx, member : discord.Member, channel : discord.VoiceChannel):
    await member.move_to(channel)
    print("move started")

@client.command() ### คำสั่ง Help จะแสดง Function ของตัวบอทที่เพิ่มเข้ามา
async def helpme(ctx):
    emBed=discord.Embed(title="Toturial Bot help", description="All available bot commands", color=0x080c30)
    emBed.add_field(name="Helpme :computer: ", value="Get help command ", inline=False)
    emBed.add_field(name="Math", value="prefix ! and follow command for math(x, y)\n - !mathadd\n- !mathdiv\n- !mathsub\n- !mathrandom\n- !mathmult\n- !mathsqrt", inline=False)
    emBed.add_field(name="Timezone", value=":clock1:  Check your timezone right now!\n Commands !check_timezone_(country)\n :flag_um:   USA      :flag_eu:   EU\n\
        :tokyo_tower:   Tokyo    :flag_th:   Bangkok", inline=False)
    emBed.add_field(name=":musical_note:  Music Command :musical_note: ", value="!play your url from youtube", inline=False)
    emBed.add_field(name=":partly_sunny:  Weathers", value="!onweather_(north, isan, mid, east, southeast, southwest)\n!onweather_north ภาคเหนือ    \
        !onweather_isan ภาคอีสาน\n!onweather_mid ภาคกลาง !onweather_east ภาคตะวันออก\n!onweather_southeast ใต้ฝั่งตะวันออก    !onweather_southwest ภาคใต้ฝั่งตะวันตก", inline=False)
    emBed.add_field(name="General commands for Host server", value="!move @mention\n!kick @mention\n!ban @mention\n!unban@mention", inline=False)
    emBed.set_footer(text="This form for commands dolph-discordbot let you enjoy!")
    emBed.set_thumbnail(url="https://media.discordapp.net/attachments/964948925293404180/1048895134676295700/107478505_183669600023893_5611812722437419751_n.jpg?width=342&height=456")
    emBed.set_image(url="https://media.discordapp.net/attachments/1046306958124273727/1052290840023793715/thank-you-very-much-memes.jpg?width=458&height=458")
    await ctx.send(embed=emBed)

@client.command()
async def timer(ctx):
    while 1:
        now = datetime.datetime.now()
        #then = now+datetime.timedelta(days=1)
        then = now.replace(hour=6, minute=0)
        wait_time = (then-now).total_seconds()
        await asyncio.sleep(wait_time)
        channel = client.get_channel(1046306958124273727)
        await channel.send(f"Time's Up {ctx.author.mention}")

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

client.run('MTA0ODQ4NDQzMDUxMzE4ODkxNA.GDjbHk.n3N6ol11gO5nr7XVwirHTjcte6zXge98oggJQI')
