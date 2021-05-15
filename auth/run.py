import auth

def run():
    auth.client()
    auth.loop.run_forever()
    