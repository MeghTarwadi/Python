# import random

# coin=int(random.randint(0,1))
# if coin==0:
#     print('Head')
# else:
#     print('tail')
import random
rps=['Rock','Paper','Scissors']
user=int(input('\n\n  Enter 1 for rock,\n\t2 for paper,\n\t3 for scessiors: '))-1

if(user<3 and user>-1):
    comp=random.randint(0,2)
    print(f'\ncomputer : {rps[user]}')
    print(f'\ncomputer : {rps[comp]}')
    if(comp==user):
        print('\nIts draw')
    elif(user>comp) or (comp==2 and user==0):
        print('\nYou win')    
    else:
        print('\nYou loss\n\n\n.')
else:
    print('you selected wrong option mother fucker')