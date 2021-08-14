import asyncio
from app.vars.client import client
from app.helpers.notify import ConsoleLog
    
@client.command(aliases=['leaveAllServers', 'LaS'])
async def leaveServers(ctx):
    AllowList = [847280853255716954]
    Total = 0

    await ctx.message.delete()

    for server in client.guilds:
        if not(server.id in AllowList):

            try:
                await server.leave()
                Total = Total + 1
                ConsoleLog(f'[{server.name}]: has been successfully removed from your server list.')
            except Exception as e:
                if (e.text == 'Invalid Guild'):
                    ConsoleLog('You probably own this server, or this server is invalid or blocked.')
                pass

        else:
            ConsoleLog(f'[{server.name}]: was ignored because it was in the AllowList!')

    message = await ctx.channel.send(
        f'You are out of a total of {Total} servers.'
    )

    await asyncio.sleep(5)

    await message.delete()