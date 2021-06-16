import asyncio

import discord

from discord.ext import commands


medm={}   """Dictionary that contains your Memes in any audio format key:Meme name key-value: location of audio on machine"""

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='Memebot')


@bot.command()
async def Memelist(ctx):                        """List all the Memes that are currently in your database"""
    opstr="They useable meme commands are: \n"
    for a in medm.keys():
        opstr+='\t'+a+'\n'
    await ctx.send(opstr)


@bot.command()                                  """Meme command"""
async def meme(ctx,mena):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(medm[mena]))
    ctx.voice_client.play(source, after=lambda e: print(f'Player error: {e}') if e else None)

    await ctx.send(f'Now playing: {query}')

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

bot.run('token')
