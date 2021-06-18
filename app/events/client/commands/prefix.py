from app.filesystem import cfg, save
from app.vars.client import client
from app.helpers import delete, notify

@client.command()
async def prefix(ctx, arg):
    await delete.byContext(ctx)
    client.command_prefix = arg
    cfg["prefix"] = arg
    save(cfg)
    await notify.success(ctx, f'The prefix has been changed to {cfg["prefix"]} successfully')