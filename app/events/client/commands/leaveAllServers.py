from app.vars.client import client
    
@client.command(aliases=['leaveAllServers'])
async def leaveServers(ctx):
    for server in client.guilds:
        try:
            await server.leave()
        except:
            pass