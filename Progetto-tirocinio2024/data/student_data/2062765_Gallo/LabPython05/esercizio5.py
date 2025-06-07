s=input("Inserisci stringa: ")
n=int(input("Inserisci numero: "))
finito=False
i=0
while not finito:
    if n<len(s):
        if s[i]==s[n]:
            print("True")
            finito=True
        else:
            i+=1
            n+=1
    else:
        print("False")
        finito=True
    
