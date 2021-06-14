  
import discord
import time
import datetime
from helpers import delete
from config import cfg


async def success(ctx, message, count : int = cfg['notifyTime']):
    try:
        embed = discord.Embed(description=f'```{message}```', colour=discord.Colour.green())
        embedMessage = await ctx.send(embed=embed)
        time.sleep(count)
    except:
        pass
    finally:
        if(embedMessage):
            await delete.byMessage(embedMessage)

async def error(ctx, message, count : int = cfg['notifyTime']):
    try:
        embed = discord.Embed(description=f'```{message}```', colour=discord.Colour.dark_red())
        embedMessage = await ctx.send(embed=embed)
        time.sleep(count)
    except:
        pass
    finally:
        if(embedMessage):
            await delete.byMessage(embedMessage)
               
async def alert(ctx, message, count : int = cfg['notifyTime']):
    try:
        embed = discord.Embed(description=f'{message}', colour=discord.Colour.gold())
        embedMessage = await ctx.send(embed=embed)
        time.sleep(count)
    finally:
        if(embedMessage):
            await delete.byMessage(embedMessage)

async def plain(ctx, title, message):
    embed = discord.Embed(title=f'{title}',description=f'{message}')
    await ctx.send(embed=embed)

async def exception(ctx, e = 'Something went wrong, try again!'):
    await error(ctx, e, 5)
