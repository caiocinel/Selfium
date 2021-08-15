import requests
import discord
from app.vars.client import client
from app.helpers import delete

@client.command(aliases=['ipinfo', 'iplocate', 'getIP'])
async def ip(ctx, *, IP):
    await ctx.message.delete()
    ipInfo = requests.get(f'http://extreme-ip-lookup.com/json/{IP}').json()
    fields = [
        {'name': 'IP', 'value': ipInfo['query']},
        {'name': 'Type', 'value': ipInfo['ipType']},
        {'name': 'Country', 'value': ipInfo['country']},
        {'name': 'City', 'value': ipInfo['city']},
        {'name': 'Country', 'value': ipInfo['country']},
        {'name': 'Hostname', 'value': ipInfo['ipName']},
        {'name': 'ISP', 'value': ipInfo['isp']},
        {'name': 'Latitute', 'value': ipInfo['lat']},
        {'name': 'Longitude', 'value': ipInfo['lon']},
        {'name': 'Org', 'value': ipInfo['org']},
        {'name': 'Region', 'value': ipInfo['region']},
    ]
    embed = discord.Embed()
    for field in fields:
        if field['value']:
            embed.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=embed)