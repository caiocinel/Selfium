import asyncio
from discord.ext import commands
from app.vars.client import client
from app.helpers import Notify
from app.filesystem import ignore


@client.command(aliases=['removeAllWebhooks'])
@commands.guild_only()
@commands.has_permissions(manage_channels=True)
async def deleteAllWebhooks(ctx):
    notify = Notify(ctx=ctx, title ='Deleting All Webhooks...')
    notify.prepair()

    if str(ctx.guild.id) in ignore.getIgnore():
        notify.error(content='The server {} is being ignored'.format(ctx.guild.name))
        return

    for channel in ctx.guild.text_channels:
        if channel.permissions_for(ctx.guild.me).manage_webhooks:
            for webhook in channel.webhooks:
                await webhook.delete()
                await asyncio.sleep(0.33)
    else:
        notify.success(content=f'Successful deleted all webhooks')    