import json,re

ip = open("Output.json","r")
dict = json.loads(ip.read())

er = open("errors.txt","a")


print(json.dumps(dict, indent=4))

#Initialize each dict with 3 lists

def parseResponseTree(rdict):
    for word in rdict.keys():
        if word not in dict[item]["resp_words"]:
            dict[item]["resp_words"].append(word)
            if type(rdict[word]) == type({}):
                parseResponseTree(rdict[word])


for item in dict.keys():
    dict[item]["req_words"] = []
    dict[item]["resp_words"] = []
    dict[item]["URL_words"] = []
    dict[item]["display"] = True

for item in dict.keys():
    if dict[item].get("request") != None:
        if type(dict[item]["request"]) == type([]):
            for req in dict[item]["request"]:
                for word in req.keys():
                    if word not in dict[item]["req_words"]:
                        dict[item]["req_words"].append(word)
        elif type(dict[item]["request"]) == type({}):
            for word in dict[item]["request"].keys():
                if word not in dict[item]["req_words"]:
                    dict[item]["req_words"].append(word)
    if dict[item].get("response") != None:
        if type(dict[item]["response"]) == type([]):
            for req in dict[item]["response"]:
                if type(req) == type({}):
                    for word in req.keys():
                        if word not in dict[item]["resp_words"]:
                            dict[item]["resp_words"].append(word)

        elif type(dict[item]["response"]) == type({}):
            parseResponseTree(dict[item]["response"])
    if dict[item].get("URL") != None:
        url = dict[item]["URL"]
        try:
            url = re.search('https://(.+)', url).group(1)
            r = re.sub(r"[/{}]", " ", url)
            dict[item]["URL_words"] = r.split()
        except:
            er.write("URL cant be parsed:")
            er.write(url)
            er.write("")


op = open("owords.json","w")
op.write(json.dumps(dict))
op.close()
er.close()
#print(json.dumps(dict,indent=4))
