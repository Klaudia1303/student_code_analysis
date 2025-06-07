s1=input("Inserisci 2 stringhe della stessa lunghezza: ")
s2=input("Inserisci 2 stringhe della stessa lunghezza: ")
while len(s1)!=len(s2):
    s1=input("Inserisci 2 stringhe della stessa lunghezza: ")
    s2=input("Inserisci 2 stringhe della stessa lunghezza: ")
c=''
for i in range(len(s1)):
    c=c+s1[i]+s2[i]
print(c)

