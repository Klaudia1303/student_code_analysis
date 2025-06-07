s1=input("Inserire la prima stringa: ")
s2= input("Inserire la seconda stringa: ")
n= int(input("Inserire un numero intero positivo: "))
lettere = " "
for i in range(len(s1)):
        c1= s1[i]
        c2= s2[i-n:i+n]
        find=c2.find(c1)
        if find>-1:
                lettere+=c2[find]
print(lettere)
                    
