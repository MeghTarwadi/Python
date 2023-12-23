def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return fact(n-1)*n

a=int(input("Enter the digit that you want factorial of   "))
print(fact(a))