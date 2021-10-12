import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify, params
from app.filesystem import ignore, error


@client.command()
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def renameAllChannels(ctx, *, args = ''):
    notify = Notify(ctx=ctx, title='Renaming All Channels')
    notify.prepair()

    if str(ctx.guild.id) in ignore.getIgnore():
        notify.error(content='The server {} is being ignored'.format(ctx.guild.name))
        return

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
            notify.error(content=f'The type of channel you provide ({args[1]}) is not supported')
    else:
        type = ctx.guild.channels

    for channel in type:
        try:
            await channel.edit(name=args[0])
            await asyncio.sleep(0.33)
        except Exception as e:
            error(e)
            pass         
    else:
        notify.success(content=f'Successful renamed all channels to {args[0]}')    