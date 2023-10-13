a=int(input("ENTER VALUE OF A = "))
b=int(input("ENTER VALUE OF B = "))
c=int(input("ENTER VALUE OF C = "))


if a>b:
    if a>c:
        print(f"{a} is greatest")
    else:
        print(f"{c} is greatest")
elif b>a:
    if b>c:
        print(f"{b} is greatest")
    else:
        print(f"{c} is greatest")
elif a==b and b==c:
        print(f"{a} , {b} and {c} are greatest")
elif c==a:    
    if b>c:
        print(f"{c} and {a} are greatest")
    else:
        print(f"{b} is greatest")
elif c==a:    
    if b>c:
        print(f"{c} and {a} are greatest")
    else:
        print(f"{b} is greatest")

else:    
    if b>c:
        print(f"{b} and {a} are greatest")
    else:
        print(f"{c} is greatest")
    

