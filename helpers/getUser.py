from vars.client import client

async def byMember(member):
    targetId = int(member.id)
    return await byID(targetId)

async def byID(id):
    target = await client.fetch_user(id)
    return target