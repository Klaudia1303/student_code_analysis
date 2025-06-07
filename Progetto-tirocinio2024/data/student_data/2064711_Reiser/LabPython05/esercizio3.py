s=str(input("inserisci una stringa:"))
t=str(input("inserisci una stringa:"))

for i in range (0,len(s)):
    printchar=1
    for j in range(0,len(t)):
        if s[i]==t[j]:
            printchar=0
    if printchar==1:
        print(s[i],end="")
            

                   
                   
