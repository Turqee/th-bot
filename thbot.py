from asyncio import sleep
import os, random, discord, sys, getopt, time, minestat
from importlib.abc import TraversableResources
from click import pass_context
from turtle import color, title
from unicodedata import name
from dotenv import load_dotenv
from urllib.request import urlopen, Request
from discord.ext.commands import bot
from discord.ext import commands
from discord_ui import Button
 
def main(argv):
    intents = discord.Intents.default()
    intents.members = True

    client = discord.Client()
    #intents = discord.Intents().all()
    bot = commands.Bot(command_prefix='t!')

    load_dotenv()
    token = os.getenv('TOKEN')



    print("DO NOT PUBLISH PUBLICLY: " + token)
    @client.event
    async def on_ready():
      #print('made it to client.event') (debug)

      #---------Bot Status (Not Custom)---------#
        status=["wit dey worm", "with twitch source code", "Skate 3", "theroy.tech", "im here for cs club", "with finkey 🥺", "clash royale", "with java" ]
        rstatus = random.choice(status)
        await client.change_presence(activity=discord.Game( rstatus +' | t!help in ' + str(len(client.guilds)) + ' servers.'), status=discord.Status.idle)
        print("We have logged in as {}".format(client.user.name))

        
        
    @client.event
    async def on_message(message):

       # print('made it to on_message') (for debug)

        color = [0xff0000, 0xff4d00, 0xfcca03, 0x37ff00, 0x0059ff, 0xa200ff]
        rcolor = random.choice(color)
        #---------Help Command; may try to add multiple pages at a later date---------#
        if message.content == 't!help':
            info = discord.Embed(title="Commands list:",  description="All existing commands", color=rcolor)
            info.add_field(name=":star_struck:`t!inspiration`", value="makes you go :O", inline=False)
            info.add_field(name=":1234:`t!randommath`", value="random math. adds numbers -45000-45000", inline=True)
            info.add_field(name=":ping_pong:`t!ping`", value=":exploding_head:", inline=False)
            info.add_field(name=":receipt:`t!userinfo`", value="User information about yourself (Pinging others does not bring up theirs sadly).", inline=False)
            info.add_field(name=":signal_strength:`t!serverinfo`", value="Server information :exploding_head:", inline=False)
            info.set_footer(text='Sumbit ideas and issues @ https://github.com/zTheroy/theroy-discord-bot/issues')
            await message.reply(embed=info, mention_author=False)

        #---------Random math command. May remove at a later date---------#
        if message.content == 't!randommath':
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
            await message.channel.send(embed=math_embed)

        #---------Inspirational quotes command; honestly not sure how it works---------#
        if message.content == 't!inspiration':
            random_quote = Request('https://api.forismatic.com/api/1.0/?method=getQuote&lang=en&format=jsonp&jsonp=?', headers={'User-Agent': 'Mozilla/5.0'})
            page = urlopen(random_quote)
            html_bytes = page.read()
            html = html_bytes.decode("utf-8")
            #print(html)
            html = html.split(":")
            inspiration = html[1].split("quoteAuthor")
            inspiration = inspiration[0]
            inspiration = inspiration[:-3]
            await message.channel.send(inspiration)


        # if message.content.startswith('t!cvf'):
        #     message_content = message.content.split()
        #     arg = message_content[1]
        #     lst = arg.split("=")
        #     for x in lst:
        #         if "+" in x:
        #             y = lst[0]
        #             temp=lst[1].split("+")
        #             mx = temp[0]
        #             answer = temp[1]
        #         elif "-" in x:
        #             y = lst[0]
        #             temp=lst[1].split("-")
        #             mx = temp[0]
        #             answer = temp[1]
        #     if "+" in arg:
        #         cvf_answer="Youre ansswer do be: {} - {} = {} :flushed:".format(mx, y, answer)
        #     else:
        #         cvf_answer="Youre ansssswer do be: {} + {} = {} :flushed:".format(mx, y, answer)
        #     await message.channel.send(cvf_answer)

        #---------Ping Command (Note: Execution time is most likely broken, keeps printing 0.0 seconds?)---------#
        if message.content.startswith('t!ping'):
            start = time.time()
            latency = message.channel.created_at
            end = time.time()
            execution_time = end - start
            #embedding execution time and latency under
            ping_title = discord.Embed(title="pong :ping_pong:",color=0x005ef5)
            ping_title.add_field(name="Execution Time", value=(f"{execution_time} seconds"), inline=False)
            ping_title.add_field(name="Latency", value=str(round(client.latency*1000))+" ms", inline=False)
            await message.channel.send(embed=ping_title)
        
        
        #---------USER INFORMATION---------#
        id = message.author.id
        username = message.author.name
        avatar = message.author.avatar_url
        is_bot = message.author.bot
        disc = message.author.discriminator
        create = message.author.created_at
        #---------GUILD INFORMATION---------#
        gname = message.guild.name
        gid = message.guild.id
        gavatar = message.guild.icon_url
        channels = message.guild.text_channels
        owner = message.guild.owner_id
        gcreate = message.guild.created_at
        gmfa = message.guild.mfa_level # (According to API Documentation) Indicates the guild’s two factor authorisation level. If this value is 0 then the guild does not require 2FA for their administrative members. If the value is 1 then they do.
        cat = message.guild.categories
        voice = message.guild.voice_channels
        emoji = message.guild.emojis
        members = message.guild.member_count
        #---------SPOTIFY INFORMATION---------#
        ac = discord.Spotify.album_cover_url
        album = discord.Spotify.album
        sid = discord.Spotify.track_id
        art = discord.Spotify.artist
        stime = discord.Spotify.duration
        #---------random ah code 💀💀---------#
        if gmfa == 1:
            gmfa = "Required"
            gemoji = ":lock:"
        else:
            gmfa = "Not Required"
            gemoji = ":unlock:"
        # Checks if 2FA is required on server, explained above
        gchannels = len(cat) + len(channels) + len(voice)
        emojilst = [':grinning:', ':smiley:', ':smile:', ':grin:', ':laughing:', ':sweat_smile:', ':joy:', ':rofl:', ':relaxed:', ':blush:', ':innocent:', ':slight_smile:', ':upside_down:', ':wink:', ':relieved:', ':smiling_face_with_tear:', ':heart_eyes:', ':smiling_face_with_3_hearts:', ':kissing_heart:', ':kissing:', ':kissing_smiling_eyes:', ':kissing_closed_eyes:', ':yum:', ':stuck_out_tongue:', ':stuck_out_tongue_closed_eyes:', ':stuck_out_tongue_winking_eye:', ':zany_face:', ':face_with_raised_eyebrow:', ':face_with_monocle:', ':nerd:', ':sunglasses:', ':star_struck:', ':partying_face:', ':smirk:', ':unamused:', ':disappointed:', ':pensive:', ':worried:', ':confused:', ':slight_frown:', ':frowning2:', ':persevere:', ':confounded:', ':tired_face:', ':weary:', ':pleading_face:', ':cry:', ':sob:', ':triumph:', ':face_exhaling:', ':angry:', ':rage:', ':face_with_symbols_over_mouth:', ':exploding_head:', ':flushed:', ':face_in_clouds:', ':hot_face:', ':cold_face:', ':scream:', ':fearful:', ':cold_sweat:', ':disappointed_relieved:', ':sweat:', ':hugging:', ':thinking:', ':face_with_hand_over_mouth:', ':yawning_face:', ':shushing_face:', ':lying_face:', ':no_mouth:', ':neutral_face:', ':expressionless:', ':grimacing:', ':rolling_eyes:', ':hushed:', ':frowning:', ':anguished:', ':open_mouth:', ':astonished:', ':sleeping:', ':drooling_face:', ':sleepy:', ':dizzy_face:', ':face_with_spiral_eyes:', ':zipper_mouth:', ':woozy_face:', ':nauseated_face:', ':face_vomiting:', ':sneezing_face:', ':mask:', ':thermometer_face:', ':head_bandage:', ':money_mouth:', ':cowboy:', ':disguised_face:']
        remojilist = random.choice(emojilst)
        #random emoji thing for server information, will try to find random emoji api later ¯\_(ツ)_/¯
        if members < 10:
            memoji = ':bust_in_silhouette:'
        else:
            memoji = ':busts_in_silhouette:'
        #if statements for code🤯

        #---------User Information Command---------#
        if message.content == 't!userinfo':
            info = discord.Embed(title="",  description="", color=0x481c70)
            info.set_author(name=username + "#" + disc, icon_url=avatar)
            info.add_field(name="User ID :performing_arts:", value="*" + str(id) + "*",)
            info.add_field(name="Username :name_badge:", value="*" + username + "*",  inline=True)
            info.add_field(name="Bot :robot:", value="*" + str(is_bot) + "*")
            info.add_field(name="Discriminator :hash:", value="*" + disc + "*", inline=True)
            info.set_footer(text="Profile creation: " + create.strftime("%Y-%m-%d, %H:%M:%S"))
            await message.reply(embed=info, mention_author = False)



        #---------Server Information Command---------#
        #server.add_field(name="", value=, inline=True)
        if message.content == 't!serverinfo':
            server = discord.Embed(title="", description="", color=0x3c8009)
            server.set_author(name=gname, icon_url=gavatar)
            server.add_field(name="Owner :judge:", value=owner, inline=True)
            server.add_field(name="2FA Required " + gemoji , value=str(gmfa), inline=True)
            server.add_field(name="Channels :speech_balloon:", value=gchannels, inline=True)
            server.add_field(name="Emojis " + remojilist, value=str(len(emoji)), inline=True)
            server.add_field(name="Members " + memoji, value=str(members), inline=True)
            server.set_footer(text="ID: " + str(gid) + " | Server Creation: " + gcreate.strftime("%Y-%m-%d %H:%M:%S"))
            await message.channel.send(embed=server)

        #---------Spotify Command LOL!---------#
        if message.content == "t!spotify":
             spit = discord.Embed(title="", value="", color=0x189bcc)
             spit.set_author(name=username + "#" + disc, icon_url=avatar)
             spit.add_field(name="Album", value=album, inline=True)
             spit.add_field(name="Duration", value=stime, inline=True)
             spit.add_field(name="Artist", value=str(art), inline=True)
             spit.set_footer(text="Track ID: " + str(sid))
             await message.channel.send(embed=spit)

    

        # ms = minestat.MineStat('cultcraft.my.pebble.host', 25565)
        # if message.content == "serverstats" and ms.online:
        #     await message.channel.send('Minecraft server status of %s on port %d:' % (ms.address, ms.port)) 
        #     mserver = discord.Embed(title="", description="", color=0x3c8009)
        #     mserver.add_field(name="f", Svalue='Server is online running version %s with %s out of %s players.' % (ms.version, ms.current_players, ms.max_players), inline=False)
        #     mserver.add_field(name="a", value='Message of the day: %s' % ms.motd, inline=False)
        #     mserver.add_field(name="r", value='Message of the day without formatting: %s' % ms.stripped_motd, inline=False)
        #     mserver.add_field(name="t", value='Latency: %sms' % ms.latency, inline=False)
        #     mserver.add_field(name="s", value='Connected using protocol: %s' % ms.slp_protocol, inline=False)
        #     await message.channel.send(embed=mserver)

    client.run(token)
if __name__ == "__main__":
    main(sys.argv[1:])