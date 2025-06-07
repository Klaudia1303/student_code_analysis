s=input("Inserisci stringa: ")
finito=False
n=0
while not finito:
    n+=1
    if s.find("a")>=0:
        if s.find("c")>=0:
            print(n)
            finito=True
        else:
            s=input("Inserisci stringa: ")
    else:
        s=input("Inserisci stringa: ")
    
    
    
