s1=''
s2=' '
while(len(s1)!=len(s2)):
    print("Inserire due stringhe della stessa lunghezza")
    s1=input("Inserire la prima stringa")
    s2=input("Inserire la seconda stringa")
for i in range (len(s2)):
    print(s1[i],s2[i])
