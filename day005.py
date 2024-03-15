# stu=int(input('Enter total number of student:   '))
# temp0=0
# l=[]
# for k in range(stu):
#     temp1=int(input('Enter string: '))
#     l.append(temp1)
#     temp0=temp1+temp0

# print(f'Average hight = {temp0/stu}')


# for count in range(1,101):
#     if(count%3==0 or count%5==0):
#         if(count%3==0 and count%15!=0):
#             print("\nFizz")
#         if(count%5==0 and count%15!=0):
#             print("\nBuzz")
#         if(count%15==0):
#             print("\nFizzBuzz")
#     else:
#         print(f'\n{count}')


import random

let=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num=['0','1','2','3','4','5','6','7','8','9']
sym=['!','@','#','$','%','&']

letter=''
number=''
symbol=''
password=''

l=int(input('\nWnter the number of digit of  alphabates you want in your password to have       :'))
n=int(input('\nWnter the number of digit of  number you want in your password to have           :'))
s=int(input('\nWnter the number of digit of  symbol you want in your password to have           :'))

if(l+n+s<8):
    print(f'\nThis password might not be accepted by many webistes since it consist {l+n+s} lenght')

for temp in range(0,l):
    letter=letter+let[random.randint(0,len(let)-1)]
for temp in range(0,n):
    number=number+num[random.randint(0,len(num)-1)]
for temp in range(0,s):
    symbol=symbol+sym[random.randint(0,len(sym)-1)]
################################################################################################
password=letter+number+symbol

pas=[]

for p in range(0,l+n+s):
    pas.append(password[p])
random.shuffle(pas)
password=''
for ch in pas:
    password += ch

#####################################################################################################
# for final in range(0,l+n+s):
#     slc=random.randint(0,2)
    
#     if(slc==0):
#         if(len(letter)==0):
#             slc=1
#         else:
#             password=password+letter[-1]
#             if len(letter)!=1:
#                 letter=letter[:-1]
#             else:
#                 letter=''
#     if(slc==1):
#         if(len(number)==0):
#             slc=2
#         else:
#             password=password+number[-1]
#             if len(number)!=1:
#                 number=number[:-1]
#             else:
#                 number=''
#     if(slc==2):
#         if(len(symbol)==0):
#             slc=0
#             if(slc==0):
#                 if(len(letter)==0):
#                     slc=1
#                 else:
#                     password=password+letter[-1]
#                     if len(letter)!=1:
#                         letter=letter[:-1]
#                     else:
#                         letter=''
#         else:
#             password=password+symbol[-1]
#             if len(symbol)!=1:
#                 symbol=symbol[:-1]
#             else:
#                 symbol=''
                
print(f'Your password could be  :{password}')