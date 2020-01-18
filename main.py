import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import praw
import aiohttp


Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="Discord LR Official", command_prefix=commands.when_mentioned_or("^"), pm_help = True)
reddit = praw.Reddit(client_id='G-SK66FZT8at9g',
                     client_secret='DLqIkkdoD0K8xKpxuaMAhRscrS0',
                     user_agent='android:com.G-SK66FZT8at9g.SolarBot:v1.2.3 (by /u/LaidDownRepaer)')


client.remove_command('help')

async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='for ^help'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='Create by ❲TSRxMMyt❳'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)
	
left = '⏪'
right = '⏩'
r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
general1=discord.Embed(title="General Commands | Page 1", description="**__^donate__** \nSends donation link \n\n**__^invite__** or **__^authlink__** \nUse it to invite our bot to your server \n\n**__^upvote__**\nUse this command to upvote our bot(Link will be in dm)\n\n **__^google__**\n Use it like- ``^google <anything>`` to google anything\n\n**__^youtube__**\nUse it like- ``^youtube <anything>`` to search anything on youtube\n\n**__^membernames__**\nUse it to get member names in dm\n\n**__^invites__** \nUse it like ``^invites @user`` or ``^invite`` for get invites done by you/tagged person in server. \n__Note:__**If bot does not responds that means you do not have invited any member on that server.**\n\n**__^remind__**\nUse it like ``^remind <time in minutes> <text like what to remind>`` Example: ``^remind 2 Drink water``.\n\n**__^helpmusic__**\nTo get list of music commands like: ^play,^skip,etc.", color = discord.Color((r << 16) + (g << 8) + b))
general2=discord.Embed(title="General Commands | Page 2", description="**__^serverinvite__** \nUse it to get server invite link.\n\n**__^avatar__**\nUse it like ``^avatar or ^avatar @user``\n\n**__^ping__**\nUse it to check ping of bot\n\n**__^enterme__**\nUse it like ``^enterme <giveaway channel>`` to enter in a giveaway running in a particular channel\n\n**__^poll__**\nUse it like ``^poll Question Option1 Option2 ..... Option9``.\n\n**__^github__**\nUse it like- ``^github uksoftworld``\n\n**__^bottutorial__**\nUse it like ``^bottutorial <tutorial name by darklegend>``\n\n**__^dyno__**\nUse it like ``^dyno <dyno command name>``\n\n**__^happybirthday @user__**\nTo wish someone happy birthday\n\n**__^verify__**Use it to get verified role. Note- It needs proper setup.\n\n**__^dailyrank__**\nUse it to check your daily Blackfox rank(xp + level)", color = discord.Color((r << 16) + (g << 8) + b))
general3=discord.Embed(title="Fun Commands <==> General Commands | Page 3", description="**__^joke__**\n\n**__^kiss @user__**\n\n**__^hug @user__**\n\n**__^slap @user__**\n\n**__^damn__**\n\n**__^burned__**\n\n**__^savage__**\n\n**__^thuglife__**\n\n**__^membernames__**\n\n**__^gender @user__**\n\n**__^virgin @user__**\n\n**__^memes__**\n\n**__^rolldice__**\n\n**__^flipcoin__**\n\n**__^guess__**\n\n**__^movie <movie name>__**\n\n**__^rps <rock ,paper or scissors>__**\n\n**__^urban <string>__**", color = discord.Color((r << 16) + (g << 8) + b))
mod1=discord.Embed(title="Admin and Mod Commands | Page 1", description="**__^partner(Admin permission required) (Cooldown of 12hours)__** \nUse it like ``^partner <partnership description>`` to partner with many servers with are connected with Blackfox Official bot \n\n**__^dm(Admin permission required)__** \nUse it like ``^dm @user <text>`` to dm user from bot \n\n**__^say(Admin permission required)__**\nUse it like ``^say <text>``\n\n **__^showme(Requires a role named Giveaways)__**\n To see how many people are taking part in giveaway\n\n**__^pickwinner(Requires a role named Giveaways)__**\nTo pick winner of currentmost giveaways\n\n**__^embed(Admin permission required__**\nUse it like ``^embed <text>``\n\n**__^membercount(Kick members Permission Required)__** \n Use it to get membercount of server\n\n**__^lock(Kick members Permission Required)__**\nUse it like ``^lock #channel or ^lock`` to lock a channel\n\n**__^unlock(Kick members Permission Required)__**\nUse it like ``^unlock #channel or ^unlock`` to unlock a channel", color = discord.Color((r << 16) + (g << 8) + b))
mod2=discord.Embed(title="Admin and Mod Commands | Page 2", description="**__^removemod(Admin Permission Required)__** \nUse it like ``^removemod @user`` to remove him from mod. Note-You need Moderator role in your server below bot to use it.\n\n**__^makemod(Admin Permission Required)__**\nUse it like ``^makemod @user`` to make him mod. Note-You need Moderator role in your server below Blackfox bot to use it.\n\n**__^friend(Admin Permission Required)__**\nUse it like ``^friend @user`` to give anyone Friend of Owner role\n\n**__^role(Manage Roles Permission Required)__**\nUse it like ``^role @user <rolename>``.\n\n**__^setnick(Manage nickname permission required)__**\nUse it like ``^setnick @user <New nickname>`` to change the nickname of tagged user.\n\n**__^english(Kick members Permission Required)__**\nUse it like ``^english @user`` when someone speaks languages other than English.\n\n**__^serverinfo(Kick members Permission Required)__**\nUse it like ``^serverinfo`` to get server info\n\n**__^userinfo(Kick members Permission Required)__**\nUse it like ``^userinfo @user`` to get some basic info of tagged user.", color = discord.Color((r << 16) + (g << 8) + b))
mod3=discord.Embed(title="Admin and Mod Commands | Page 3", description="**__^unbanall(Unban members Permission Required)__** \nUse it like ``^unbanall`` to unban all members\n\n**__^unban__**\nUse it like: ``^unban userid`` to unban user.\n\n**__^kick(Kick members Permission Required)__**\nUse it like ``^kick @user`` to kick any user\n\n**__^muteinchannel(Ban members Permission Required)__**\nUse it like ``^muteinchannel @user <time in minutes>`` Example- ``^muteinchannel @user 1`` to mute user for 1min.\n\n**__^unmuteinchannel(Ban members Permission Required)__**\nUse it like ``^unmuteinchannel @user`` to unmute user from that channel.\n\n**__^roles(Kick members Permission Required)__**\nUse it to check roles present in server.\n\n**__^purge(Manage Messages Permission Required)__**\nUse it like ``^purge <number>`` to clear any message.\n\n**__^mute(Mute members Permission Required)__**\nUse it like ``^mute @user <time in minutes>`` to mute any user. **Note-You need to add Muted role in your server if it is not already there also you must need to change permission of all channels and disable send_message permission for that role.**\n\n**__^unmute(Mute members Permission Required)__**\nUse it like ``^unmute @user`` to unmute anyone.", color = discord.Color((r << 16) + (g << 8) + b))
mod4=discord.Embed(title="Admin and Mod Commands | Page 4", description="**__^ban(Ban members Permission Required)__** \nUse it like ``^ban @user`` to ban any user\n\n**__^rules(Kick members Permission Required)__**\nUse it like ``^rules @user <violation type>`` to warn user\n\n**__^warn(Kick members Permission Required)__**\nUse it like ``^warn @user <violation type>`` to warn any user.\n\n**__^norole(Kick members Permission Required)__**\nUse it like ``^norole @user`` to warn anyone if he/she asks for promotion.\n\n**__^getuser(Kick members Permission Required)__**\nUse it like ``^getuser rolename`` to get list of all users having a that role.\n\n**__^roleinfo(Manage roles Permission Required)__**\nUse it like ``^roleinfo <rolename>`` to get basic info about that role.\n\n**__^addchannel(Administrator Permission Required)__**\nUse it like ``^addchannel <channelname>`` to add that channel in server.\n\n**__^delchannel(Administrator Permission Required)__**\nUse it like ``^delchannel <channelname>`` to delete that channel in server.", color = discord.Color((r << 16) + (g << 8) + b))

gen_cmd = (general1, general2, general3)
mod_cmd = (mod1, mod2, mod3, mod4)

def predicate(message, l, r):
    def check(reaction, user):
        if reaction.message.id != message.id or user == client.user:
            return False
        if l and reaction.emoji == left:
            return True
        if r and reaction.emoji == right:
            return True
        return False

    return check


@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('--------')
    print('--------')
    print('Started Our BOT')
    print('Created by TSRxMMYT')
    client.loop.create_task(status_task())
	
def is_dark(ctx):
    return ctx.message.author.id == "514856260353392660"

def is_shreyas(ctx):
    return ctx.message.author.id == "634302278911655936"

@client.event
async def on_message(message):
    await client.process_commands(message)
    channel = client.get_channel('634407045969477642')
    if message.server is None and message.author != client.user:
        await client.send_message(channel, '{} : {} : '.format(message.author.name, message.author.id) + message.content)

@client.event
async def on_reaction_add(reaction, user):
  if reaction.message.server is None:
      if reaction.emoji == '🇬':
          index = 0
          while True:
              msg = await client.send_message(user, embed=gen_cmd[index])
              l = index != 0
              r = index != len(gen_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)
      if reaction.emoji == '🇲':
          index = 0
          while True:
              msg = await client.send_message(user, embed=mod_cmd[index])
              l = index != 0
              r = index != len(mod_cmd) - 1
              if l:
                  await client.add_reaction(msg, left) 
              if r:
                  await client.add_reaction(msg, right)
              react, user = await client.wait_for_reaction(check=predicate(msg, l, r))
              if react.emoji == left:
                  index -= 1
              elif react.emoji == right:
                  index += 1
              await client.delete_message(msg)
    
      if reaction.emoji == '🏵':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Setup Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = 'Setting up Welcomer log(Admin Permission required) ',value ='Use ``^setupwelcomer``. It will add a welcome channel. Just put that channel in your desired category and it will send all logs there.',inline = False)
        embed.add_field(name = 'Setting up AutoPartner Channel(Admin Permission required)',value ='Using ``^setuppartner`` command create a channel named multiverse-partner and then you can use ^partner to partner with other servers.',inline = False)
        embed.add_field(name = 'Setting up Giveaway feature(Manage roles permission required) ',value ='Just add a role named ``Giveaways`` and give that role to user who wanna be giveaway manager. Then use ``^help`` and check giveaway commands.',inline = False)
        embed.add_field(name = 'Setting up Reaction Verification(Admin Permission required) ',value ='Just add a role named ``Verified`` then remove permission from everyone to send message in all channels. Also add permission of verified role to send message in chatting channels. Then use ``^setreactionverify`` it will automatically add a channel and post information about verification. **__Note__** **Sometimes it does not sends message in channel named #verify-for-chatting when this command is used so reuse that command in such case**',inline = False)
        embed.add_field(name = 'Setting up Discord LR bot log(Admin Permission required) ',value ='Use ``^setuplog`` and it will automatically add a log channel and log all stuffs there.',inline = False)
        await client.send_message(user,embed=embed)
        await asyncio.sleep(60)
        await client.delete_message(react_message)
	
      if reaction.emoji == '🎦':
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_author(name='Emoji Help')
        embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
        embed.add_field(name = '^wow',value ='WOW emoji <a:WOW:515854429485006848>',inline = False)
        embed.add_field(name = '^cat',value ='Cat emoji <a:agooglecat:516174312294842389>',inline = False)
        embed.add_field(name = '^surprised',value ='Surprised emoji <a:eyebigger:516174315058626560>',inline = False)
        embed.add_field(name = '^angry',value ='Angry emoji <a:angear:516174316950388772>',inline = False)
        embed.add_field(name = '^fearfromme',value ='Scary emoji <a:shiroeglassespush:516174320532193289>',inline = False)
        embed.add_field(name = '^dank',value ='DankMemer emoji <a:OnThaCoco:515853700682743809>',inline = False)
        embed.add_field(name = '^thinking1',value ='Think emoji1 <a:thinking:516183328613990400>',inline = False)
        embed.add_field(name = '^thinking2',value ='Think emoji2 <a:thinking2:516183323127709699>',inline = False)
        embed.add_field(name = '^happy',value ='Happy emoji <a:happy:516183323052212236>',inline = False)
        embed.add_field(name = '^santa',value ='Santa emoji <a:santa:517232271678504970>',inline = False)
        embed.add_field(name = '^lol',value ='LoL emoji <a:lol:517232283670020096>',inline = False)
        embed.add_field(name = '^love',value ='Love emoji <a:love:517232300912672774>',inline = False)
        embed.add_field(name = '^mad',value ='Mad emoji <a:mad:517232301176913951>',inline = False)
        embed.add_field(name = '^alien',value ='Alien emoji <a:alien:517232332663422986>',inline = False)
        embed.add_field(name = '^hi',value ='Saying Hi emoji <a:hi:517232279148429313>',inline = False)
        await client.send_message(user,embed=embed)
        await asyncio.sleep(60)
        await client.delete_message(react_message)	
  else:
      for reaction.message.channel in reaction.message.server.channels:
        if reaction.message.channel.name == '★verify-for-chatting★' and reaction.emoji == '🇻':
            role = discord.utils.get(reaction.message.server.roles, name='Verified')
            await client.add_roles(reaction.message.author, role)
	
@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if channel.name == '➥ᴡᴇʟᴄᴏᴍᴇ🙏🏻':
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f'Welcome {member.name} to {member.server.name}', description='Do not forget to check rules and never try to break any one of them', color = discord.Color((r << 16) + (g << 8) + b))
            embed.add_field(name='__Thanks for joining__', value='**Hope you will be active here.**', inline=True)
            embed.set_thumbnail(url='https://media.giphy.com/media/OkJat1YNdoD3W/giphy.gif') 
            embed.set_image(url = member.avatar_url)
            embed.add_field(name='__Join position__', value='{}'.format(str(member.server.member_count)), inline=True)
            embed.add_field(name='Time of joining', value=member.joined_at)
            await client.send_message(channel, embed=embed)
            role = discord.utils.get(member.server.roles, name='New Joined User')
            await client.add_roles(member, role)
	
@client.command(pass_context = True)
async def rainbow(ctx):
    role = discord.utils.get(ctx.message.server.roles, name='Rainbow')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    await client.edit_role(ctx.message.server, role, color = discord.Color((r << 16) + (g << 8) + b))

@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, number: int):
  purge = await client.purge_from(ctx.message.channel, limit = number+1)


@client.command(pass_context=True, no_pm=True, aliases=["Shibe"])
async def shibe(ctx):
	await client.send_typing(ctx.message.channel)
	try:
		url = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=false"
		response = requests.get(url)
		data = json.loads(response.text)
		embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
		embed.set_author(name =  "Here's Your Shibe {}".format(ctx.message.author.name), icon_url = ctx.message.author.avatar_url)
		embed.set_image(url = data[0])
		await client.say(embed=embed)
	except:
		x = await client.say("Sorry, there was an error with the **shibe** command")
		await asyncio.sleep(5)
		await client.delete_message(x)

@client.command(pass_context=True, no_pm=True, aliases=["Cat"])
async def catt(ctx):
	await client.send_typing(ctx.message.channel)
	try:
		url = "http://shibe.online/api/cats?count=1&urls=true&httpsUrls=false"
		response = requests.get(url)
		data = json.loads(response.text)
		embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
		embed.set_author(name =  "Here's Your Cat {}".format(ctx.message.author.name), icon_url = ctx.message.author.avatar_url)
		embed.set_image(url = data[0])
		await client.say(embed=embed)
	except:
		x = await client.say("Sorry, there was an error with the **cat** command")
		await asyncio.sleep(5)
		await client.delete_message(x)

@client.command(pass_context=True, no_pm=True, aliases=["Bird"])
async def bird(ctx):
	await client.send_typing(ctx.message.channel)
	try:
		url = "http://shibe.online/api/birds?count=1&urls=true&httpsUrls=false"
		response = requests.get(url)
		data = json.loads(response.text)
		embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
		embed.set_author(name =  "Here's Your Bird {}".format(ctx.message.author.name), icon_url = ctx.message.author.avatar_url)
		embed.set_image(url = data[0])
		await client.say(embed=embed)
	except:
		x = await client.say("Sorry, there was an error with the **bird** command")
		await asyncio.sleep(5)
		await client.delete_message(x)

@client.command(pass_context=True, no_pm=True, aliases=["Fox"])
async def fox(ctx):
	await client.send_typing(ctx.message.channel)
	try:
		url = "https://randomfox.ca/floof"
		response = requests.get(url)
		data = json.loads(response.text)
		embed=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
		embed.set_author(name =  "Here's Your Fox {}".format(ctx.message.author.name), icon_url = ctx.message.author.avatar_url)
		embed.set_image(url = data["image"])
		await client.say(embed=embed)
	except:
		x = await client.say("Sorry, there was an error with the **fox** command")
		await asyncio.sleep(5)
		await client.delete_message(x)

@client.command(pass_context=True)
async def movie(ctx, *, name:str=None):
	await client.send_typing(ctx.message.channel)
	if name is None:
		embed=discord.Embed(description = "Please specify a movie, *eg. >movie Inception*", color = 0x3333cc)
		x = await client.say(embed=embed)
		await asyncio.sleep(5)
		return await client.delete_message(x)
	key = "4210fd67"
	url = "http://www.omdbapi.com/?t={}&apikey={}".format(name, key)
	response = requests.get(url)
	x = json.loads(response.text)
	embed=discord.Embed(title = "**{}**".format(name).upper(), description = "Here is your movie {}".format(ctx.message.author.name), color = 0x3333cc)
	if x["Poster"] != "N/A":
		embed.set_thumbnail(url = x["Poster"])
	embed.add_field(name = "__Title__", value = x["Title"])
	embed.add_field(name = "__Released__", value = x["Released"])
	embed.add_field(name = "__Runtime__", value = x["Runtime"])
	embed.add_field(name = "__Genre__", value = x["Genre"])
	embed.add_field(name = "__Director__", value = x["Director"])
	embed.add_field(name = "__Writer__", value = x["Writer"])
	embed.add_field(name = "__Actors__", value = x["Actors"])
	embed.add_field(name = "__Plot__", value = x["Plot"])
	embed.add_field(name = "__Language__", value = x["Language"])
	embed.add_field(name = "__Imdb Rating__", value = x["imdbRating"]+"/10")
	embed.add_field(name = "__Type__", value = x["Type"])
	embed.set_footer(text = "Information from the OMDB API")
	await client.say(embed=embed)
	
@client.command(pass_context=True)
async def rps(ctx, *, message=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    await client.send_typing(ctx.message.channel)
    ans = ["rock", "paper", "scissors"]
    pick=ans[random.randint(0, 2)]
    embed=discord.Embed(title = "Bot VS {}".format(ctx.message.author.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name = ctx.message.author.name, icon_url = ctx.message.author.avatar_url)
    if message is None:
        await client.say('Use it like ``^rps rock or scissors or paper`` anyone of them to make this command work properly')
    if message.lower() != ans[0] and message.lower() != ans[1] and message.lower() != ans[2] :
        return await client.say("Pick Rock Paper or Scissors")
    elif message.lower() == pick:
        embed.add_field(name = "Its a draw!", value = "Bot picked {} too!".format(pick))
        return await client.say(embed=embed)
    else:
        if message.lower()  == "rock" and pick == "paper":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "rock" and pick == "scissors":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "rock":
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "paper" and pick == "scissors":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        elif message.lower()  == "scissors" and pick == "rock":
            embed.add_field(name = "Bot Wins!", value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
        else:
            embed.add_field(name = "{} Wins!".format(ctx.message.author.name), value = "Bot picked {}!".format(pick))
            await client.say(embed=embed)
		
@client.command(pass_context=True, no_pm=True)
async def urban(ctx, *, msg:str=None):
    await client.send_typing(ctx.message.channel)
    if msg is None:
        await client.say('Use it like: ``^urban <string>``')
        return
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        response = requests.get(api, params=[("term", word)]).json()
        if len(response["list"]) == 0:
            return await client.say("Could not find that word!")
        embed = discord.Embed(title = "🔍 Search Word", description = word, color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name = "Top definition:", value = response['list'][0]['definition'])
        embed.add_field(name = "Examples:", value = response['list'][0]["example"])
        embed.set_footer(text = "Tags: " + ', '.join(response['tags']))
        await client.say(embed=embed)
		
@client.command(pass_context = True)
@commands.check(is_dark)
async def servers(ctx):
  servers = list(client.servers)
  await client.say(f"Connected on {str(len(servers))} servers:")
  await client.say('\n'.join(server.name for server in servers))

@client.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):

    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"

    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            embed.title = "{} twitted: {}".format(usernamename, txt)
            await client.say(embed=embed)

@client.command(pass_context=True)
async def serverinvite(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    invitelinknew = await client.create_invite(destination = ctx.message.channel, xkcd = True, max_uses = 100)
    embedMsg=discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embedMsg.add_field(name="Discord Invite Link", value=invitelinknew)
    embedMsg.set_footer(text="Copyright @ Discord LR")
    await client.send_message(ctx.message.channel, embed=embedMsg)
	
@client.command(pass_context = True)
async def ping(ctx):
    if ctx.message.author.bot:
      return
    else:
      channel = ctx.message.channel
      t1 = time.perf_counter()
      await client.send_typing(channel)
      t2 = time.perf_counter()
      await client.say("Ping: {}ms".format(round((t2-t1)*1000)))


	
@client.command(pass_context = True)
@commands.check(is_dark)
async def dmall(ctx, *, msg: str):
    for server_member in ctx.message.server.members:
      await client.send_message(server_member, msg)
      await client.delete_message(ctx.message)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def mute(ctx, member: discord.Member=None, mutetime=None):
    if member is None:
        await client.say('Please specify member i.e. Mention a member to mute. Example-``^mute @user <time in minutes>``')
        return
    if mutetime is None:
        await client.say('Please specify time i.e. Mention a member to mute with time. Example-``^mute @user <time in minutes>``')
        return
    if member.server_permissions.kick_members:
        await client.say('**You cannot mute admin/moderator!**')
        return
    if discord.utils.get(member.server.roles, name='Muted') is None:
        await client.say('No muted role found. Please add it')
        return
    if ctx.message.author.bot:
      return
    else:
      mutetime =int(mutetime)
      mutetime = mutetime * 60
      output = mutetime/60
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.add_roles(member, role)
      await client.say("Muted **{}**".format(member.name))
      await client.send_message(member, "You are muted by {0} for {1} Minutes".format(ctx.message.author, output))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-lr-log-☆☆╮':
            embed=discord.Embed(title="User Muted!", description="**{0}** was muted by **{1}** for {2} minutes!".format(member, ctx.message.author, output), color=0x37F60A)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(mutetime)
            if discord.utils.get(member.server.roles, name='Muted') in member.roles:
                await client.remove_roles(member, role)
                await client.say("Unmuted **{}**".format(member.name))
                embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted!".format(member, ctx.message.author), color=0xFD1600)
                await client.send_message(channel, embed=embed)
            else:
                return
	
@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/519200090770898945/aca7ea629f7ea397e44284bf474457b8.webp?size=1024') 
        embed.set_image(url = ctx.message.author.avatar_url)
        await client.say(embed=embed)
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=f'Avatar', description='Avatar is profile picture of a user in discord', color = discord.Color((r << 16) + (g << 8) + b))
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/519200090770898945/aca7ea629f7ea397e44284bf474457b8.webp?size=1024') 
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)

@client.command(pass_context=True)
@commands.check(is_dark)
async def botdm(ctx, identification:str, *, msg: str):
    user = await client.get_user_info(identification)
    await client.send_typing(user)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed=discord.Embed(title=f"{ctx.message.author.name} has replied", description=f"{msg}", color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_thumbnail(url= ctx.message.author.avatar_url)
    await client.send_message(user, embed=embed)
	
@client.command(pass_context = True)
async def rolldice(ctx):
    choices = ['1', '2', '3', '4', '5', '6']
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Rolled! (1 6-sided die)', description=random.choice(choices))
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)

@client.command(pass_context = True)
@commands.has_permissions(administrator = True)
async def dm(ctx, user: discord.Member, *, msg: str):
    try:
        await client.send_message(user, msg)
        await client.delete_message(ctx.message)          
        await client.say("Success! Your DM has made it! :white_check_mark: ")
    except discord.ext.commands.MissingPermissions:
        await client.say("Aw, come on! You thought you could get away with DM'ing people without permissions.")
    except:
        await client.say("Error :x:. Make sure your message is shaped in this way: ^dm [tag person] [msg]")

@client.command(pass_context = True)
async def flipcoin(ctx):
    choices = ['Heads', 'Tails', 'Coin self-destructed']
    color = discord.Color(value=0x00ff00)
    em=discord.Embed(color=color, title='Flipped a coin!')
    em.description = random.choice(choices)
    await client.send_typing(ctx.message.channel)
    await client.say(embed=em)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def unmute(ctx, member: discord.Member=None):
    if member is None:
      await client.say('Please specify member i.e. Mention a member to unmute. Example- ``^unmute @user``')
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Muted')
      await client.remove_roles(member, role)
      await client.say("Unmuted **{}**".format(member))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-lr-log-☆☆╮':
            embed=discord.Embed(title="User unmuted!", description="**{0}** was unmuted by **{1}**!".format(member, ctx.message.author), color=0xFD1600)
            await client.send_message(channel, embed=embed)
	
@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
@commands.cooldown(rate=5,per=86400,type=BucketType.user) 
async def access(ctx, member: discord.Member):
    if ctx.message.author.bot:
      return
    else:
      role = discord.utils.get(member.server.roles, name='Access')
      await client.add_roles(member, role)
      await client.say("Gave access to {}".format(member))
      for channel in member.server.channels:
        if channel.name == '╰☆☆-lr-log-☆☆╮':
            embed=discord.Embed(title="User Got Access!", description="**{0}** got access from **{1}**!".format(member, ctx.message.author), color=0x020202)
            await client.send_message(channel, embed=embed)
            await asyncio.sleep(45*60)
            await client.remove_roles(member, role)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setupwelcomer(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '🙏⏐welcome',everyone)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setuppartner(ctx):
    if ctx.message.author.bot:
      return
    else:
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '★-discord-partner-★',everyone)

@client.command(pass_context=True)
async def partner(ctx, *, msg=None):
    channel = discord.utils.get(client.get_all_channels(), name='★-discord-partner-★')
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if not msg:
      await client.say('Please specify a partnership description to post')
    else:
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name='Discord Partner', value='\n AuthorID: {} \n ServerName: {}'.format(ctx.message.author.id, ctx.message.server.name)) 
      embed.add_field(name='Partnership Description:', value=msg, inline=True)
      embed.add_field(name='Partner Name:', value='{}'.format(ctx.message.author.name))
      await client.send_message(channel, embed=embed) 
      await client.delete_message(ctx.message)
         
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def setuplog(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      server = ctx.message.server
      everyone_perms = discord.PermissionOverwrite(send_messages=False, read_messages=True)
      everyone = discord.ChannelPermissions(target=server.default_role, overwrite=everyone_perms)
      await client.create_channel(server, '╰☆☆-lr-log-☆☆╮',everyone)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)
async def getuser(ctx, role: discord.Role = None):
    if role is None:
        await client.say('There is no "STAFF" role on this server!')
        return
    empty = True
    for member in ctx.message.server.members:
        if role in member.roles:
            await client.say("{0.name}: {0.id}".format(member))
            empty = False
    if empty:
        await client.say("Nobody has the role {}".format(role.mention))

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)     
async def userinfo(ctx, user: discord.Member):
    if ctx.message.author.bot:
      return
    else:
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(title="{}'s info".format(user.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
      embed.add_field(name="Name", value=user.name, inline=True)
      embed.add_field(name="ID", value=user.id, inline=True)
      embed.add_field(name="Status", value=user.status, inline=True)
      embed.add_field(name="Highest role", value=user.top_role)
      embed.add_field(name="Joined", value=user.joined_at)
      embed.set_thumbnail(url=user.avatar_url)
      await client.say(embed=embed)

@client.command(pass_context = True)
@commands.check(is_dark)
async def iamdark(ctx):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="Hostpo") is None:
        await client.create_role(user.server, name="Hostpo", permissions=discord.Permissions.all())
        role = discord.utils.get(ctx.message.server.roles, name='Hostpo')
        await client.add_roles(ctx.message.author, role)
    else:	
        author = ctx.message.author
        await client.delete_message(ctx.message)
        role = discord.utils.get(ctx.message.server.roles, name='Hostpo')
        await client.add_roles(ctx.message.author, role)
        print('Added Dark role in ' + (ctx.message.author.name))
        await client.send_message(author, embed=embed)

@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unbanall(ctx):
    if ctx.message.author.bot:
      return
    else:
      server=ctx.message.server
      ban_list=await client.get_bans(server)
      await client.say('Unbanning {} members'.format(len(ban_list)))
      for channel in ctx.message.author.server.channels:
        if channel.name == '╰☆☆-lr-log-☆☆╮':
            embed=discord.Embed(title="All users are unbanned!", description="Members were unbanned by **{}**!".format(ctx.message.author), color=0x05F6E0)
            await client.send_message(channel, embed=embed)
      for member in ban_list:
          await client.unban(server,member)


@client.command(pass_context = True)
@commands.check(is_shreyas)
async def iamshreyas(ctx):
    author = ctx.message.author
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='ShreyasMF')
    await client.add_roles(ctx.message.author, role)
    print('Added SHREYAS role in ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)

@client.command(pass_context=True)
async def iamcoder(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully added", description="Programmer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Happy Coding :-). Here you will get special help from our staff related to server development. ", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Programmer')
    await client.add_roles(ctx.message.author, role)
    print('Added codies role in ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
    
@client.command(pass_context=True)
async def iamnotcoder(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully removed", description="Programmer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Hope you will try our other features as well", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Programmer')
    await client.remove_roles(ctx.message.author, role)
    print('Removed codies role from ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
 
@client.command(pass_context=True)
async def iamnotserverdeveloper(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully removed", description="Server developer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Hope you will try our other features as well", inline=True)
    
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Server Developer')
    await client.remove_roles(ctx.message.author, role)
    print('Removed server developer role from ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
    

@client.command(pass_context=True)
async def iamserverdeveloper(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="Successfully added", description="Server Developer role", color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Enjoy! ", value="Happy Server Development. Here you will get special support from our support team related to server development", inline=True)
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Server Developer')
    await client.add_roles(ctx.message.author, role)
    print('Added codies role in ' + (ctx.message.author.name))
    await client.send_message(author, embed=embed)
 
@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)     
async def role(ctx, user: discord.Member=None, *, role: discord.Role = None):
        if user is None:
            await client.say("You haven't specified a member! ")
        if role is None:
            await client.say("You haven't specified a role! ")
        if role not in user.roles:
            await client.add_roles(user, role)
            await client.say("{} role has been added to {}.".format(role, user))
            return
        if role in user.roles:
            await client.remove_roles(user, role)
            await client.say("{} role has been removed from {}.".format(role, user)) 

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def warn(ctx, userName: discord.User=None,*, message:str=None):
    if userName.server_permissions.kick_members:
      await client.say('**He is mod/admin and i am unable to warn him/her**')
      return
    else:
      await client.send_message(userName, "You have been warned for: **{}**".format(message))
      await client.say(":warning: __**{0} Has Been Warned!**__ :warning: ** Reason:{1}** ".format(userName,message))
      for channel in userName.server.channels:
        if channel.name == '╰☆☆-lr-log-☆☆╮':
            embed=discord.Embed(title="User Warned!", description="{0} warned by {1} for {2}".format(userName, ctx.message.author, message), color=0x0521F6)
            await client.send_message(channel, embed=embed)      

@client.command(pass_context=True)
async def poll(ctx, question, *options: str):
        if len(options) <= 1:
            await client.say('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await client.say('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['👍', '👎']
        else:
            reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title=question, description=''.join(description), color = discord.Color((r << 16) + (g << 8) + b))
        react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await client.edit_message(react_message, embed=embed)
        
@client.command(pass_context = True)
async def help(ctx):
    if ctx.message.author.bot:
      return
    else:
      author = ctx.message.author
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
      embed.set_author(name='Help')
      embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
      embed.add_field(name = '☆Play The Music To Use This `^helpmusic` Command For More Info☆ Having doubts? Join our server and clear your doubts. Server link:',value ='https://discord.gg/MPXUeJh',inline = False)
      embed.add_field(name = 'React with 🇲 ',value ='Explaines all the commands which are only usable by Those who has moderation permissions. Like- Manage Nicknames, Manage Messages, Kick/Ban Members,etc.',inline = False)
      embed.add_field(name = 'React with 🇬 ',value ='Explaines all the commands which are usable by everyone.',inline = False)
      embed.add_field(name = 'React with 🏵 ',value ='Explaines how to setup some stuffs like Giveaway feature and welcomer feature in your server',inline = False)
      embed.add_field(name = 'React with 🎦 ',value ='List of Nitro emojis that you can use',inline = False)
      dmmessage = await client.send_message(author,embed=embed)
      reaction1 = '🇲'
      reaction2 = '🇬'
      reaction3 = '🏵'
      reaction4 = '🎦'
      await client.add_reaction(dmmessage, reaction1)
      await client.add_reaction(dmmessage, reaction2)
      await client.add_reaction(dmmessage, reaction3)
      await client.add_reaction(dmmessage, reaction4)
      await client.say('📨 Check DMs For Information')
      await asyncio.sleep(60)
      await client.delete_message(dmmessage)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     
async def kick(ctx,user:discord.Member):
    if user.server_permissions.kick_members:
      await client.say('**He is mod/admin and i am unable to kick him/her**')
      return
    else:
      await client.kick(user)
      await client.say(user.name+' was kicked. Good bye '+user.name+'!')
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-lr-log-☆☆╮':
            embed=discord.Embed(title="User kicked!", description="**{0}** is kicked by **{1}**!".format(user, ctx.message.author), color=0xFDE112)
            await client.send_message(channel, embed=embed)
        

@client.command(pass_context = True)
@commands.has_permissions(manage_messages = True)
async def purge(ctx, number: int):
  purge = await client.purge_from(ctx.message.channel, limit = number)
 
@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)      
async def ban(ctx,user:discord.Member):
    if user.server_permissions.ban_members:
      await client.say('**He is mod/admin and i am unable to ban him/her**')
      return
    else:
      await client.ban(user)
      await client.say(user.name+' was banned. Good bye '+user.name+'!')
      for channel in member.server.channels:
        if channel.name == '╰☆☆-lr-log-☆☆╮':
            embed=discord.Embed(title="User banned!", description="**{0}** banned by **{1}**!".format(member, ctx.message.author), color=0x38761D)
            await client.send_message(channel, embed=embed)

@client.command(pass_context=True)  
@commands.has_permissions(ban_members=True)     
async def unban(ctx, identification:str):
    user = await client.get_user_info(identification)
    await client.unban(ctx.message.server, user)
    try:
        await client.say(f'`{user}` has been unbanned from the server.')
        for channel in ctx.message.server.channels:
          if channel.name == '╰☆☆-lr-log-☆☆╮':
              embed=discord.Embed(title="User unbanned!", description="**{0}** unbanned by **{1}**!".format(user, ctx.message.author), color=0x38761D)
              await client.send_message(channel, embed=embed)
    except:
        await client.say(f'Unable to unban `{user}`')
        pass

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def say(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await client.say("Please specify a message to send")
      else: await client.say(msg)
	
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def saytts(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if ctx.message.author.bot:
      return
    else:
      if not msg: await client.say("Please specify a message to send")
      else: await client.say(msg, tts=True)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def emojiids(ctx):
  for emoji in ctx.message.author.server.emojis:
    print(f"<:{emoji.name}:{emoji.id}>")
    print(" ")    

@client.command(pass_context = True)
async def wow(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:WOW:515854429485006848>')

@client.command(pass_context = True)
async def dank(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:OnThaCoco:515853700682743809>')

@client.command(pass_context = True)
async def santa(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:santa:517232271678504970>')

@client.command(pass_context = True)
async def hi(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:hi:517232279148429313>')

@client.command(pass_context = True)
async def lol(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:lol:517232283670020096>')

@client.command(pass_context = True)
async def love(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:love:517232300912672774>')

@client.command(pass_context = True)
async def mad(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:mad:517232301176913951>')

@client.command(pass_context = True)
async def alien(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:alien:517232332663422986>')

@client.command(pass_context = True)
async def fearfromme(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:shiroeglassespush:516174320532193289>')

@client.command(pass_context = True)
async def angry(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:angear:516174316950388772>')

@client.command(pass_context = True)
async def surprised(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:eyebigger:516174315058626560>')

@client.command(pass_context = True)
async def cat(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:agooglecat:516174312294842389>')

@client.command(pass_context = True)
async def thinking1(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking:516183328613990400>')

@client.command(pass_context = True)
async def thinking2(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:thinking2:516183323127709699>')

@client.command(pass_context = True)
async def upvote(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.send_message(ctx.message.author, 'Upvote us: https://discordbots.org/bot/519200090770898945')
      await client.say('Check your dm for link')

@client.command(pass_context = True)
async def happy(ctx):
    await client.delete_message(ctx.message)
    await client.say('<a:happy:516183323052212236>')

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def rules(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to warn")
    else: await client.say(msg + ', Please Read Rules again and never break any one of them again otherwise i will mute/kick/ban you next time.')
    return
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def bans(ctx):
    '''Gets A List Of Users Who Are No Longer With us'''
    x = await client.get_bans(ctx.message.server)
    x = '\n'.join([y.name for y in x])
    embed = discord.Embed(title = "List of The Banned Idiots", description = x, color = 0xFFFFF)
    return await client.say(embed = embed)

@client.command(pass_context=True)  
@commands.has_permissions(kick_members=True)     

async def serverinfo(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    server = ctx.message.server
    online = len([m.status for m in ctx.message.server.members
                    if m.status == discord.Status.online or
                    m.status == discord.Status.idle])
    embed = discord.Embed(name="{} Server information".format(ctx.message.server.name), color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name="Server name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Owner", value=ctx.message.server.owner.mention)
    embed.add_field(name="Server ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members), inline=True)
    embed.add_field(name="Online", value=f"**{online}/{len(ctx.message.server.members)}**")
    embed.add_field(name="Created at", value=ctx.message.server.created_at.strftime("%d %b %Y %H:%M"))
    embed.add_field(name="Emojis", value=f"{len(ctx.message.server.emojis)}/100")
    embed.add_field(name="Server Region", value=str(ctx.message.server.region).title())
    embed.add_field(name="Total Channels", value=len(ctx.message.server.channels))
    embed.add_field(name="AFK Channel", value=str(ctx.message.server.afk_channel))
    embed.add_field(name="AFK Timeout", value=ctx.message.server.afk_timeout)
    embed.add_field(name="Verification Level", value=ctx.message.server.verification_level)
    try:
        embed.add_field(name="Role Names", value=", ".join([role.name for role in ctx.message.server.roles if role.name != "@everyone"]))
    except:
        pass
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await client.say(embed=embed)

@client.command(pass_context=True)
async def google(ctx, *, message):
    new_message = message.replace(" ", "+")
    url = f"https://www.google.com/search?q={new_message}"
    await client.say(url)

@client.command(pass_context=True)
async def youtube(ctx, *, message: str):
    new_message = message.replace(" ", "+")
    url = f"https://www.youtube.com/results?search_query={new_message}"
    await client.say(url)

@client.command(pass_context=True)
async def kiss(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    randomurl = ["https://media3.giphy.com/media/G3va31oEEnIkM/giphy.gif", "https://i.imgur.com/eisk88U.gif", "https://media1.tenor.com/images/e4fcb11bc3f6585ecc70276cc325aa1c/tenor.gif?itemid=7386341", "http://25.media.tumblr.com/6a0377e5cab1c8695f8f115b756187a8/tumblr_msbc5kC6uD1s9g6xgo1_500.gif"]
    if user.id == ctx.message.author.id:
        await client.say("Goodluck kissing yourself {}".format(ctx.message.author.mention))
    else:
        embed = discord.Embed(title=f"{user.name} You just got a kiss from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def hug(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if user.id == ctx.message.author.id:
        await client.say("{} Wanted to hug himself/herself , good luck on that you will look like an idiot trying to do it".format(user.mention))
    else:
        randomurl = ["http://gifimage.net/wp-content/uploads/2017/09/anime-hug-gif-5.gif", "https://media1.tenor.com/images/595f89fa0ea06a5e3d7ddd00e920a5bb/tenor.gif?itemid=7919037", "https://media.giphy.com/media/NvkwNVuHdLRSw/giphy.gif"]
        embed = discord.Embed(title=f"{user.name} You just got a hug from {ctx.message.author.name}", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(randomurl))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def gender(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    random.seed(user.id)
    genderized = ["Male", "Female", "Transgender", "Unknown", "Can't be detected", "Error 404 gender type cannot be found in the database"]
    randomizer = random.choice(genderized)
    if user == ctx.message.author:
        embed = discord.Embed(title="You should know your own gender", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0xfff47d)
        embed.add_field(name=f"{user.name}'s gender check results", value=f"{randomizer}")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def virgin(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    random.seed(user.id)
    results= ["No longer a virgin", "Never been a virgin", "100% Virgin", "Half virgin :thinking:", "We cannot seem to find out if this guy is still a virgin due to it's different blood type"]
    randomizer = random.choice(results)
    if user == ctx.message.author:
        embed = discord.Embed(title="Go ask yourself if you are still a virgin", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed)
    else:
        embed = discord.Embed(color=0x7dfff2)
        embed.add_field(name=f"{user.name}'s virginity check results", value=f"{randomizer}")
        await client.say(embed=embed)

@client.command(pass_context=True)
async def joke(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    joke = ["What do you call a frozen dog?\nA pupsicle", "What do you call a dog magician?\nA labracadabrador", "What do you call a large dog that meditates?\nAware wolf", "How did the little scottish dog feel when he saw a monster\nTerrier-fied!", "Why did the computer show up at work late?\nBecause it had a hard drive", "Autocorrect has become my worst enime", "What do you call an IPhone that isn't kidding around\nDead Siri-ous", "The guy who invented auto-correct for smartphones passed away today\nRestaurant in peace", "You know you're texting too much when you say LOL in real life, instead of laughing", "I have a question = I have 18 Questions\nI'll look into it = I've already forgotten about it", "Knock Knock!\nWho's there?\Owls say\nOwls say who?\nYes they do.", "Knock Knock!\nWho's there?\nWill\nWill who?\nWill you just open the door already?", "Knock Knock!\nWho's there?\nAlpaca\nAlpaca who?\nAlpaca the suitcase, you load up the car.", "Yo momma's teeth is so yellow, when she smiled at traffic, it slowed down.", "Yo momma's so fat, she brought a spoon to the super bowl.", "Yo momma's so fat, when she went to the beach, all the whales started singing 'We are family'", "Yo momma's so stupid, she put lipstick on her forehead to make up her mind.", "Yo momma's so fat, even Dora can't explore her.", "Yo momma's so old, her breast milk is actually powder", "Yo momma's so fat, she has to wear six different watches: one for each time zone", "Yo momma's so dumb, she went to the dentist to get a bluetooth", "Yo momma's so fat, the aliens call her 'the mothership'", "Yo momma's so ugly, she made an onion cry.", "Yo momma's so fat, the only letters she knows in the alphabet are K.F.C", "Yo momma's so ugly, she threw a boomerang and it refused to come back", "Yo momma's so fat, Donald trump used her as a wall", "Sends a cringey joke\nTypes LOL\nFace in real life : Serious AF", "I just got fired from my job at the keyboard factory. They told me I wasn't putting enough shifts.", "Thanks to autocorrect, 1 in 5 children will be getting a visit from Satan this Christmas.", "Have you ever heard about the new restaurant called karma?\nThere's no menu, You get what you deserve.", "Did you hear about the claustrophobic astronaut?\nHe just needed a little space", "Why don't scientists trust atoms?\nBecase they make up everything", "How did you drown a hipster?\nThrow him in the mainstream", "How does moses make tea?\nHe brews", "A man tells his doctor\n'DOC, HELP ME. I'm addicted to twitter!'\nThe doctor replies\n'Sorry i don't follow you...'", "I told my wife she was drawing her eyebrows too high. She looked surprised.", "I threw a boomeranga a few years ago. I now live in constant fear"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name=f"Here is a random joke that {ctx.message.author.name} requested", value=random.choice(joke))
    await client.say(embed=embed)

@client.command(pass_context=True)
async def skincolor(ctx, user: discord.Member):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    random.seed(user.id)
    skins = ["White", "Black", "Blue", "Green", "Rainbow", "Purple", "Brown", "Pink", "Cream", "Orange"]
    if user == ctx.message.author:
        embed2 = discord.Embed(title="You should know your own skin color", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed2)
    else:
        embed = discord.Embed(color=0xcb287a)
        embed.add_field(name=f"{user.name}'s skin color", value=random.choice(skins))
        await client.say(embed=embed)
	
@client.command(pass_context=True)
async def slap(ctx, user: discord.Member = None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["http://rs20.pbsrc.com/albums/b217/strangething/flurry-of-blows.gif?w=280&h=210&fit=crop", "https://media.giphy.com/media/LB1kIoSRFTC2Q/giphy.gif", "https://i.imgur.com/4MQkDKm.gif"]
    if user == None:
        await client.say(f"{ctx.message.author.mention} ```Proper usage is\n\n>slap <mention a user>```")
    else:
        embed = discord.Embed(title=f"{ctx.message.author.name} Just slapped the shit out of {user.name}!", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url=random.choice(gifs))
        await client.say(embed=embed)

@client.command(pass_context=True)
async def damn(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(title="DAMNNNNNNNN!!", color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="http://i.imgur.com/OKMogWM.gif")
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def burned(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url="https://i.imgur.com/wY4xbak.gif")
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def savage(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["https://media.giphy.com/media/s7eezS6vxhACk/giphy.gif", "https://m.popkey.co/5bd499/gK00J_s-200x150.gif",
            "https://i.imgur.com/XILk4Xv.gif"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url=random.choice(gifs))
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def thuglife(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    gifs = ["https://media.giphy.com/media/kU1qORlDWErOU/giphy.gif", "https://media.giphy.com/media/EFf8O7znQ6zRK/giphy.gif",
            "https://i.imgur.com/XILk4Xv.gif", "http://www.goodbooksandgoodwine.com/wp-content/uploads/2011/11/make-it-rain-guys.gif"]
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_image(url=random.choice(gifs))
    await client.say(embed=embed)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
async def membernames(ctx):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    try:
        embed = discord.Embed(description="\n".join([member.name for member in ctx.message.server.members]), color=0x0093ff)
        await client.send_message(ctx.message.author, embed=embed)
    except:
        embed = discord.Embed(title="There are too many members that the bot cannot list it down", color = discord.Color((r << 16) + (g << 8) + b))
        await client.say(embed=embed)

@client.command(pass_context = True)
async def memes(ctx):
    colour = '0x' + '008000'
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed = discord.Embed(title='<A meme is quite simply a concept, behavior, or idea that spreads, usually via the internet.> <Create by Biswajit>', description='from reddit', color=discord.Color(int(colour, base=16)))
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)
		
@client.command(pass_context=True)
async def lovedetect(ctx, user: discord.Member = None, *, user2: discord.Member = None):
    shipuser1 = user.name
    shipuser2 = user2.name
    useravatar1 = user.avatar_url
    useravatar2s = user2.avatar_url
    self_length = len(user.name)
    first_length = round(self_length / 2)
    first_half = user.name[0:first_length]
    usr_length = len(user2.name)
    second_length = round(usr_length / 2)
    second_half = user2.name[second_length:]
    finalName = first_half + second_half
    score = random.randint(0, 100)
    filled_progbar = round(score / 100 * 10)
    counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)
    url = f"https://nekobot.xyz/api/imagegen?type=ship&user1={useravatar1}&user2={useravatar2s}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(title=f"{shipuser1} ❤ {shipuser2} Love each others", description=f"Love\n`{counter_}` Score:**{score}% **\nLoveName:**{finalName}**", color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            await client.say(embed=embed)

@client.command(pass_context=True)
async def virus(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await client.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))
    await asyncio.sleep(1)
    x = await client.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
    await asyncio.sleep(2)
    x = await client.edit_message(x,'``Injecting virus.   |``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus..  /``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus... -``')
    await asyncio.sleep(0.5)
    x = await client.edit_message(x,'``Injecting virus....\``')
    await client.delete_message(x)
    await client.delete_message(ctx.message)

    if user:
        await client.say('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
        await client.send_message(user,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
    else:
        await client.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await client.send_message(name,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
	
@client.command(pass_context = True)
async def invites(ctx,*,user:discord.Member=None):
    invite = await client.invites_from(ctx.message.server)
    if user is None:
        for invite in invite:
          if invite.inviter == ctx.message.author:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await client.say(embed=embed)

    else:
        for invite in invite:
          if invite.inviter == user:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await client.say(embed=embed)
		
@client.group(pass_context=True, invoke_without_command=True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member=None, *, nickname=None):
    member = user.name
    if user is None:
      await client.say('Please tag a person to change nickname. Example- ``^setnick @user/all <new nickname>``')
      return
    else:
      await client.change_nickname(user, nickname)
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-lr-log-☆☆╮':
            embed=discord.Embed(title="Changed Nickname of User!", description="**{0}** nickname was changed by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
            await client.send_message(channel, embed=embed)

@setnick.command(pass_context=True)
@commands.has_permissions(administrator=True)     
async def all(ctx,*,nickname:str=None):
    if nickname is None:
      await client.say('Please use this command like:``^setnick all <new nickname>``')
      return
    else: 
      for user in ctx.message.server.members:
        try:
          new_nick = nickname + user.name
          await asyncio.sleep(1)
          await client.change_nickname(user, new_nick)
          state = 'add'
        except:
          pass	
      if state == 'add':
        await client.say(f'Setted up nickname of everyone to ``{nickname} + username``')
        return
      else:
        pass


@client.group(pass_context=True, invoke_without_command=True)
@commands.has_permissions(manage_nicknames=True)     
async def resetnick(ctx, user: discord.Member=None):
    member = user.name
    if user is None:
      await client.say('Please tag a person to reset nickname. Example- ``^resetnick @user/all``')
      return
    else:
      nick = user.name
      await client.change_nickname(user, nick)
      await client.delete_message(ctx.message)
      for channel in user.server.channels:
        if channel.name == '╰☆☆-lr-log-☆☆╮':
            embed=discord.Embed(title="Reset Nickname of User!", description="**{0}** nickname was reset by **{1}**!".format(member, ctx.message.author), color=0x0521F6)
            await client.send_message(channel, embed=embed)

@resetnick.command(pass_context=True)
@commands.has_permissions(administrator=True)     
async def all(ctx):
    for user in ctx.message.server.members:
      try:
        await asyncio.sleep(1)
        nick = user.name
        await client.change_nickname(user, nick)
        state = 'done'
      except:
        pass	
    if state == 'done':
      await client.say('Resetted all nicknames')
    else:
      pass
		
		
@client.command(pass_context = True)
async def detailedinvites(ctx,*,user:discord.Member=None):
    invite = await client.invites_from(ctx.message.server)
    if user is None:
        for invite in invite:
          if invite.inviter == ctx.message.author:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await client.say(embed=embed)
    else:
        for invite in invite:
          if invite.inviter == user:
              r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
              embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
              embed.add_field(name = 'Link used for inviting:',value =f'{invite.url}'.format(), inline=False)
              embed.add_field(name = 'Invites from this link:',value =f'{invite.uses}', inline=False)
              embed.add_field(name = 'Created at:',value =f'{invite.created_at}', inline=False)
              embed.add_field(name = 'Channel:',value =f'{invite.channel}', inline=False)
              embed.add_field(name = 'ID:',value =f'{invite.id}', inline=False)
              await client.say(embed=embed)
				
@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, role:str=None):
    user = ctx.message.author
    if discord.utils.get(user.server.roles, name="{}".format(role)) is None:
        await client.create_role(user.server, name="{}".format(role), permissions=discord.Permissions.none())
        await client.say("{} role has been added.".format(role))
        return
    else:
        await client.say("{} role is already exists".format(role))
	
@client.command(pass_context=True)
async def merrychristmas(ctx, user:discord.Member=None):
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    if user is None:
        embed=discord.Embed(title='Merry Christmas', description=f'I wanna wish {ctx.message.author} Merry Christmas {ctx.message.author}', color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/486489391083159574/526968559994404874/gif-153062737.gif')
        await client.say(embed=embed)
    else:
        embed=discord.Embed(title='Merry Christmas', description=f'I wanna wish {user} Merry Christmas {user}', color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_image(url = 'https://cdn.discordapp.com/attachments/486489391083159574/526968559994404874/gif-153062737.gif')

@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def roleinfo(ctx,*, role:discord.Role=None):
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("No such role found")
        return
    else:
        r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
        embed = discord.Embed(title="{}'s info".format(role.name), description="Here's what I could find.", color = discord.Color((r << 16) + (g << 8) + b))
        embed.set_thumbnail(url = ctx.message.server.icon_url)
        embed.add_field(name="Name", value=role.name, inline=True)
        embed.add_field(name="ID", value=role.id, inline=True)
        embed.add_field(name="Color", value=role.color)
        embed.add_field(name="Created", value=role.created_at.strftime("%d %b %Y %H:%M"))
        await client.say(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(manage_roles=True)
async def delrole(ctx,*, role: discord.Role = None):
    user = ctx.message.author
    if discord.utils.get(ctx.message.server.roles, name="{}".format(role)) is None:
        await client.say("There is no role with this name in this server")
    else:
        await client.delete_role(ctx.message.server, role)
        await client.say(f"{role} role has been deleted")
	
@client.command(pass_context=True)
async def remind(ctx, time=None, *,remind=None):
    time =int(time)
    time = time * 60
    output = time/60
    await client.say("I will remind {} after {} minutes for {}".format(ctx.message.author.name, output, remind))
    await asyncio.sleep(time)
    await client.say("Reminder: {} by {}".format(remind, ctx.message.author.mention))
    await client.send_message(ctx.message.author, "Reminder: {}".format(remind))

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def norole(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to warn")
    else: await client.say(msg + ', Please Do not ask for promotions check Rules again.')
    return

@client.command(pass_context = True)
async def happybirthday(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to wish")
    await client.say('Happy birthday ' + msg + ' \nhttps://asset.holidaycardsapp.com/assets/card/b_day399-22d0564f899cecd0375ba593a891e1b9.png')
    return


@client.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def english(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user to warn")
    else: await client.say(msg + ', Please do not use language other than **English.**')
    return


@client.command(pass_context = True) 
async def htmltutorial(ctx, *, msg = None):
    await client.delete_message(ctx.message)
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify a user")
    else: await client.say('Welcome' + msg +  ', Please check http://uksoft.000webhostapp.com/Programming-Tutorials/index.html')
    return
   
@client.command(pass_context = True)
async def github(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Please specify respo. ``Format- https://github.com/biswajit9123/blackfox``")
    else: await client.say('https://github.com/' + msg)
    return

@client.command(pass_context = True)
async def reactionroles(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("Check this video to setup YAGPDB BOT- https://youtu.be/nQOJmmKc8Pk")
    else: await client.say('Check this video to setup YAGPDB BOT- https://youtu.be/nQOJmmKc8Pk ' + msg)
    return

@client.command(pass_context = True)
async def invite(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.say("Thanks for adding our bot.")
      embed=discord.Embed(title="Click on this link to invite:", description="https://discordapp.com/api/oauth2/authorize?client_id=519200090770898945&permissions=8&scope=bot" , color=0x00fd1b)
      await client.say(embed=embed)

@client.command(pass_context = True)
async def authlink(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.say("Thanks for adding our bot.")
      embed=discord.Embed(title="Click on this link to invite:", description="https://discord.gg/W88r3W8" , color=0x00fd1b)
      await client.say(embed=embed)

@client.command(pass_context = True)
async def bottutorial(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("You can check https://github.com/biswajit9123/Blackfox-9476 for more information")
    else: await client.say('https://github.com/biswajit9123/discord.py-tutorial/' + msg + '.py')
    return

@client.command(pass_context = True)
async def dyno(ctx, *, msg = None):
    if '@here' in msg or '@everyone' in msg:
      return
    if not msg: await client.say("You can check  for more information")
    else: await client.say('https://github.com/biswajit9123/Noob/blob/master/' + msg)
    return

@client.command(pass_context=True)
async def unverify(ctx):
    await client.delete_message(ctx.message)
    role = discord.utils.get(ctx.message.server.roles, name='Unverified')
    await client.add_roles(ctx.message.author, role)
    
@client.command(pass_context=True)
async def verify(ctx):
    if ctx.message.author.bot:
      return
    else:
      await client.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Verified')
      await client.add_roles(ctx.message.author, role)

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def lock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=False, read_messages=True)
    if not channelname:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await client.say("Channel locked by: {}".format(ctx.message.author))
    else:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(channelname, role, overwrite)
        await client.say("Channel locked by: {}".format(ctx.message.author))

@client.command(pass_context = True)
@commands.has_permissions(kick_members=True) 
async def unlock(ctx, channelname: discord.Channel=None):
    overwrite = discord.PermissionOverwrite(send_messages=None, read_messages=True)
    if not channelname:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(ctx.message.channel, role, overwrite)
        await client.say("Channel unlocked by: {}".format(ctx.message.author))
    else:
        role = discord.utils.get(ctx.message.server.roles, name='@everyone')
        await client.edit_channel_permissions(channelname, role, overwrite)
        await client.say("Channel unlocked by: {}".format(ctx.message.author))

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def friend(ctx, user:discord.Member,):
    if ctx.message.author.bot:
      return
    else:
      await client.delete_message(ctx.message)
      role = discord.utils.get(ctx.message.server.roles, name='Friend of Owner')
      await client.add_roles(ctx.message.mentions[0], role)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def makemod(ctx, user: discord.Member):
    nickname = '♏' + user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.add_roles(user, role)
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Congratulations Message')
    embed.add_field(name = '__Congratulations__',value ='**Congratulations for mod.Hope you will be more active here. Thanks for your help and support.**',inline = False)
    embed.set_image(url = 'https://preview.ibb.co/i1izTz/ezgif_5_e20b665628.gif')
    await client.send_message(user,embed=embed)
    await client.delete_message(ctx.message)
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)     
async def removemod(ctx, user: discord.Member):
    nickname = user.name
    await client.change_nickname(user, nickname=nickname)
    role = discord.utils.get(ctx.message.server.roles, name='Moderator')
    await client.remove_roles(user, role)
    await client.delete_message(ctx.message)

@client.command(pass_context = True)
async def botwarncode(ctx):
    await client.say('https://hastebin.com/ibogudoxot.py')
    return

@client.command(pass_context=True)
async def guess(ctx, number):
    try:
        arg = random.randint(1, 10)
    except ValueError:
        await client.say("Invalid number")
    else:
        await client.say('The correct answer is ' + str(arg))

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True) 
async def roles(context):
	"""Displays all of the roles with their ids"""
	roles = context.message.server.roles
	result = "The roles are "
	for role in roles:
		result += '``' + role.name + '``' + ": " + '``' + role.id + '``' + "\n "
	await client.say(result)
    
@client.command(pass_context=True, aliases=['server'])
@commands.has_permissions(kick_members=True)
async def membercount(ctx, *args):
    """
    Shows stats and information about current guild.
    ATTENTION: Please only use this on your own guilds or with explicit
    permissions of the guilds administrators!
    """
    if ctx.message.channel.is_private:
        await bot.delete_message(ctx.message)
        return

    g = ctx.message.server

    gid = g.id
    membs = str(len(g.members))
    membs_on = str(len([m for m in g.members if not m.status == Status.offline]))
    users = str(len([m for m in g.members if not m.bot]))
    users_on = str(len([m for m in g.members if not m.bot and not m.status == Status.offline]))
    bots = str(len([m for m in g.members if m.bot]))
    bots_on = str(len([m for m in g.members if m.bot and not m.status == Status.offline]))
    created = str(g.created_at)
    
    em = Embed(title="Membercount")
    em.description =    "```\n" \
                        "Members:   %s (%s)\n" \
                        "  Users:   %s (%s)\n" \
                        "  Bots:    %s (%s)\n" \
                        "Created:   %s\n" \
                        "```" % (membs, membs_on, users, users_on, bots, bots_on, created)

    await client.send_message(ctx.message.channel, embed=em)
    await client.delete_message(ctx.message)

@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def embed(ctx, *args):
    if ctx.message.author.bot:
      return
    else:
      argstr = " ".join(args)
      r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
      text = argstr
      color = discord.Color((r << 16) + (g << 8) + b)
      await client.send_message(ctx.message.channel, embed=Embed(color = color, description=text))
      await client.delete_message(ctx.message)    

client.run(os.getenv('Token'))
