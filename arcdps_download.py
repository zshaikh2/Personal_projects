#! /usr/bin/env python

import requests

url = "https://www.deltaconnected.com/arcdps/x64/d3d9.dll"
r = requests.get(url, allow_redirects=True)

with open("/home/zeeshan/Games/guild-wars-2/drive_c/Program Files/Guild Wars 2/bin64/d3d9.dll", 'wb') as f:
    f.write(r.content)

print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
