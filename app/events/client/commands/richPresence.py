from app.events.client.commands.reload import reload
import discord
from discord import activity
import app.filesystem as fileSystem
from app.filesystem import cfg
from app.vars.client import client
from app.helpers import Notify

 ##

@client.command(aliases=['presencechanger','activitychanger','setactivity'])
async def richpresence(ctx):
    notify = Notify(ctx=ctx, title='Rich Presence')
    notify.prepair()
    cfg['activity']['enabled'] = not cfg['activity']['enabled']
    fileSystem.save(cfg)
    notify.success(content=f"Rich Presence has been set to { cfg['activity']['enabled'] }")
    if cfg['activity']['enabled']:
        await updatePresence(notify)
    else:
        await client.change_presence(activity=discord.Activity())


@client.command()
async def updatePresence(notify=None):
    activityData = dict(
        name=cfg['activity']['name'],
        state=cfg['activity']['state'],
        details=cfg['activity']['details'],
        type=cfg['activity']['type'],
        url=cfg['activity']['url']
    )
    fileSystem.save(cfg)
    if(cfg['activity']['enabled']):
        await client.change_presence(activity=discord.Activity(**activityData))
        if(notify):
            notify.success(content='Rich Presence has been updated successfully')
    else:
        if(notify):
            notify.alert(content=f'Rich Presence is not enabled\n Activate with {cfg["prefix"]}richPresence')

@client.command()
async def setPresenceName(ctx, *, name):
    cfg['activity']['name'] = name
    await updatePresence(Notify(ctx=ctx, title='Presence Name'))

@client.command()
async def setPresenceState(ctx, *, state):
    cfg['activity']['state'] = state
    await updatePresence(Notify(ctx=ctx, title='Presence State'))

@client.command()
async def setPresenceDetails(ctx, *, details):
    cfg['activity']['details'] = details
    await updatePresence(Notify(ctx=ctx, title='Presence Details'))

@client.command()
async def setPresenceURL(ctx, *, url):
    notify = Notify(ctx=ctx, title='Presence URL')
    notify.prepair()
    cfg['activity']['url'] = url
    if(cfg['activity']['type']) != 1:
        notify.alert(content='Streaming will only be displayed if presence is set to "Streaming"')
    await updatePresence(notify)

@client.command()
async def setPresenceType(ctx, *, type: str.lower):
    notify = Notify(ctx=ctx, title='Presence Type')
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
        notify.error(content='Invalid Activity Type')
        return
    await updatePresence(ctx)