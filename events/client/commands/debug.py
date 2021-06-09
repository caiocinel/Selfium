import discord
import asyncio
from vars.client import client
from helpers import delete, notify, getUser

@client.command()
async def debug(ctx):
    
    a = ctx.guild._members
    for member in a:
        user = await getUser.byID(member)
        if user.id != ctx.author.id:
            await user.create_dm()
            await user.send('Boa noite')
            print(user.name)
            await asyncio.sleep(2)
    return
    print(a)