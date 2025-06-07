s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
for i in range(len(s1)):
    if s2.find(s1[i])==True:
        print("",end="",sep="")
    else:
        print(s1[i],sep="",end="")
