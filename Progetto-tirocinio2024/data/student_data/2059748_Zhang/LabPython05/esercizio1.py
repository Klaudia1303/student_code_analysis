s1=input("inserisci una stringa: ")
s2=input("inserisci un'altra stringa della stessa lunghezza: ")

for i in range(len(s1)):
    x=s1[i]+s2[i]
    print(x,end='')
