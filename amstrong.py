l=input("Input  ")
sum = int(l)
k=0 
for j in l:
    j=int(j)
    k=j**3+k   
if(k == sum):
    print(f'{sum} is ams numbeer')
else:
    print(f'{sum} is not ams numbeer')