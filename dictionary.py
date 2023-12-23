dict1={1:"megh"
       ,2:"gotya"
       ,3:"devlu"
       ,4:"gol"}
print(dict1)

print(dict1.keys())

print(dict1.values())

print(dict1.get(2))
print(dict1.get(4))
num=int(input("EnTeR LOOP THAT YOU WANT TO EXECUTE   " ))
count1=0


for dict in dict1.keys():
    
    
    if(count1 < num):
        print(f"at roll no {dict} the student is {dict1[dict]}")
        count1=count1+1
    else:
        print("exicuted")


count1=0
for key,val in dict1.items():

    if(count1 < num):
        print(f"at roll no {key} the student is {val}")
        count1=count1+1
    else:
        print("exicuted")





