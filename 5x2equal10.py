def table(t):
    for k in range(1,11):
        #print(t,"x",k,"=",t*k)
#        print(t,k,sep="X",end="=")
#        print(t*k,end="\n")
        print(f"{t}x{k}={t*k}")

        
tab=int(input("Enter value: "))
table(tab)
