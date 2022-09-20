#!/usr/bin/python3
from asyncio import sleep
import os, random, discord, sys, time, minestat, itertools, threading, asyncio
from importlib.abc import TraversableResources
from click import pass_context
from unicodedata import name
from dotenv import load_dotenv
from urllib.request import urlopen, Request
# from discord.ext.commands import bot
from discord.ext import commands
 
def main(argv):
    intents=discord.Intents.all()
    intents.members = True
    #intents.message_content = True
    #bot = discord.bot(intents=discord.Intents.default())
    #intents = discord.Intents().all()
    print("Bot loading...")
    
    animation = ["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    for i in range(len(animation)):
        time.sleep(0.05)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()

    #client = discord.Client()
    bot = commands.Bot(command_prefix='t!',intents=intents,description="")
    bot.remove_command('help')
    if len(argv) < 1:
        try:
            load_dotenv()
            token = os.getenv('TOKEN')
        except:
            raise Exception(".env file not present please check .env or pass token via the command line")
    elif len(argv[0]) > 0:
        token = argv[0]
    else:
        raise("Token does not work or is missing!")

    print("\nToken: " + token)

    @bot.event
    async def on_ready():
        status=["wit dey worm", "with twitch source code", "Skate 3", "theroy.tech", "im here for cs club", "with finkey 🥺", "clash royale", "with java", "with theroy's head", "Minecraft - 20 Years Elapsed", "gorillaz spotify", "Google Chrome", "Dead Cells", "Fortnite (<--- FUNNY JOKE)" ]
        rstatus = random.choice(status)
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
            info.set_footer(text='Sumbit ideas and issues @ https://github.com/Turqww/theroy-discord-bot/issues')
            await ctx.send(embed=info, mention_author=False)
            #await ctx.send("test")

        #---------Random math command. May remove at a later date---------#
    @bot.command()
    async def randommath(ctx, *, message=None):
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
        latency = ctx.channel.created_at
        end = time.time()
        execution_time = end - start
        #embedding execution time and latency under
        ping_title = discord.Embed(title="pong :ping_pong:",color=0x005ef5)
        ping_title.add_field(name="Execution Time", value=(f"{execution_time} seconds"), inline=False)
        ping_title.add_field(name="Latency", value=str(round(bot.latency*1000))+" ms", inline=False)
        await ctx.send(embed=ping_title)


    #require global vars username gname etc.
    @bot.command()
    async def userinfo(ctx, user:discord.Member=None):
        #print(user)\\
        #print(ctx.message.author.avatar.url
        if user != None:
            info = discord.Embed(title="",  description="", color=0x481c70)
            info.set_thumbnail(url=user.avatar_url)
            info.set_author(name=user.name, icon_url=user.avatar_url)
            info.add_field(name="Information", value="**:id: User ID: ** " + str(user.id) + "\n **:robot: Bot:** ***" + str(user.bot) + "***" + "\n **:hash: Discriminator: **" + user.discriminator, inline=False)
            info.add_field(name="Roles")
            info.set_footer(text="Profile creation: " + user.created_at.strftime("%Y-%m-%d, %H:%M:%S") + " | Requested by: " + ctx.author.name )
            await ctx.reply(embed=info, mention_author = False)
        else:
            info = discord.Embed(title="",  description="", color=0x481c70)
            info.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            info.add_field(name=":id:User ID", value="*" + str(ctx.author.id) + "*")
            info.add_field(name=":name_badge:Username", value="*" + str(ctx.author.name).split('#')[0] + "*",  inline=False)
            info.add_field(name=":robot:Bot", value="*" + str(ctx.author.bot) + "*")
            info.add_field(name="Discriminator :hash:", value="*" + ctx.author.discriminator + "*", inline=False)
            info.set_footer(text="Profile creation: " + ctx.author.created_at.strftime("%Y-%m-%d, %H:%M:%S") + " | Requested by: " + ctx.author.name )
            await ctx.reply(embed=info, mention_author = False)
             



        #---------Server Information Command---------#
    @bot.command()
    async def serverinfo(ctx):
        server = discord.Embed(title="", description="", color=0x3c8009)
        server.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon_url)
        server.add_field(name="Owner :judge:", value=ctx.guild.owner, inline=True)
        # server.add_field(name="2FA Required ", value=str(gmfa), inline=True)
        server.add_field(name="Channels :speech_balloon:", value=str(len(ctx.guild.text_channels)), inline=True)
        server.add_field(name="Emojis ", value=str(len(ctx.guild.emojis)), inline=True)
        server.add_field(name="Members ", value=str(len(ctx.guild.members)), inline=True)
        server.set_footer(text="ID: " + str(ctx.guild.id) + " | Server Creation: " + ctx.guild.created_at.strftime("%Y-%m-%d %H:%M:%S")+ " | Requested by: " + ctx.author.name)
        await ctx.send(embed=server)
        
    @bot.command()
    async def kick(ctx, member:discord.Member, *, reason=None):
        try:
            await member.kick(reason=reason)
            await ctx.send(f'User <@{str(member.id)}> has been kicked.')
        except Exception as err:
            error = discord.Embed(title="", description="", color=0xd000db)
            error.add_field(name="<a:shimy:1020126329036881920> Error <a:shimy:1020126329036881920>", value="You cannot kick this member/You do not have the correct permissions!", inline=False)
            error.set_footer(text="Error Code: {}".format(err))
            await ctx.reply(embed=error, mention_author = True)
            
    @bot.command()
    async def ban(ctx, member:discord.Member, *, reason=None):
        try:
            await ctx.guild.ban(member, reason=reason) # Bans the user.
            await member.send(f"You have been banned in {ctx.guild} for {reason}") # Private messages user.
            await ctx.send(f"<@{str(member.id)}> has been successfully banned.")
        except Exception as err2:
            error2 = discord.Embed(title="", description="", color=0xd000db)
            error2.add_field(name="<:NotLikeThis:857079883800772649> Error <:NotLikeThis:857079883800772649>", value="You cannot ban this member/You do not have the correct permissions!", inline=False)
            error2.set_footer(text="Error Code: {}".format(err2))
            await ctx.reply(embed=error2, mention_author = True)

    @bot.command()
    async def addRole(self, ctx, user : discord.Member, *, role : discord.Role):
        if role in user.roles:
            await ctx.send("User already has {role}")
        else:
            await user.add_roles(role)
            await ctx.send("Added {role} to {user.mention}")
    
    @bot.command()
    async def unban(ctx, id: int):
            user = await bot.fetch_user(id)
            await ctx.guild.unban(user)
          
    print("Bot loading complete.")
    @bot.command()
    async def ghost(ctx): 
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()  
            player = voice.play(discord.FFmpegPCMAudio("bentalk(1).wav"))
            time.sleep(5.5)
            await voice.disconnect()         
        except Exception as err4:
            error4 = discord.Embed(title="", description="", color=0xd000db)
            error4.add_field(name="<:NotLikeThis:857079883800772649> Error <:NotLikeThis:857079883800772649>", value="You are not in a voice channel!/I am already playing something!", inline=False)
            error4.set_footer(text="Error Code: {}".format(err4))
            await ctx.reply(embed=error4, mention_author = True)
            
    @bot.command()
    async def gummy(ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()  
            player = voice.play(discord.FFmpegPCMAudio("gummy.wav"))
            time.sleep(8.5)
            await voice.disconnect()         
        except Exception as err5:
            error5 = discord.Embed(title="", description="", color=0xd000db)
            error5.add_field(name="<:NotLikeThis:857079883800772649> Error <:NotLikeThis:857079883800772649>", value="You are not in a voice channel!/I am already playing something!", inline=False)
            error5.set_footer(text="Error Code: {}".format(err5))
            await ctx.reply(embed=error5, mention_author = True)
            
    @bot.command()
    async def pipe(ctx):
        try:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()  
            player = voice.play(discord.FFmpegPCMAudio("pipe.mp3"))
            time.sleep(1.5)
            await voice.disconnect()         
        except Exception as err6:
            error6 = discord.Embed(title="", description="", color=0xd000db)
            error6.add_field(name="<:NotLikeThis:857079883800772649> Error <:NotLikeThis:857079883800772649>", value="You are not in a voice channel!/I am already playing something!", inline=False)
            error6.set_footer(text="Error Code: {}".format(err6))
            await ctx.reply(embed=error6, mention_author = True)
                    
            
    # @bot.command()
    # async def pages(ctx):
    #     contents = ["This is page 1!", "This is page 2!", "This is page 3!", "This is page 4!"]
    #     pages = 4
    #     cur_page = 1
    #     message = await ctx.send(f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    #     # getting the message object for editing and reacting

    #     await message.add_reaction("◀️")
    #     await message.add_reaction("▶️")

    #     def check(reaction, user):
    #         return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    #     while True:
    #         try:
    #             reaction, user = await bot.wait_for("reaction_add", timeout=60, check=check)

    #             if str(reaction.emoji) == "▶️" and cur_page != pages:
    #                 cur_page += 1
    #                 await message.edit(embed=help)
    #                 await message.remove_reaction(reaction, user)

    #             elif str(reaction.emoji) == "◀️" and cur_page > 1:
    #                 cur_page -= 1
    #                 await message.edit(content=f"Page {cur_page}/{pages}:\n{contents[cur_page-1]}")
    #                 await message.remove_reaction(reaction, user)

    #             else:
    #                 await message.remove_reaction(reaction, user)

    #         except asyncio.TimeoutError:
    #             await message.delete()
    #             break

        
    bot.run(token)
if __name__ == "__main__":
    main(sys.argv[1:])