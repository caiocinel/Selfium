from app.vars.client import client
from app.helpers import Notify, delete

@client.event
async def on_command_error(ctx, error):
    try:
        notify = Notify(ctx=ctx, title="Exception")
        notify.exception(content=error.args[0])
    except:
        pass

