name=input("Enter your name: ")
total=float(input('How much bill is it: '))
totalp=int(input('How many person are there: '))-1
percent=float('0.'+input('How much tip you wonna give ratio: '))
share=round((total+(total*percent))/totalp,2)
print(f'Hey share {share} money you {totalp-1} friends of {name}')