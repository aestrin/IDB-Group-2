import requests
import re
import json

response = requests.get("http://reddifulapi.me/api/users?page=1").json()[0]
response+=(requests.get("http://reddifulapi.me/api/users?page=2").json())[0]
response+=(requests.get("http://reddifulapi.me/api/users?page=3").json())[0]
response+=(requests.get("http://reddifulapi.me/api/users?page=4").json())[0]


t = []
for item in response:
	t.append((item.get("name"),item.get("link_karma") ,item.get("comment_karma")))

jsondict =  dict([ (k, [v, w]) for k, v, w in t ])

with open('visual.json', 'w') as outfile:  
    json.dump(jsondict, outfile,indent=4)

print("user	commentKarma	linkKarma")
for item in t :
    print(str(item[0]) + "\t" + str(item[1]) + "\t" + str(item[2]))
