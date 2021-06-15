import discord
import asyncio
from app.vars.client import client
from app.helpers import delete, notify, getUser
from app.config import log

@client.command()
async def debug(ctx):
    
    log.error('Deu ruim em algo')

    return
    print(a)