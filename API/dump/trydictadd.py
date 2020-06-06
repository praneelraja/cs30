import json,re

#dict = {"abc" : {"def" : ["test"]}}
#dict["abc"]["klm"] = "nop"
#dict["qrs"] = [{"tuv" : "wxy", "zab" : "cde"} , {"fgh" : "ijk" , "lmo" : "pqr"}]
#if type(dict["qrs"]) == type([]):
#    print("says type is list")
#if type(dict["abc"]) == type({}):
#    print("says type is dict")
#dict["abc"]["def"].append("add")
#print(json.dumps(dict,indent=4))
#dic = {"abc" : {"def" : "test", "new" : "value","lets" : "see"}}
#for item in dic["abc"]:
#    print(item)

url = "POST https://{api-url}/api/v2/tenants/{clientId}/timeBoundRequests/{timeBountRequestId}"

url = re.search('https://{api-url}/api/v2/(.+)', url).group(1)
print(url)
r = re.sub(r"[/{}]", " ", url)
print(r)
r = r.split()
print(r)

dic = [{"abc" : "val"}, {"def" : "test"}, {"new" : "value"}, {"lets" : "see"}]
for item in dic:
    print(item)
    print(item.keys(),
