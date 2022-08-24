from asyncio import trsock
import discord
from discord.ext import commands
import socket
import os
import re
import subprocess
import time


bot = commands.Bot(command_prefix="-", description=":troll:")


@bot.event
async def on_ready():
    activity = discord.Game(name="powerbot.py", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)


@bot.command()
async def test(ctx):
    await ctx.send("test response")


@bot.command()
async def ip(ctx):
    await ctx.send(socket.gethostbyname("play.spacetime.technology"))


@bot.command()
async def speedtest(ctx):
    await ctx.send('testing <--->')
    speed = subprocess.Popen('/usr/bin/speedtest', shell=True,
                             stdout=subprocess.PIPE).stdout.read().decode('utf-8')
    await ctx.send(speed)


discord_key = open("discord.key", 'r')
bot.run(discord_key.read())
