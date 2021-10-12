import os
import sys
from app.vars.client import client
from app.helpers import Notify
from app.filesystem import ignore
from app.events.client.commands import banAll, deleteAllChannels, deleteAllRoles

@client.command()
async def raid(ctx):
    notify = Notify(ctx=ctx, title='Confirm Raid')
    if str(ctx.guild.id) in ignore.getIgnore():
        notify.error(content='The server {} is being ignored'.format(ctx.guild.name))
        return
    try:
        notify.alert(content=f'Confirm the command by typing *{ctx.guild.name}*')
        check = await client.wait_for('message', check=lambda m: m.content == ctx.guild.name, timeout=60)
        await check.delete()
        notify.success(title='Raiding Server',content='Starting Raid...')
        await banAll(ctx)
        await deleteAllChannels(ctx)
        await deleteAllRoles(ctx)
        notify.success(content='Raid Complete')  
    except Exception as e:
        print(e)
        notify.error(content='Something goes wrong, verify the console logs!')
        