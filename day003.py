# if(int(input('Enter number: '))%2==0):
#     print('The number is even')
# else:
#     print('The number is odd')

# x=int(input('Enter Year: '))
# if (x%400 == 0)or(x%4 == 0 and x%100!=0):
#     print('The year is leap year')
# else:
#     print('The year is not leap year')

#pizzaaaa
print('\n\nThank you for choosing Python pizza Deliveries!\n')
size=input('Enter the size of pizza: ')

if(size[0]=='s' or size[0]=='S'):
    price=15
elif(size[0]=='m' or size[0]=='M'):
    price=20
    add_pepperoni=input('Do you want pepperoni for Medium or Large pizza: ')
    if(add_pepperoni[0]=='n' or add_pepperoni[0]=='N'):
        price=price
    else:
        price=price+2
else:
    price=25
    add_pepperoni=input('Do you want pepperoni for Medium or Large pizza: ')
    if(add_pepperoni[0]=='n' or add_pepperoni[0]=='N'):
        price=price
    else:
        price=price+2

extra_cheese=input('do you need extra cheese for any size pizza: ')
if(extra_cheese[0]=='n' or extra_cheese[0]=='N'):
    price=price
else:
    price=price+1

print(f'\nYour total bill is {price}')
