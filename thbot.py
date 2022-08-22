#!/usr/bin/python3
from asyncio import sleep
import os, random, discord, sys, time
from importlib.abc import TraversableResources
from click import pass_context
from turtle import color, title
from unicodedata import name
from dotenv import load_dotenv
from urllib.request import urlopen, Request
# from discord.ext.commands import bot
from discord.ext import commands
# from discord_ui import Button
 
def main(argv):
    intents=discord.Intents.all()
    intents.members = True
    #intents.message_content = True
    #bot = discord.bot(intents=discord.Intents.default())
    #intents = discord.Intents().all()
    print("bot loading")
    #client = discord.Client()
    bot = commands.Bot(command_prefix='t!',intents=intents,description="")
    bot.remove_command('help')
    load_dotenv()
    #token = os.getenv()
    token = None
    if token == None:
        token = argv[0]
    else:
        raise("Token does not work or is missing!")


    print("DO NOT PUBLISH PUBLICLY: " + token)




    @bot.event
    async def on_ready():
        status=["wit dey worm", "with twitch source code", "Skate 3", "theroy.tech", "im here for cs club", "with finkey 🥺", "clash royale", "with java" ]
        rstatus = random.choice(status)
        print("bot loading complete")
        await bot.change_presence(activity=discord.Game( rstatus +' | t!help in ' + str(len(bot.guilds)) + ' servers.'), status=discord.Status.idle)

    @bot.event
    async def on_message(message):
        #print(message.content.lower())
        if message.author == bot.user or message.author.bot:
            return
        ctx = await bot.get_context(message)
        if ctx.valid and "t!" in message.content.lower():
            await bot.process_commands(message)
        elif message.content.lower().startswith("t!"):
            print("{} Command not found".format(message.content.lower()))
            await message.channel.send("{} is not a command".format(message.content.lower()))
        else:
            '''This will make it so it does not read every message as a 
            command unless it contains t! which could still exist in some 
            case and we should be very careful with this because something 
            like "I love tater tot!" will trigger this lol
            '''
            pass



    @bot.command()
    async def help(ctx):
            color = [0xff0000, 0xff4d00, 0xfcca03, 0x37ff00, 0x0059ff, 0xa200ff]
            rcolor = random.choice(color)
            
            info = discord.Embed(title="Commands list:",  description="All existing commands", color=rcolor)
            info.add_field(name=":star_struck:`t!inspiration`", value="makes you go :O", inline=False)
            info.add_field(name=":1234:`t!randommath`", value="random math. adds numbers -45000-45000", inline=True)
            info.add_field(name=":ping_pong:`t!ping`", value=":exploding_head:", inline=False)
            info.add_field(name=":receipt:`t!userinfo`", value="User information about yourself (Pinging others does not bring up theirs sadly).", inline=False)
            info.add_field(name=":signal_strength:`t!serverinfo`", value="Server information :exploding_head:", inline=False)
            info.set_footer(text='Sumbit ideas and issues @ https://github.com/zTheroy/theroy-discord-bot/issues')
            await ctx.send(embed=info, mention_author=False)
            #await ctx.send("test")

        #---------Random math command. May remove at a later date---------#
    @bot.command()
    async def randommath(ctx, user:discord.Member, *, message=None):
        lst = ['+', '-', '*', '/']
        math_embed = discord.Embed(title="math", description="math answer", color=0x11d43b)
        x = random.randint(-45000,45000)
        y = random.randint(-45000,45000)
        random_operator=random.randint(0,len(lst)-1)
        if lst[random_operator] == '+':
            answer = x + y
            math_output = '{} + {} = {}'.format(x,y,answer)
        elif lst[random_operator] == '-':
            answer = x - y
            math_output = '{} - {} = {}'.format(x,y,answer)
        elif lst[random_operator] == '*':
            answer = x * y
            math_output = '{} * {} = {}'.format(x,y,answer)
        elif lst[random_operator] == '/':
            answer = x / y
            math_output = '{} / {} = {}'.format(x,y,answer)
        elif x < 0 and y < 0 and lst[random_operator] == '-':
            y = abs(y)
            answer = x + y
            math_output = '{} + {} = {}'.format(x,y,answer)
            print(y)
        math_embed.add_field(name="oh my god its your math answer", value=math_output, inline=False)
        await ctx.send(embed=math_embed)

    @bot.command()
    async def inspiration(ctx, *, message=None):
        'Inspirational quotes command; honestly not sure how it works'
        random_quote = Request('https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?', headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(random_quote)
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        #print(html)
        html = html.split(":")
        inspiration = html[1].split("quoteAuthor")
        inspiration = inspiration[0]
        inspiration = inspiration[:-3]
        await ctx.send(inspiration)
    @bot.command()
    async def ping(ctx, *, message=None):
        'ping command to pong the ping'
        start = time.time()
        latency = message.channel.created_at
        end = time.time()
        execution_time = end - start
        #embedding execution time and latency under
        ping_title = discord.Embed(title="pong :ping_pong:",color=0x005ef5)
        ping_title.add_field(name="Execution Time", value=(f"{execution_time} seconds"), inline=False)
        ping_title.add_field(name="Latency", value=str(round(bot.latency*1000))+" ms", inline=False)
        await ctx.send(embed=ping_title)







#require global vars username gname etc.
        #---------User Information Command---------#
    @bot.command()
    async def userinfo(ctx, user:discord.Member= None, *, message=None):
        #print(user)
        #print(ctx.message.author.avatar.url)
        if user != None:
            create = user.created_at
            is_bot = user.bot
            info = discord.Embed(title="",  description="", color=0x481c70)
            info.set_author(name=str(user), icon_url=user.avatar.url)
            info.add_field(name="User ID :performing_arts:", value="*" + str(user.id) + "*")
            info.add_field(name="Username :name_badge:", value="*" + str(user).split('#')[0] + "*",  inline=False)
            info.add_field(name="Bot :robot:", value="*" + str(is_bot) + "*")
            info.add_field(name="Discriminator :hash:", value="*" + ctx.author.discriminator + "*", inline=False)
            info.set_footer(text="Profile creation: " + create.strftime("%Y-%m-%d, %H:%M:%S"))
            await ctx.reply(embed=info, mention_author = False)
        else:
            await ctx.reply("User not entered or found", mention_author=True)



        #---------Server Information Command---------#
        #server.add_field(name="", value=, inline=True)
    @bot.command()
    async def serverinfo(message):
        server = discord.Embed(title="", description="", color=0x3c8009)
        server.set_author(name=gname, icon_url=gavatar)
        server.add_field(name="Owner :judge:", value=owner, inline=True)
        server.add_field(name="2FA Required " + gemoji , value=str(gmfa), inline=True)
        server.add_field(name="Channels :speech_balloon:", value=gchannels, inline=True)
        server.add_field(name="Emojis " + remojilist, value=str(len(emoji)), inline=True)
        server.add_field(name="Members " + memoji, value=str(members), inline=True)
        server.set_footer(text="ID: " + str(gid) + " | Server Creation: " + gcreate.strftime("%Y-%m-%d %H:%M:%S"))
        await ctx.send(embed=server)

        #---------Spotify Command LOL!---------#
    @bot.command()
    async def spotify(ctx, user:discord.Member, *, message=None):
        spit = discord.Embed(title="", value="", color=0x189bcc)
        spit.set_author(name=str(user) + "#" + disc, icon_url=avatar)
        spit.add_field(name="Album", value=album, inline=True)
        spit.add_field(name="Duration", value=stime, inline=True)
        spit.add_field(name="Artist", value=str(art), inline=True)
        spit.set_footer(text="Track ID: " + str(sid))
        await ctx.send(embed=spit)

    bot.run(token)





if __name__ == "__main__":
    main(sys.argv[1:])