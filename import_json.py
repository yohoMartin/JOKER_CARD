import json 
user_data = 'user_point.json'

def get_point(user):
    with open(user_data,"r") as file:
        data = json.load(file)
        a = data[user]['points']
    return a

def new_point(user,points):
    with open(user_data,'r+') as file:
        data = json.load(file)
        data[user]["points"] = points
        file.seek(0)
        json.dump(data,file,indent=4)
        file.truncate()
def new_user(user):
    with open(user_data,"r+") as file:
        data = json.load(file)
        if user in data:
            return
        else:
            data[user] = {"points" :0, "cards" :[]}
            file.seek(0)
            json.dump(data,file,indent=4)
            file.truncate()
    return

def new_card(user,card):
    with open(user_data,"r+") as file:
        data = json.load(file)
        if card not in data[user]:
            data[user]["cards"].append(card)
            file.seek(0)
            json.dump(data,file,indent=4)
            file.truncate()
    return

def show_cards(user):
    with open(user_data,"r") as file:
        data = json.load(file)
        a = data[user]["cards"]
    return a

def get_counter():
     with open(user_data,"r") as file:
         data = json.load(file)
         a = data["counter"]
     return a
def new_counter(counter):
    with open(user_data,'r+') as file:
        data = json.load(file)
        data["counter"] = counter
        file.seek(0)
        json.dump(data,file,indent=4)
        file.truncate()

if __name__ == 'main':
    print(show_cards("789"))

