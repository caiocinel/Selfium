from vars.client import client

async def byGuild(guild):
    targetId = int(guild.id)
    return await byID(targetId)

async def byID(id):
    target = await client.fetch_guild(id)
    return target