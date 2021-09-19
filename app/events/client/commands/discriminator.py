from app.vars.client import client
from app.helpers import Notify, params 
from app.filesystem import cfg

@client.command()
async def discriminator(ctx):
    notify = Notify(ctx=ctx, title='Getting All Members...')
    fields = [('Member Discriminators', '** **', False)]
    for guild in client.guilds:
        print(f'Subscribing to guild {guild.name}')
        await guild.subscribe()
        print('Subscribed')
        for member in guild.members:
            if member.discriminator == client.user.discriminator:
                fields.append(name=f'{member.name}#{member.discriminator}', value=f'{member.id}', inline=False)
    else:
        notify.fields(title='Members Discriminator',fields=fields)
