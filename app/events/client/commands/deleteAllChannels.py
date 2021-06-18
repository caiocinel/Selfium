import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import notify, delete


@commands.guild_only()
@client.command(aliases=['removeallchannels', 'deleteChannels'])
async def deleteAllChannels(ctx, *, arg: str.lower = ''):
    await delete.byContext(ctx)

    if not (ctx.message.author.guild_permissions.manage_channels):
        notify.error(ctx,"You can't do this here")  
        return

    if(arg == 'text'):
        type = ctx.guild.text_channels
    elif(arg == 'voice'):
        type = ctx.guild.voice_channels
    elif(arg == 'category'):
        type = ctx.guild.categories
    elif(arg == 'all'):
        type = ctx.guild.channels
    else:
        await notify.error(ctx, 'Not provided channel type:\n Text | Voice | Category | All')
        return

    for channel in type:
        try:
            await channel.delete()
            await asyncio.sleep(0.33)
        except:
            pass         
        finally:
            if(arg != 'all'):
                await notify.success(ctx, f'Successful deleted {arg} channels')    