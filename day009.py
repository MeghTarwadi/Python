option = {}


def add(name,bid):
    option[name]=bid


isthereanyone=True

while isthereanyone:
    add(name=input("Enter your name: "),bid=int(input("Enter data: ")))
    if input("Is there anyoneelse yes/no: ").lower()=="no":
        isthereanyone=False

maxname = ""
maxval=0

for key in option:
    if option[key]>maxval:
        maxname = key
        maxval = option[key]

print(f"Winner is {maxname} who is won at price of {option[maxname]}")