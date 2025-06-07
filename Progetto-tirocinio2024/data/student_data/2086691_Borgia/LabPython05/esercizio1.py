s1=input("Inserire la prima stringa: ")
s2=input("Inserire la seconda stringa: ")
stot=''
if len(s1)!=len(s2):
    print("Le stringhe devono essere di uguale lunghezza")
for i in range(len(s1)):
    stot=stot+s1[i]+s2[i]
print(stot)
