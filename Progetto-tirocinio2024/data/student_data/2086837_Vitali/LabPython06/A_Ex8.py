s1=input("Inserisci prima stringa :")
s2=input("Inserisci seconda stringa :")
n=int(input("Inserisci numero intero :"))
new=''
for i in range(len(s1)):
    if (i-n)<=s2.find(s1[i])<=(i+n) and s2.find(s1[i])!=-1:
        new +=s1[i]
print(new)
      
