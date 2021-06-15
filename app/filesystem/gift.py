import json

def load():
    with open("logs/nitro.json") as giftFile:
        return json.load(giftFile)
    

def save(data):
    with open("logs/nitro.json", "w") as giftFile:
        giftFile.write(json.dumps(data))
    giftFile.close()