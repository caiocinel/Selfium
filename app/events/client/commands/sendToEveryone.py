from app.vars.client import client
from app.helpers import Notify 
from app.filesystem import ignore

@client.command()
async def sendToEveryone(ctx, *, message):
    notify = Notify(ctx=ctx, title='Sending To Everyone...')
    notify.prepair()
    
    if str(ctx.guild.id) in ignore.getIgnore():
        notify.error(content='The server {} is being ignored'.format(ctx.guild.name))
        return

    await ctx.guild.subscribe() # Depending on server size this can take several minutes

    for member in ctx.guild.members: # Maybe multi-account support to increase speed?
        if member.id != ctx.author.id:
            await member.send(content=message)
    else:
        notify.success(content='The message {} has been sent to all server users successfully'.format(message))
