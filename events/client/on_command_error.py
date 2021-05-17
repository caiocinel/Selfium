import cli
from vars.client import client
from helpers import notify

@client.event
async def on_command_error(ctx, error):
    await notify.error(ctx, error)
