import requests,json

from html.parser import HTMLParser

duplicate = {}
i = 0
dict = {}
val = 'abc'

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global i,val
        i += 1
        if i == 39:
            for item in attrs:
                if item[0] == 'href':
                    val = item[1]

        #print("Encountered a start tag:", tag, i)
        #pass

    def handle_endtag(self, tag):
        global i
        i -= 1
        #print("Encountered an end tag :", tag, i)
        #pass

    def handle_data(self, data):
        global i,dict,val
        if i == 39:
            if dict.get(data) == None:
                dict[data] = val
            else:
                duplicate[data] = val
        #print("Encountered some data  :", data , i)

x = requests.get('https://docs-beta.opsramp.com/api/api-reference/agents-gateways/')

#print the response text (the content of the requested file):
#print(x.text)

parser = MyHTMLParser()
parser.feed(x.text)
print(json.dumps(dict,indent=4))
print("")
print("Total APIs in dictionary : ",end="")
print(len(dict))
#the required first parameter of the 'get' method is the 'url':
print("")

op1 = open("duplicates.csv","a",encoding="utf-8")
op1.write("This file has list of APIs that are erroneously labelled")
op1.write("\n")

print(json.dumps(duplicate,indent=4))

for k in duplicate.keys():
    op1.write(f"{k},https://docs.opsramp.com{duplicate[k]}")
    op1.write("\n")

op1.close()
print("")
print("Erroneously labelled apis with same name : ", end="")
print(len(duplicate))
