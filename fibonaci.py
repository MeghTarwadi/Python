# def fibonaci(a=0,b=1,c=10,k=0):
#     print(a)
#     g=a
#     k=k+1
#     a=b
#     b=a+g
#     if(k<=c):
#         fibonaci(a,b,c,k)

# start0=0
# start1=1
# maxloop=55
# startingloop=50

# fibonaci(start0,start1,maxloop,startingloop)

def fibonaci(k,b,c):
    print(b)
    
    if(k>0):
        k=k-1
        fibonaci(k,c,b+c)

start0=0
start1=1
maxloop=10

fibonaci(maxloop,start0,start1)

