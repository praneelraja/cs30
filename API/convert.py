import json
#txt = "{'id': '042761ba-542e-4a7a-8e38-3ebbea7eeb16'}"
import requests
txt =   "[{\"id\": \"042761ba-542e-4a7a-8e38-3ebbea7eeb16\"},{\"id\": \"023471da-698b-3a2e-1e93-6dbaca8eea23\"},{\"id\": \"855eb82e-3064-40a1-a26e-77efabe300da\"}]"
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'

# printing original string
print("The original string : " + str(test_string))

# using json.loads()
# convert dictionary string to dictionary
res = json.loads(test_string)

#x = json.loads(txt)
#x = requests.get(txt).json()

dataform = txt.encode().decode('unicode_escape')
struct = json.loads(txt)

f = open("apiDictOutput.txt" , "a")
f.write(json.dumps(res))
f.write(json.dumps(struct))
f.close()

print(res)
print(struct)
