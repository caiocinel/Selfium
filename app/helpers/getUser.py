from app.vars.client import client

async def byMember(member):
    if hasattr(member, 'id'):
        targetId = int(member.id)
    else:
        targetId = member.author.id

    return await byID(targetId)

async def byID(id):
    target = await client.fetch_user_profile(int(id))
    if target == None:
        target = client.fetch_user(int(id))
    return target