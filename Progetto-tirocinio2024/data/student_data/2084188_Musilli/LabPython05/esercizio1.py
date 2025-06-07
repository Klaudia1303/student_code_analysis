s1=input("Inserire una stringa: ")
b=True
while b:
    s2=input("Inserire una seconda stringa con lunghezza pari alla prima: ")
    if len(s1)!=len(s2):    print("\n\t\tLa seconda stringa non ha lunghezza \
 pari alla prima!\n")
    else:   b=False
s=""
for i in range(len(s1)):
    s+=s1[i]+s2[i]
print("Stringhe iniziali: \n\t",s1,"\t",s2,"\nStringa finale: ",s)
