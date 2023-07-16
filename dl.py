import json, pathlib, urllib.request, os

dlPath = 'saved/'

he = open('heBringsYouPlaybackProgress.json')
data = json.load(he)

for o in data:
    url = o['url']
    name = o['name']
    ext = pathlib.Path(url).suffix
    
    newName = name + ext
    
    newPath = os.path.join(dlPath, newName)
    
    urllib.request.urlretrieve(url, newPath)

he.close()
