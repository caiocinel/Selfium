from app.filesystem import cfg, save
from app.vars.client import client
from app.helpers import delete, notify

@client.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    client.command_prefix = prefix
    cfg["prefix"] = prefix
    save(cfg)
    await notify.success(ctx, f'The prefix has been changed to {cfg["prefix"]} successfully')