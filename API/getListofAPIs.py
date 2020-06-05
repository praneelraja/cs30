import requests,json

from html.parser import HTMLParser


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
            dict[data] = val
        #print("Encountered some data  :", data , i)

x = requests.get('https://docs-beta.opsramp.com/api/api-reference/agents-gateways/')

#print the response text (the content of the requested file):
#print(x.text)

parser = MyHTMLParser()
parser.feed(x.text)
print(json.dumps(dict,indent=4))
print("")
print(len(dict))
#the required first parameter of the 'get' method is the 'url':
