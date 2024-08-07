import random

print("\n\n==========Black Jack==========")


card = {"Ace":['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
        "Clubs":['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
        "Diamonds":['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
        "Hearts":['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        }
cardType = ["Ace","Clubs","Diamonds","Hearts"]

values = {"A":11,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10}

computer = {"Ace":[],"Clubs":[],"Diamonds":[],"Hearts":[]}
player = {"Ace":[],"Clubs":[],"Diamonds":[],"Hearts":[]}

def hit(compititor):
    temp0 = cardType[random.randint(0,len(cardType)-1)]
    temp1 = random.randint(0,len(card[temp0])-1)
    compititor[temp0].append(card[temp0][temp1])
    card[temp0].remove(card[temp0][temp1])

def show(compititor,all=True):
    if(all==True):
        for type in compititor:
            for x in compititor[type]:
                print(x+" of "+type )
    else:
        for type in compititor:
            for x in compititor[type]:
                print(x+" of "+type )
                return

def score(compititor):
    total=0
    for type in compititor:
            for x in compititor[type]:
                total=values[x]+total
    return total

hit(computer)
hit(computer)
hit(player)
hit(player)

print("\nYour cards :")
show(player)

print("\nComputer cards :")
show(computer,False)
exit = False

while not (score(player)>16 and score(computer)>16):
    if score(player)<17:
        hit(player)
    if score(computer)<17:
        hit(computer)
    