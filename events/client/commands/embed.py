from vars.client import client
from helpers import delete, notify

#makeEmbed(ctx, title, author, author_iconURL, description, thumbnail, 
#>> thumbnailImageURL, fields, footer, footerText, footer_iconURL, timestamp):

@client.command(aliases=['embed','simpleembed'])
async def simpleEmbed(ctx, title, *, arg):
    await notify.plain(ctx, title, arg)
    delete.byContext(ctx)

@client.command()
async def completeEmbed(ctx, title, author, description, thumbnail, footer, timestamp):
    notify.makeEmbed(ctx, title, author, description, thumbnail, footer, timestamp)

