i=1
s=input("inserisci una stringa: ")
l=input("inserisci una stringa: ")
k=input("inserisci una stringa: ")
while i!=2:
    if(len(s)+len(l)==len(k)) and i!=2:
        print(s,l,k)
        i+=1
    if i!=2:
        s=input("inserisci una stringa: ")
    if (len(l)+len(k)==len(s)) and i!=2:
        print(l,k,s)
        i+=1
    if i!=2:
        l=input ("inserisci una stringa: ")
    if (len(k)+len(s)==len(l)) and i!=2:
        print(k,s,l)
        i+=1
    if i!=2:
        k=input("inserisci una stringa: ")

