import requests

def token(Njc4NTY4MTIxMjkxNzY3ODE5.YffYtA.TQW-K2hvw0S5PVhLJ7m6x7dhbbA):
    headers = {'Content-Type': 'application/json', 'authorization': token}
    url = "https://discordapp.com/api/v6/users/@me/library"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return token
    else:
        return False
