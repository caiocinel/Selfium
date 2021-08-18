from app.filesystem import cfg, save
from app.vars.client import client
from app.helpers import delete, Notify

@client.command()
async def prefix(ctx, prefix):
    notify = Notify(ctx=ctx, title='Changing Prefix')
    notify.prepair()
    client.command_prefix = prefix
    cfg["prefix"] = prefix
    save(cfg)
    notify.success(content=f'The prefix has been changed to {cfg["prefix"]} successfully')