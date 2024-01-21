dic=(   {"Q":"qustion 1","A":"a1","B":"b1","C":"c1","D":"d1","ANS":"A","P":10,"fix":0},
        {"Q":"qustion 2","A":"a2","B":"b2","C":"c2","D":"d2","ANS":"B","P":100,"fix":0},
        {"Q":"qustion 3","A":"a3","B":"b3","C":"c3","D":"d3","ANS":"C","P":1000,"fix":0},
        {"Q":"qustion 4","A":"a4","B":"b4","C":"c4","D":"d4","ANS":"D","P":10000,"fix":0},
        {"Q":"qustion 5","A":"a5","B":"b5","C":"c5","D":"d5","ANS":"A","P":100000,"fix":10000},
        {"Q":"qustion 6","A":"a6","B":"b6","C":"c6","D":"d6","ANS":"B","P":1000000,"fix":10000},
        {"Q":"qustion 7","A":"a7","B":"b7","C":"c7","D":"d7","ANS":"C","P":10000000,"fix":10000},
        {"Q":"qustion 8","A":"a8","B":"b8","C":"c8","D":"d8","ANS":"D","P":100000000,"fix":10000},
        {"Q":"qustion 9","A":"a9","B":"b9","C":"c9","D":"d9","ANS":"A","P":1000000000,"fix":100000000},
        {"Q":"qustion 10","A":"a10","B":"b10","C":"c10","D":"d10","ANS":"B","P":10000000000,"fix":100000000},
        {"Q":"qustion 11","A":"a11","B":"b11","C":"c11","D":"d11","ANS":"C","P":100000000000,"fix":100000000}
    )
current=0
money=0;
for qust in dic:
    print(f"{qust["Q"]}\nA.{qust["A"]}\nB.{qust["B"]}\nC.{qust["C"]}\nD.{qust["D"]}\n")
    conf="NO"
    while(conf!="YES"):
        Opt=input("Enter your ans: ").upper()
        while(Opt!='A' and Opt!='C' and Opt!='D' and Opt!='B'):
            print("\nPlease Enter valid input from A to D")
            Opt=input("Enter your ans: ").upper()

        print(f"\nDo you want to confirm option {Opt} if yes than enter YES")
        conf=input().upper()
    if(Opt==qust["ANS"] and qust["P"]==10000000000):
        print("\nCorrect Answer!!\nCONGRATULATIONS\n")
        money=qust["P"]
        break;
    elif(Opt==qust["ANS"]):
        print("\nCorrect Answer!!\n")
    else:
        print("\nIncorrect Answer!!\n")
        money=qust["fix"]
        break;

    print(f"\nDo you want to continue or return with {current} RS. if NO than write NO")
    choice=input("Enter your ans: ").upper()
    if(choice=="NO"):
        money=current
        break;
    current=qust["P"]
    print(f"\nNext qustion for rs.{current}")
    
print(f"\n\nYOU HAVE WON {money} RS")
    