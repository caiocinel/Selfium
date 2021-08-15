import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import notify, delete, params


@client.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def renameAllChannels(ctx, *, args = ''):
    await ctx.message.delete()
    args = params.split(args)
    if len(args) > 1:
        channelType = str.lower(args[1])
        if(channelType == 'text'):
            type = ctx.guild.text_channels
        elif(channelType == 'voice'):
            type = ctx.guild.voice_channels
        elif(channelType == 'category'):
            type = ctx.guild.categories
        else:
            notify.error(ctx, f'The type of channel you provide ({args[1]}) is not supported')
    else:
        type = ctx.guild.channels

    for channel in type:
        try:
            await channel.edit(name=args[0])
            await asyncio.sleep(0.33)
        except:
            pass         
    else:
        await notify.success(ctx, f'Successful renamed all channels to {args[0]}')    