from vars.client import client

async def byMember(member):
    if hasattr(member, 'id'):
        targetId = int(member.id)
    else:
        targetId = member.author.id

    return await byID(targetId)

async def byID(id):
    target = await client.fetch_user(id)
    return target