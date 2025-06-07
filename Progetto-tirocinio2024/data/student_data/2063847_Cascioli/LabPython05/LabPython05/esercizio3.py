s1=input("Inserire la prima stringa")
s2=input("Inserire la seconda stringa")
for i in range (len(s1)):
    if (s1[i]!=s2[i] and s2.find(s1[i])==-1):
        print(s1[i],end="")
    
