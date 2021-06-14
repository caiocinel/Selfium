import json
import requests

def parse(token):
    headers = {"Content-Type": "application/json", "authorization": token}
    url = "https://discord.com/api/v8/users/@me"
    r = requests.get(url, headers=headers)
    userInfo = json.loads(r.text)
    return userInfo