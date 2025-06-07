s=input("inserire una stringa:")
i=0
while i<len(s):

    if ord(s[i])>100:
        print("il primo carattere con Unicode maggiore di 100 è:"+s[i])
        i=len(s)
    else:
        if i==len(s)-1:
            print("stringa consumata e carattere non trovata")

    i+=1
            
