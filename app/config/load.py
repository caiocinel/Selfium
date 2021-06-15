import json

with open("data/config.json") as loadFile:
    cfg = json.load(loadFile)
loadFile.close()