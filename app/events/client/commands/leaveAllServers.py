import asyncio
from app.vars.client import client
from app.helpers import Notify
from app.filesystem import ignore, error
    
@client.command(aliases=['leaveAllServers', 'LaS'])
async def leaveServers(ctx):
    Total = 0
    notify = Notify(ctx=ctx, title='Leaving All Servers')
    notify.prepair()
    for server in client.guilds:
        if str(server.id) in ignore.getIgnore():
            notify.alert(content='The server {} is being ignored'.format(server.name))
            return
        try:
            await server.leave()
            Total = Total + 1
        except Exception as e:
            if (e.text == 'Invalid Guild'):
                notify.exception(content='You probably own this server, or this server is invalid or blocked.')
            error(e)
            pass
    notify.success(content=f'You are out of a total of {Total} servers.') #How the fuck will this be sent if it leaves all servers???

        