import os, random, discord, sys, getopt
from dotenv import load_dotenv
from urllib.request import urlopen, Request
from discord.ext.commands import Bot
from discord.ext import commands


load_dotenv()

def main(argv):
    client = discord.Client()
    bot = commands.Bot(command_prefix="t!")
    TOKEN = sys.argv[1]
    print(TOKEN)


    @client.event
    async def on_ready():
        print("We have logged  in as {}".format(client))

    @client.event
    async def on_ready():
            await client.change_presence(activity=discord.Game('damian official - imposter | t!help'))

    @client.event
    async def on_message(message):
        
        if message.author == client.user:
            return

    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


    random_quotes = [
        'bro this bot took too long',
        'so guys in this tutorial im gonna teach you how to be funny',
            (
        'thanks to lam 2',
        'this took 1~ months (because i barley programed LOL! XD! LMAO!)',
        'edskidesp1',
            ),
        ]

    if message.content == 't!randomquotes':
        response = random.choice(random_quotes)
    await message.channel.send(response)

    if message.content == 't!randommath':
        x = random.randint(0,101)
        y = random.randint(0,101)
        answer = x + y
        math_output = '{} + {} = {}'.format(x,y,answer)
        await message.channel.send(math_output)
    ##    if message.content == 't!numberguess':
    ##        guess = int(input('Guess youre number: ')
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
    if message.content == 't!help':
        info = discord.Embed(title="Commands list:",  description="All existing commands", color=0x28e038)
        info.add_field(name="t!inspiration", value="makes you go :O", inline=False)
        info.add_field(name="t!randommath", value="random addition. adds numbers 1-100", inline=False)
        info.add_field(name="t!randomquotes", value="random quotes, made by yours truly", inline=False)
        info.add_field(name="t!cvf y=mx+b", value="replace y=mx+b with numbers (Don't nake y a number, and don't add spaces)", inline=False)
        await message.channel.send(embed=info)


    if message.content.startswith('t!cvf'):
        message_content = message.content.split()
        arg = message_content[1]

        lst = arg.split("=")
        for x in lst:
            if "+" in x:
                y = lst[0]
                temp=lst[1].split("+")
                mx = temp[0]
                answer = temp[1]
            elif "-" in x:
                y = lst[0]
                temp=lst[1].split("-")
                mx = temp[0]
                answer = temp[1]
        if "+" in arg:
            cvf_answer="Youre ansswer do be: {} - {} = {} :flushed:".format(mx, y, answer)
        else:
            cvf_answer="Youre ansssswer do be: {} + {} = {} :flushed:".format(mx, y, answer)
        await message.channel.send(cvf_answer)

                
    client.run(TOKEN)



if __name__ == "__main__":
    main(sys.argv[1:])
