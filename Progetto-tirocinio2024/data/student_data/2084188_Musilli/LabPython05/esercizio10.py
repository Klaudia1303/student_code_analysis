b=True
while b:
    lato=int(input("Inserire la misura del lato del \
quadrato (>=2): "))
    if lato>=2: b=False
    else:   print("\n\tValore inserito non valido! Deve essere >=2\n")
if lato%2==0: k=lato//2; g=(lato//2)-1; b=True
else:   k=(lato//2); g=(lato//2); b=False
if b:
    for i in range(k):  #prima metà pari
        if i==0: s="*"*(lato//2); c=-1;   s+=s[-1::-1]; print(s)
        else:   s="*"+((" "*c)+"*"+(" "*g)); s+=s[-1::-1]; print(s)
        c+=1; g-=1
    c-=1; g+=1
    for i in range(k) : #seconda metà pari
        if i==(k-1):s="*"*(lato//2); s+=s[-1::-1]; print(s)
        else: print(s); c-=1; g+=1; s="*"+((" "*c)+"*"+(" "*g)); s+=s[-1::-1]
elif not b:
    for i in range(k):  #prima metà dispari
        if i==0: s1="*"*(lato//2); s=s1+"*"; c=-1;   s+=s1[-1::-1]; print(s)
        else:   s1="*"+((" "*c)+"*"+(" "*g)); s=s1; s+=s1[-2::-1]; print(s)
        if c!=k: c+=1; g-=1
        else: c+=2; g=0         #centro dispari
    s1="*"+((" "*c)+"*"+(" "*g)); s=s1; s+=s1[-2::-1]; print(s) 
    for i in range(k) : #seconda metà dispari
        if i==(k-1):s1="*"*(lato//2); s=s1+"*"; s+=s1[-1::-1]; print(s)
        else: c-=1; g+=1; s1="*"+((" "*c)+"*"+(" "*g)); s=s1; s+=s1[-2+k+1::-1]; print(s)
