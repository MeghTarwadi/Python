    if(i==alpha[a]):
                if mode.lower()=="encode" and a+offset > len(a) :
                    ans=ans+a[a-len(a)+offset]
                else:
                    ans=ans+a[a+offset]
                if mode.lower()=="decode" and a<offset:
                    ans=ans+a[len(a)-offset+a]
                else:
                    ans=ans-a[a-offset]
    retu