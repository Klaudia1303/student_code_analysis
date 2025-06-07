s1=input("Inserisci stringa: ")
s2=input("Inserisci stringa: ")
finito=False
while not finito:
    if s1[len(s1)-1]==s2[0]:
        
        finito=True
    else:
        s1=s2
        s2=input("Inserisci stringa: ")
print(str(s1)+" "+str(s2))
