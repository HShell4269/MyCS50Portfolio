import discord
from discord.ext import commands
import random
import asyncio
import youtube_dl

Token = 'MTAxODc2MDQyMTIwNjkyOTQwOA.GO9iip.sAoSub4vl3IatW7KFBRGWbwswWm4OmyHjz6PL4'

bot = commands.Bot(command_prefix = '?', intents = discord.Intents.all(), case_insensitive = True)
bot.remove_command("help")

Banned_words = {"http://", "https://", ".com", ".net"}

player = {}

voice_clients = {}

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', }

yt_dl_opts = {'format': 'bestaudio/best'}
ytdl = youtube_dl.YoutubeDL(yt_dl_opts)

ffmpeg_options = {'options': "-vn"}

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    print("Hbot is now online")

#Welcome Message for new members
@bot.event
async def on_member_join(ctx):
    guild = bot.get_guild(917611889549262858) # YOUR INTEGER GUILD ID HERE
    welcome_channel = guild.get_channel(1040905926514855979) # YOUR INTEGER CHANNEL ID HERE
    await welcome_channel.send(f'Welcome to the {guild.name}, {ctx.mention} !  :partying_face:')
    await ctx.send(f'We are glad to have you in the {guild.name} Discord Server, {ctx.name} !  :partying_face:. I am Hbot, created by Honor Shelby!')


#Message Chat Reponses
@bot.listen('on_message')
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    
    if message.author == bot.user:
        return
    
    if message.channel.name == 'hbot':
        if user_message.lower() == 'hello':
            await message.channel.send(f"Hello {username}!")
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f"Goodbye {username}, see you later!")
            return
        elif user_message.lower() == 'cool':
            await message.channel.send(f"Awesome right?")
            return
        elif user_message.lower() == 'awesome':
            await message.channel.send(f"I know, I know")
            return
        elif user_message.lower() == 'random number':
            response = f"This is your random number: {random.randrange(100000)}"
            await message.channel.send(response)
            return

@bot.command()
async def Hey(ctx):
    await ctx.send(f"Hey there to you {ctx.author.mention}!")
    
@bot.command()
async def CS50(ctx):
    await ctx.send(f"that ends it with myself... and this was CS50 Final Project.")

@bot.command()
async def mcipher(ctx,*,message):
    Morse = " ".join(MORSE_CODE_DICT[c] for c in message.upper())
    embed = discord.Embed(title=f"Encrypted Morse Code", description=Morse, color=0x9208ea)
    await ctx.send(embed=embed)
    
@bot.command()
async def mdecipher(ctx,*,message):
    decipher = ''
    citext = ''
    for letter in message:
        if (letter != ' '):
 
            i = 0
 
            citext += letter
 
        else:
            i += 1
 
            if i == 2:
 
                decipher += ' '
            else:
 
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(citext)]
                citext = ''
 
    embed = discord.Embed(title=f"Decrypted Morse Code", description=decipher, color=0x9208ea)
    await ctx.send(embed=embed)

##Caesar Encryption Message
    
##Create Help options and descriptions
@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", description = "Usage ?help <command> for more information.")
    
    em.add_field(name = "Moderation", value = "'kick', 'ban', 'unban'")
    em.add_field(name = "Music-Player", value = "'con', 'play', 'loop', 'pause', 'queue', 'resume', 'stop'")
    em.add_field(name = "Opinions", value = "'poll1','poll2'")
    em.add_field(name = "Utilities", value = "'mcipher', 'mdecipher'")
    
    await ctx.send(embed = em)

##Moderation
@help.command()
async def kick(ctx):
    
    em = discord.Embed(title = "Moderation", description = "Kicks member from the guild with proper reason.", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?kick <member> [reason]")
    
    await ctx.send(embed=em)
    
@help.command()
async def ban(ctx):
    
    em = discord.Embed(title = "Moderation", description = "Bans member from the guild with proper reason.", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?ban <member> [reason]")
    
    await ctx.send(embed=em)

@help.command()
async def unban(ctx):
    
    em = discord.Embed(title = "Moderation", description = "Unbans member from the guild", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?unban <member>")

    await ctx.send(embed=em)
    
##Music-player
@help.command()
async def con(ctx):
    em = discord.Embed(title = "Music", description = "Connects bot to where the user is in a Voice Chat", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?con")

    await ctx.send(embed=em)
    
@help.command()
async def play(ctx):
    em = discord.Embed(title = "Music", description = "Plays or queues a music for listeners in the Voice Chat", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?play <Title of the Music>")

    await ctx.send(embed=em)
    
@help.command()
async def p(ctx):
    em = discord.Embed(title = "Music", description = "Same as the play command only difference is it can play songs from a link in YouTube because Nathan is too lazy to fix it.", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?p <YouTube link of Music>")

    await ctx.send(embed=em)
    
@help.command()
async def loop(ctx):
    em = discord.Embed(title = "Music", description = "Loops current music being played", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?loop")

    await ctx.send(embed=em)
    
@help.command()
async def pause(ctx):
    em = discord.Embed(title = "Music", description = "Pauses current music being played", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?pause")

    await ctx.send(embed=em)
    
@help.command()
async def queue(ctx):
    em = discord.Embed(title = "Music", description = "Checks songs in queue", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?play <Title of the Music>")

    await ctx.send(embed=em)
    
@help.command()
async def resume(ctx):
    em = discord.Embed(title = "Music", description = "Resumes paused music", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?resume")

    await ctx.send(embed=em)
    
@help.command()
async def stop(ctx):
    em = discord.Embed(title = "Music", description = "Stops current music session and disconnect from Voice Channel", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?stop")

    await ctx.send(embed=em)

##Opinions
@help.command()
async def poll1(ctx):
    
    em = discord.Embed(title = "Opinions", description = "Create 2 option poll for people to vote.", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?poll2 'Question that has 2 options to answer with.'")
    
    await ctx.send(embed=em)

@help.command()    
async def poll2(ctx):
    
    em = discord.Embed(title = "Opinions", description = "Create a yes or no poll for people to vote.", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?poll1 'Yes or No Question to Answer'")
    
    await ctx.send(embed=em)

##Utilities
@help.command()    
async def mdecipher(ctx):
    
    em = discord.Embed(title = "Secret Messaging", description = "Deciphers a morse code text to something understandable. (Preferably use this command as a DM to the bot itself for privacy reasons)", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?mdecipher <Message Text>")
    
    await ctx.send(embed=em)

@help.command()    
async def mcipher(ctx):
    
    em = discord.Embed(title = "Secret Messaging", description = "Enciphers a normal text to a morse code dictionary. (Preferably use this command as a DM to the bot itself for privacy reasons)", color = ctx.author.color)
    
    em.add_field(name = "**Syntax**", value = "?mcipher <Message Text>")
    
    await ctx.send(embed=em)

@bot.command()
async def poll1(ctx,*,message):
    embed = discord.Embed(title=f"Poll by {ctx.author}", description=message, color=0x9208ea)
    embed.set_footer(text=f"Created by {ctx.author}")
    react_message = await ctx.send(embed=embed)
    await react_message.add_reaction("👍")
    await react_message.add_reaction("👎")
    
@bot.command()
async def poll2(ctx,*,message):
    embed = discord.Embed(title=f"Poll by {ctx.author}", description=message, color=0x9208ea)
    embed.set_footer(text=f"Created by {ctx.author}")
    react_message = await ctx.send(embed=embed)
    await react_message.add_reaction("1️⃣")
    await react_message.add_reaction("2️⃣")

@bot.listen('on_message')
async def on_message(msg):
    if msg.content.startswith("?p"):

        try:
            voice_client = await msg.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except:
            print("error")

        try:
            url = msg.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options, executable="C:\\ffmpeg\\bin\\ffmpeg.exe")

            voice_clients[msg.guild.id].play(player)

        except Exception as err:
            print(err)


    if msg.content.startswith("?pause"):
        try:
            voice_clients[msg.guild.id].pause()
        except Exception as err:
            print(err)

    # This resumes the current song playing if it's been paused
    if msg.content.startswith("?res"):
        try:
            voice_clients[msg.guild.id].resume()
        except Exception as err:
            print(err)

    # This stops the current playing song
    if msg.content.startswith("?st"):
        try:
            voice_clients[msg.guild.id].stop()
            await voice_clients[msg.guild.id].disconnect()
        except Exception as err:
            print(err)

##Ban and Kick Members (Moderation)
@commands.has_permissions(kick_members=True)
@bot.command()
async def kick(ctx, user: discord.Member=None, *, reason="No reason Provided YEET!!"):
    if user is None:
        embed = discord.Embed(color=0x1c1c1c, title="No member found", description="Please specify vict- I mean user to kick.")
        await ctx.send(embed=embed)
    elif user == ctx.message.author:
        embed = discord.Embed(color=0x1c1c1c, title="You can't kick yourself", description="Please choose another person that is not yourself.")
        await ctx.send(embed=embed)
    elif user.guild_permissions.administrator:
        embed = discord.Embed(color=0x1c1c1c, title="No Kicking of Admins", description="You cannot kick the people managing this Server.")
        await ctx.send(embed=embed)
    else:
        DMembed = discord.Embed(color=0x1c1c1c, title=f"You have been Kicked from {user.guild.name}", description=f"Kicked for Reason/s: **{reason}**\n Kicked by: {ctx.author.name}")
        await user.send(embed=DMembed)
        
        await user.kick(reason=reason)
        embed = discord.Embed(color=0x1c1c1c, title=f"Kicked {user}", description=f"{user.mention} has been kicked for {reason} by {ctx.author.mention}")
        await ctx.send(embed=embed)

@commands.has_permissions(ban_members=True)
@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member=None, *, reason="No reason Provided YEET!!"):
    if user is None:
        embed = discord.Embed(color=0x1c1c1c, title="No member found", description="Please specify vict- I mean user to kick.")
        await ctx.send(embed=embed)
    elif user == ctx.message.author:
        embed = discord.Embed(color=0x1c1c1c, title="You can't ban yourself", description="Please choose another person that is not yourself.")
        await ctx.send(embed=embed)
    elif user.guild_permissions.administrator:
        embed = discord.Embed(color=0x1c1c1c, title="No Banning of Admins", description="You cannot ban the people managing this Server.")
        await ctx.send(embed=embed)
    else:
        DMembed = discord.Embed(color=0x1c1c1c, title=f"You have been Banned from {user.guild.name}", description=f"Banned for Reason/s: **{reason}**\n Banned by: {ctx.author.name}")
        await user.send(embed=DMembed)
        
        await user.ban(reason=reason)
        embed = discord.Embed(color=0x1c1c1c, title=f"Banned {user}", description=f"{user.mention} has been banned for {reason} by {ctx.author.mention}")
        await ctx.send(embed=embed)
        
@commands.has_permissions(ban_members=True)
@bot.command()
async def unban(ctx, id: int = None):
    if id is None:
        embed = discord.Embed(color=0x1c1c1c, title=f"No member found", description=f"Please specify User ID in the banned area section")
        await ctx.send(embed=embed)
    else:
        user = await bot.fetch_user(id)
        await ctx.guild.unban(user)
        embed = discord.Embed(color=0x1c1c1c, title=f"Unbanned {user}", description=f"{user.name} has been unbanned by {ctx.author.mention}")
        await ctx.send(embed=embed)

##Censorship
@bot.listen('on_message')
async def on_message(msg):
    
    if msg.author != bot.user:
        for text in Banned_words:
            if "Moderator" not in str(msg.author.roles) and text in str(msg.content.lower()):
                await msg.delete()
                return
            
async def setup(bot):
    await bot.load_extension('dismusic')

bot.run(Token)
