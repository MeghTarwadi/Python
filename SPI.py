def grades(marks,ret=0,dif=0):
    if dif==0:
        if(ret==1):
            if marks>26:
                return 'AA'
            elif marks>22:
                return 'AB'
            elif marks>18:
                return 'BB'
            elif marks>16:
                return 'BC'
            elif marks>14:
                return 'CC'
            elif marks>12:
                return 'CD'
            else:
                return 'DD'
        else:
            if marks>26:
                return 10.00
            elif marks>22:
                return 9.00
            elif marks>18:
                return 8.00
            elif marks>16:
                return 7.00
            elif marks>14:
                return 6.00
            elif marks>12:
                return 5.00
            else:
                return 4.00
    else:
        if(ret==1):
            if marks>62:
                return 'AA'
            elif marks>55:
                return 'AB'
            elif marks>48:
                return 'BB'
            elif marks>41:
                return 'BC'
            elif marks>34:
                return 'CC'
            elif marks>27:
                return 'CD'
            elif marks>22:
                return 'DD'
            else:
                return 'FF'
        else:
            if marks>62:
                return 10.00
            elif marks>55:
                return 9.00
            elif marks>48:
                return 8.00
            elif marks>41:
                return 7.00
            elif marks>34:
                return 6.00
            elif marks>27:
                return 5.00
            elif marks>22:
                return 4.00
            else:
                return 3.00

print("\nENTER MARKS IN MID (Highest) \n")

gtu = {"etc ": (0.0), "ps  ": (0.0), "ds  ": (0.0), "dbms": (0.0), "df  ": (0)}
   
for t in gtu:
    gtu[t]=float(input(f"{t}   : "))
    
print("\nYOUR GRADES \n")
for t in gtu:
    temp=grades(gtu[t],1)
    print(f"{t}  : {temp}")

for t in gtu:
    gtu[t]=grades(gtu[t])

print("\nENTER MARKS IN GTU (that you think but you always get less) \n")
sub = {"etc ": (0.0), "ps  ": (0.0), "ds  ": (0.0), "dbms": (0.0), "df  ": (0.0)}
for t in sub:
    sub[t]=float(input(f"{t}   : "))

print("\nYOUR GRADES \n")
for t in sub:
    temp=grades(sub[t],1,1)
    print(f"{t}  : {temp}")

for t in sub:
    sub[t]=grades(sub[t],0,1)

final=0.0
n=1.0
avg=0.0

print("\nENTER CREDITS OF PRACTICLE LIKE 10 FOR AA, 8 FOR BB , 6 FOR CC , 9 FOR AB...\n")
prac = {"etc ": (10), "ps  ": (0.0), "ds  ": (10.0), "dbms": (10.0), "df  ": (10.0)}
credits = {"etc ": (3.0), "ps  ": (5.0), "ds  ": (5.0), "dbms": (5.0), "df  ": (4.0)}
for t in prac:
    if(prac[t]!=0):
        prac[t]=float(input(f"{t}   : "))



for s in sub:
    credit=credits[s]
    n=n+credits[s]
    avg=(sub[s]+gtu[s])/2
    if(prac[s]!=0):
        avg=(avg+prac[s])/2
    final=(avg*credit) + final
    
final=(final/n) + (10/23)
print(f"YOR SPI {final}")