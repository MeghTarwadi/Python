# def prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return "not a prime number"
#     return "numbe is prime number"

# print("\nThe numbe is " + prime(int(input("Enter number: "))))



def cefer(mode,msg,offset):
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    offset=offset%len(alpha)
    ans=""
    for i in msg.lower():
        tf=False
        a=0
        while not tf and a<len(alpha):
            if(i==alpha[a]):
                if mode.lower()=="encode" and a+offset > len(alpha) :
                    ans=ans+alpha[a-len(alpha)+offset]
                elif mode.lower()=="encode" and a+offset <= len(alpha):
                    ans=ans+alpha[a+offset]
                elif mode.lower()=="decode" and a<offset:
                    ans=ans+alpha[len(alpha)-offset+a]
                else:
                    ans=ans+alpha[a-offset]
                tf=True
            a+=1
        if not tf:
            ans=ans+i
    return ans

print(cefer(mode=input("Enter mode: ") , msg=input("enter msg: ") , offset=int(input("Enter offset: "))))