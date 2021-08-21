import io
import json
import os

def getIgnore():
    if not os.path.isfile("data/ignore.json") and not os.access("data/ignore.json", os.R_OK):
        with io.open("data/ignore.json",'w') as ignoreFile:
            ignoreFile.write(json.dumps({}))
        ignoreFile.close()

    with io.open("data/ignore.json",'r') as ignoreFile:
        return (json.loads(ignoreFile.read()))

def saveIgnore(ignoreList):
    with io.open("data/ignore.json",'w') as ignoreFile:
        ignoreFile.write(json.dumps(ignoreList))