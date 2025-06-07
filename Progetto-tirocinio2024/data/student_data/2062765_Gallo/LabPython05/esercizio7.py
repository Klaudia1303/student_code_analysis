s=input("Inserisci stringa: ")
finito=False
i=0
while not finito:
    if i<len(s)-1:
        if s.count(s[i])>1:
            print(True)
            finito=True
        else:
            i+=1
    else:
        print(False)
        finito=True
        
