import asyncio
import discord
import os
import json
import media_json

from discord.ext import commands

media_json.makeJson()
medm = {}
medm = json.loads(open('media.json').read())


dirn = os.path.dirname(__file__)
filename = os.path.join(dirn,'key.txt')
f = open(filename, "r")
key_string=f.read()



bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='Relatively simple music bot example')

""""@bot.event
async def on_message(message):
    await message.channel.send('Hello World!')"""
@bot.command()
async def Memelist(ctx):
    opstr="They useable meme commands are: \n"
    for a in medm.keys():
        opstr+='\t'+a+'\n'
    await ctx.send(opstr)

@bot.command()
async def bolo(ctx):
    await ctx.send("Kya");

@bot.command()
async def meme(ctx,mena):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(medm[mena]))
    ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

    await ctx.send(f'Now playing: {mena}')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def joinM(ctx, *, channel: discord.VoiceChannel):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(channel)
        await channel.connect()

bot.run(key_string)