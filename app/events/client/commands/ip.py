import requests
import discord
from app.vars.client import client
from app.helpers import Notify

@client.command(aliases=['ipinfo', 'iplocate', 'getIP'])
async def ip(ctx, *, IP):
    notify = Notify(ctx=ctx, title='IP Information')
    notify.prepair()
    ipInfo = requests.get(f'http://extreme-ip-lookup.com/json/{IP}').json()
    fields = [
        ('IP', ipInfo['query'], True),
        ('Type', ipInfo['ipType'], True),
        ('Country', ipInfo['country'], True),
        ('City', ipInfo['city'], True),
        ('Country', ipInfo['country'], True),
        ('Hostname', ipInfo['ipName'], True),
        ('ISP', ipInfo['isp'], True),
        ('Latitute', ipInfo['lat'], True),
        ('Longitude', ipInfo['lon'], True),
        ('Org', ipInfo['org'], True),
        ('Region', ipInfo['region'], True),
    ]

    notify.fields(fields=fields)