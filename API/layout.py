import requests,json
import re

from html.parser import HTMLParser


i = 0
dict = {'Assign agent policy for resources': '/api/api-reference/alerts/schedule-maintenance-create-daily-post/', 'Assign agent profile for resources': '/api/api-reference/agents-gateways/agents-gateways-agent-profile-post/'}
val = []
store = {}
td_set = False
tr_set = False
j = ""

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        global i,td_set,tr_set
        i += 1
        print("Encountered a start tag:", tag, i)
        if tag == "td":
            td_set = True
        elif tag == "tr":
            tr_set = True
        #pass

    def handle_endtag(self, tag):
        global i,td_set
        i -= 1
        print("Encountered an end tag :", tag, i)
        if tag == "td":
            td_set = False
        #pass
    #def close():
        #print("close called")
        #super.close()

    def handle_data(self, data):

        global i,store,j,val,td_set,tr_set
        if tr_set and td_set and i == 34:
            val.append(data)
            tr_set = False
            #td_set = False
        print("Encountered data :", data, i)
        if i == 31 and data == "URL":
            j = "URL"
        elif i == 31 and data == "Sample URLs":
            j = "Sample"
        elif i == 31 and data == "Sample request":
            j = "request"
        elif i == 31 and data == "Sample response":
            j = "response"
        elif i == 32:
            #print("")
            #print(data.split('\t'))
            r = data
            #r = re.sub(r"[\n\t]*", "", data)
            #r = re.sub(r"[\"]", "'", r)
            #print(r)
            #r = re.sub(r"[']", '"', r)
            #print(''.join(r.split('\n')))
            #r = ''.join(r.split('\n'))
            #r = ''.join(r.replace("\"",'"'))
            #print(r)
            #print("")
            #print(type(r))
            #print(dir(r))
            #dataform = str(r).strip("'<>() ").replace('\'', '\"')
            #struct = json.loads(dataform)

            if j == "response" or j == "request":
                try:
                    store[j] = json.loads(r)
                except ValueError as e:
                    store[j] = r
            elif j == "URL" or j == "Sample":
                store[j] = r
            #print(store[j])
            j = ""

store["table_parms"] = val

x = requests.get('https://docs-beta.opsramp.com' + dict["Assign agent policy for resources"])
print(x.text)
parser = MyHTMLParser()
parser.feed(x.text)

print(json.dumps(store,indent=4))
