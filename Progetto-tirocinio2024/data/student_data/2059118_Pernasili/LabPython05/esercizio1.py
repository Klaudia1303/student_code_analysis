
s1=input("Inserisci una stringa: ")
s2=input("Inserisci una stringa: ")
i=0
ss=''
x = range(len(s1))
for i in x:
    ss=ss+s1[i]
    ss=ss+s2[i]
print(ss)
