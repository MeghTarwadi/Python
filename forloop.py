'''

for letter in 'python':
    print('current letter',letter)

fruits = ['banana','apple','mango']
for fruit in fruits:
    print('current fruit',fruit)
    

letter="Python is op"
for l in range(2,10,2):
    #range(start , stop , steps)
    
    print('current letter',letter[l])

'''
a=int(input("Enterr the digit that you want to print  "))

start=a
stop=a*10+1
steps=a
for l in range(start , stop , steps):
    print(f"{start} * {l/5} = {l}")
    
    

