s1=input("Inserisci prima stringa: ")
s2=input("Inserisci seconda stringa :")
new=''
for i in range(len(s1)):
    if s2.find(s1[i])==-1:
        new=new+s1[i]
print(new)
