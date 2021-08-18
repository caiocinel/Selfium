import asyncio
from app.vars.client import client
from app.helpers import Notify
    
@client.command(aliases=['leaveAllServers', 'LaS'])
async def leaveServers(ctx):
    Total = 0
    notify = Notify(ctx=ctx, title='Leaving All Servers')
    notify.prepair()
    for server in client.guilds:
            try:
                await server.leave()
                Total = Total + 1
            except Exception as e:
                if (e.text == 'Invalid Guild'):
                    notify.exception(title='Oops',content='You probably own this server, or this server is invalid or blocked.')
                pass
    notify.success(content=f'You are out of a total of {Total} servers.')