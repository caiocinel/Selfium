import json

def load():
    with open("data/nitro.json") as giftFile:
        return json.load(giftFile)
    

def save(data):
    with open("data/nitro.json", "w") as giftFile:
        giftFile.write(json.dumps(data))
    giftFile.close()