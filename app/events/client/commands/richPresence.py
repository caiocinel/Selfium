from app.events.client.commands.reload import reload
import discord
from discord import activity
import app.filesystem as fileSystem
from app.filesystem import cfg
from app.vars.client import client
from app.helpers import notify, delete

@client.command(aliases=['presencechanger','activitychanger','setactivity'])
async def richpresence(ctx):
    cfg['activity']['enabled'] = not cfg['activity']['enabled']
    fileSystem.save(cfg)
    await notify.success(ctx, f"Rich Presence has been set to { cfg['activity']['enabled'] }")
    if cfg['activity']['enabled']:
        await updatePresence(ctx)
    else:
        await client.change_presence(activity=discord.Activity())


@client.command()
async def updatePresence(ctx=None):
    activityData = dict(
        name=cfg['activity']['name'],
        state=cfg['activity']['state'],
        details=cfg['activity']['details'],
        type=cfg['activity']['type'],
        url=cfg['activity']['url']
    )
    if(ctx):
        await delete.byContext(ctx)
    fileSystem.save(cfg)
    if(cfg['activity']['enabled']):
        await client.change_presence(activity=discord.Activity(**activityData))
        if(ctx):
            await notify.success(ctx, 'Rich Presence has been updated successfully',2)
    else:
        if(ctx):
            await notify.alert(ctx, f'Rich Presence is not enabled\n Activate with {cfg["prefix"]}richPresence')

@client.command()
async def setPresenceName(ctx, *, name):
    cfg['activity']['name'] = name
    await updatePresence(ctx)

@client.command()
async def setPresenceState(ctx, *, state):
    cfg['activity']['state'] = state
    await updatePresence(ctx)

@client.command()
async def setPresenceDetails(ctx, *, details):
    cfg['activity']['details'] = details
    await updatePresence(ctx)
    discord.ActivityType

@client.command()
async def setPresenceURL(ctx, *, url):
    cfg['activity']['url'] = url
    if(cfg['activity']['type']) != 1:
        await notify.alert(ctx,'Streaming will only be displayed if presence is set to "Streaming"')
    await updatePresence(ctx)
    discord.ActivityType

@client.command()
async def setPresenceType(ctx, *, type: str.lower):
    type.upper()
    if(type == 'playing'):
        cfg['activity']['type'] = 0
    elif(type == 'streaming'):
        cfg['activity']['type'] = 1
    elif(type == 'listening'):
        cfg['activity']['type'] = 2
    elif(type == 'watching'):
        cfg['activity']['type'] = 3
    elif(type == 'custom'):
        cfg['activity']['type'] = 4
    elif(type == 'competing'):
        cfg['activity']['type'] = 5
    elif(type == 'unknown'):
        cfg['activity']['type'] = -1
    else:
        await notify.error(ctx, 'Invalid Activity Type')
        return
    await updatePresence(ctx)