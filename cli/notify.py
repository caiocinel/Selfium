  
import discord
import time
import datetime
from helpers import delete
from config import cfg


async def success(ctx, message, thumbnail, count : int = cfg['notifyTime']):
    embed = discord.Embed(description=f'```{message}```', colour=discord.Colour.green())
    if (thumbnail):
        embed.set_thumbnail(
        url=f"""{thumbnail}"""
        )
    if (message):
        embedMessage = await ctx.send(embed=embed)
        time.sleep(count)
        await delete.byMessage(embedMessage)
    else:
        await error(ctx, 'The message was not found.')


async def error(ctx, message, thumbnail, count : int = cfg['notifyTime']):
    embed = discord.Embed(description=f'```{message}```', colour=discord.Colour.dark_red())
    if (thumbnail):
        embed.set_thumbnail(
        url=f"""{thumbnail}"""
        )
    if (message):
        embedMessage = await ctx.send(embed=embed)
        time.sleep(count)
        await delete.byMessage(embedMessage)
    else:
        await error(ctx, 'The message was not found.')
               
async def alert(ctx, message, thumbnail, count : int = cfg['notifyTime']):
    embed = discord.Embed(description=f'{message}', colour=discord.Colour.red())
    if (thumbnail):
        embed.set_thumbnail(
        url=f"""{thumbnail}"""
        )
    if (message):
        embedMessage = await ctx.send(embed=embed)
        time.sleep(count)
        await delete.byMessage(embedMessage)
    else:
        await error(ctx, 'The message was not found.', None)

async def makeEmbed(ctx, title, author, author_iconURL, description, thumbnail, thumbnailImageURL, fields, footer, footerText, footer_iconURL, timestamp):
    embed = discord.Embed(title=f'{title}', description=f'{description}', Color=discord.Colour.purple())
    embed.set_author(name=f'{author}', icon_url=f'{author_iconURL}')
    if (footer):
        if (timestamp):
            embed.set_footer(text=f'{footerText}' + f' {str(datetime.utcnow())}', icon_url=f'{footer_iconURL}')
        else:
            embed.set_footer(text=f'{footerText}', icon_url=f'{footer_iconURL}')
    
    if (thumbnail):
        embed.set_thumbnail(url=f'{thumbnailImageURL}')
    await ctx.send(embed=embed)

async def exception(ctx):
    await error(ctx, f'Something went wrong, try again!', None, 5)