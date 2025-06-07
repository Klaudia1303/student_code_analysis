i=False
s=input("inserisci una stringa:")
a=1
if "a" in s and "c" in s:
    print("numero di stringhe:",a)
    i=True
while i==False:
    if "a" in s and "c" in s:
        print("numero di stringhe:",a)
        i=True
    else:
        s=input("inserisci stringa:")
        a+=1
