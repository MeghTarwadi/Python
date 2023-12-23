def sum_of_evrydigit(k):
    i=0
    for string in k:
        if string>='a' and string<='z' or string>='A' and string<='Z':
            return "DO YOU KNOW WATCHYA DOING BROO  !!"
            #or we can do nothing by putting it into comment
        else:
            i=int(string)+i
        
            
    return i




a=input("YOWAIMOOOO           ")

if type(sum_of_evrydigit(a))==str:
    print(sum_of_evrydigit(a))
else:
    print("The sum is          ",sum_of_evrydigit(a))

