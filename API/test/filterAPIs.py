import json

f = open("Output.json","r")
dict = json.loads(f.read())

print(json.dumps(dict, indent=4))
