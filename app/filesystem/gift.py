import json

def loadGift():
    with open("data/nitro.json") as giftFile:
        return json.load(giftFile)
    

def saveGift(data):
    with open("data/nitro.json", "w") as giftFile:
        giftFile.write(json.dumps(data))
    giftFile.close()