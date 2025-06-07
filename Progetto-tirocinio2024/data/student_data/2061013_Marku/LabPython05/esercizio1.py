s=input("inserisci una stringa: ")
r=input("inserisci una stringa della stessa lunghezza della precedente: ")
if len(s)!=len(r):
    print('lunghezze stringhe diverse')
else:
    for i in range(len(s)):
        print(s[i]+r[i],end='')
       
