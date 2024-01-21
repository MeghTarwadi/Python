for t in gtu:
    gtu[t]=float(input(f"{t}   : "))
    
print("\nYOUR GRADES \n")
for t in gtu:
    temp=grades(gtu[t],1)
    print(f"{t}  : {temp}")

for t in gtu:
    gtu[t]=grades(gtu[t])
