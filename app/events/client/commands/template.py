from app.vars.client import client
from app.helpers import Notify, params 
from app.filesystem import cfg

@client.command()
async def template(ctx):
    notify = Notify(ctx=ctx, title='Template File...')
    
