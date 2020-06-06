import json

ip = open("owords.json","r")
dict = json.loads(ip.read())

chosen_words = []

request_words = []
response_words = []
url_words = []
table_words = []


def get_req_words():
    global request_words
    request_words = []
    for item in dict.keys():
        if dict[item]["display"] == True:
            for word in dict[item]["req_words"]:
                if word not in request_words:
                    request_words.append(word)

def get_resp_words():
    global response_words
    response_words = []
    for item in dict.keys():
        if dict[item]["display"] == True:
            for word in dict[item]["resp_words"]:
                if word not in response_words:
                    response_words.append(word)

def get_url_words():
    global url_words
    url_words = []
    for item in dict.keys():
        if dict[item]["display"] == True:
            for word in dict[item]["URL_words"]:
                if word not in url_words:
                    url_words.append(word)

def get_table_words():
    global table_words
    table_words = []
    for item in dict.keys():
        if dict[item]["display"] == True and dict[item].get("table_parms") != None:
            for word in dict[item]["table_parms"]:
                if word not in table_words:
                    table_words.append(word)

def get_rem_apis():
    apis_true = 0
    for item in dict.keys():
        if dict[item]["display"] == True:
            apis_true += 1
    return apis_true

while True:
    get_req_words()
    get_resp_words()
    get_url_words()
    get_table_words()
    print("Words left in API request : ", end="")
    print(len(request_words))
    print("Words left in API response : ", end="")
    print(len(response_words))
    print("Words left in API URLs : ", end="")
    print(len(url_words))
    print("Words left in parsed tables in APIs : ", end="")
    print(len(table_words))
    print("Remaining APIs : ", end="")
    print(get_rem_apis())
    print("")
    choice = input("Do you want to stop here? y/n: ")
    if choice == "y":
        break
    print("")
    st = input("To choose words from API request? Enter 1\nTo choose words from API response? Enter 2\nTo choose words from API URL? Enter 3\nTo choose words from parsed tables? Enter 4\n")
    if st == '1':
        print("Words left in API request : ", end="")
        print(len(request_words))
        print(request_words)
        print("")
        print("Pick a word that will need RBAC to access. All APIs using that word as parameter will be marked for review")
        word_chosen = input()
        chosen_words.append(word_chosen)
        for item in dict.keys():
            if dict[item]["display"] == True:
                if dict[item].get("req_words") != None:
                    if word_chosen in dict[item]["req_words"]:
                        dict[item]["display"] = False
    elif st == '2':
        print("Words left in API response : ", end="")
        print(len(response_words))
        print(response_words)
        print("")
        print("Pick a word that will need RBAC to access. All APIs using that word as parameter will be marked for review")
        word_chosen = input()
        chosen_words.append(word_chosen)
        for item in dict.keys():
            if dict[item]["display"] == True:
                if dict[item].get("resp_words") != None:
                    if word_chosen in dict[item]["resp_words"]:
                        dict[item]["display"] = False
    elif st == '3':
        print("Words left in API URLs : ", end="")
        print(len(url_words))
        print(url_words)
        print("")
        print("Pick a word that will need RBAC to access. All APIs using that word as parameter will be marked for review")
        word_chosen = input()
        chosen_words.append(word_chosen)
        for item in dict.keys():
            if dict[item]["display"] == True:
                if dict[item].get("URL_words") != None:
                    if word_chosen in dict[item]["URL_words"]:
                        dict[item]["display"] = False
    elif st == '4':
        print("Words left in  parsed tables in APIs : ", end="")
        print(len(table_words))
        print(table_words)
        print("")
        print("Pick a word that will need RBAC to access. All APIs using that word as parameter will be marked for review")
        word_chosen = input()
        chosen_words.append(word_chosen)
        for item in dict.keys():
            if dict[item]["display"] == True:
                if dict[item].get("table_parms") != None:
                    if word_chosen in dict[item]["table_parms"]:
                        dict[item]["display"] = False
    else:
        print("You did not choose from ['1', '2', '3', '4'] ")


op1 = open("needRBAC.txt","w",encoding="utf-8")
op1.write("This file has list of APIs that need to be verified if they honor RBAC")
op1.write("\n")
for item in dict.keys():
    if dict[item]["display"] == False:
        if dict[item].get("href") != None:
            op1.write(f"{item},https://docs-beta.opsramp.com{dict[item]['href']},https://docs.opsramp.com{dict[item]['href']}")
        else:
            op1.write(item)
        op1.write("\n")

op1.write("Above APIs use the following attributes")
op1.write("\n")
for n in chosen_words:
    op1.write(n)
    op1.write("\n")


op1.write("End of a run")
op1.write("\n")
op1.write("\n")
op1.close()

op2 = open("filter.txt","w",encoding="utf-8")
op2.write("This file has list of APIs that may need a manual check to see if they need RBAC")
op2.write("\n")
for item in dict.keys():
    if dict[item]["display"] == True:
        if dict[item].get("href") != None:
            op2.write(f"{item},https://docs-beta.opsramp.com{dict[item]['href']},https://docs.opsramp.com{dict[item]['href']}")
        else:
            op2.write(item)
        op2.write("\n")
op2.write("End of a run")
op2.write("\n")
op2.write("\n")
op2.close()
