  
import discord
import time
from app.helpers import delete
from app.filesystem import cfg


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

async def plain(ctx, message, title=None):
    embed = discord.Embed()
    if(title):
        embed.title = title
    embed.description = message
    await ctx.send(embed=embed)

async def exception(ctx, e = 'Something went wrong, try again!'):
    await error(ctx, e, 5)
