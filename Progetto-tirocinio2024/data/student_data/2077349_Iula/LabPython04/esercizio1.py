s=input("Inserisci una stringa: ")
i=0
controllo=False
while controllo==False:
    if s.count("c")>0 and s.count("a")>0:
        controllo=True
    else:
        s=input("Inserisci una stringa: ")
    i+=1
print(i)



