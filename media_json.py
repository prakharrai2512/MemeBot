import os
import json

def makeJson():
    fname = open("media.json", "w")
    dirn = os.path.dirname(__file__)
    filename = os.path.join(dirn, 'Media')
    entries = os.listdir(filename)
    labels = {}
    for entry in entries:
        labels.update({entry.split(".")[0]:os.path.join('Media', entry)})
    json.dump(labels,fname,separators=(',\n',': '))
    fname.close()

