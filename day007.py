import random


#---------------------------------
#   Test func to check indexes   |
#   are correct or not           |
#---------------------------------

def test(chosen):
    ip=input("Guess a Character: ")[0].upper()
    i=0
    indexes = set()
        
    while i<len(chosen):
        if ip==chosen[i]:
            indexes.add(i)
        i+=1
    return indexes

def reveal(sets,character):
    temp=[]
    output=""
    for t in range(0,len(character)):
        temp.append(" _ ")
    for i in character:
        for j in sets:
            if i==character[j]:
                temp[j]=" "+i+" "
    for t in range(0,len(character)):
        output=output+temp[t]

    return output



retry = True
while retry:


    #---------------------------------
    #   RANDOM CHOSEN                |
    #---------------------------------

    characters = ['Jiraiya', 'Sasuke Uchiha', 'Naruto Uzumaki', 'Tsunade Senju', 'Kakashi Hatake', 'Sakura Haruno', 'Shikamaru Nara', 'Choji Akamichi', 'Ino Yamanaka', 'Asuma Sarutobi', 'Hiruzen Sarutobi', 'Hinata Hyuga', 'Neji Hyuga', 'Rock Lee', 'Tenten', 'Might Guy', 'Kurenai', 'Shino Aburame', 'Kiba Inuzuka', 'Gaara', 'Temari', 'Kankuro', 'Konohamaru Sarutobi', 'Minato Namikaze', 'Kushina Uzumaki', 'Shisui Uchiha', 'Yahiko', 'Hagoromo Otsutsuki', 'Hamura Otsutsuki', 'Ashura Otsutsuki', 'Indra Otsutsuki', 'Nine Tails Kurama', 'Hashirama Senju', 'Tobirama Senju', 'Orochimaru', 'Kabuto Yakushi', 'Nagato Uzumaki', 'Itachi Uchiha', 'Kisame Hoshigaki', 'Deidara', 'Sasori', 'Hidan', 'Kakuzu', 'Pain', 'Konan', 'Black Zetsu/White Zetsu', 'Obito Uchiha', 'Madara Uchiha','Kaguya Otsutsuki']
    chosen = characters[random.randint(0,len(characters)-1)].upper()


    #---------------------------------
    #   HP and checks whether are    |
    #   repeated or not              |
    #---------------------------------

    hp=5
    before=set()
    after=set()
    while hp != 0:
        ans = reveal(before,chosen)
        print(f"\n\n{ans}\n")
        check=test(chosen)
                
        #---------------------------------
        #   check repeated or not        |
        #   and also gives ans reveal    |
        #---------------------------------
        after=after.union(check)
        if after!=before:
            before=after
            print("\nYou guessed correctly\n")
        else:
            print("\nWrong guessed")
            hp-=1
            print(f"Remaining HP {hp} \n")
            if hp==0:
                print(f"\nSorry you have lost this battle \nThe character you are guessing is {chosen}")
                break
        
        
        if reveal(before,chosen)==reveal(before,chosen).replace("_", " _ "):
            print("\nCongratulations you have guessed it correctly\n")
            break
        
        
    reply=input("Do you want to play this game again(y or Y/n or N): ")
    if reply.upper()!="Y":
        retry=False