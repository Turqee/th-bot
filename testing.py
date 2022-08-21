import discord, os, getopt, sys
import asyncio
from discord.ext import commands
from discord.ext.commands import bot

client = discord.Client()
token = "MTAxMDY0OTY2ODI4MTE3MjA0OA.G-93Dg.TMEwJcjD8hAek62JTWXRyiOe1NRHnxUm5UJ9bU"
bot = commands.Bot(command_prefix="!")

@bot.command(pass_context=True)
async def hello(ctx):
    await ctx.send("Deeg")

print("Token: " + token)
print("We have logged in as {}".format(client.user.name))
bot.run(token)