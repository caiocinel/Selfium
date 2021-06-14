import cli
from vars.client import client

@client.event
async def on_ready():
    await cli.welcome_message()