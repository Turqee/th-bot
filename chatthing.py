import os, random, discord, sys, getopt
from dotenv import load_dotenv
from urllib.request import urlopen, Request

load_dotenv()







def main(argv):
    client = discord.Client()

    TOKEN = sys.argv[1]
    print(TOKEN)






    @client.event
    async def on_ready():
        print("We have logged  in as {}".format(client))
    @client.event
    async def embed(ctx):
        embed=discord.Embed(title="Sample Embed", url="httpfs://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
        await ctx.send(embed=embed)


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        random_quotes = [
            'bro this bot took too long',
            'so guys in this tutorial im gonna teach you how to be funny',
            (
                'thanks to lam 2 '
                'this took 1~ months (because i barley programed LOL! XD! LMAO!)'
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
            info = '''  Commands list:
                        - t!inspiration
                        - t!randomquotes
                        - t!randommath'''
            await message.channel.send(info)

    client.run(TOKEN)



if __name__ == "__main__":
    main(sys.argv[1:])
