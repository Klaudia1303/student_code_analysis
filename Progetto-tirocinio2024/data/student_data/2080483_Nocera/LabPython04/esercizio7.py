s= str(input("scrivere una parola : "))
smax=s[0]
i=1
nmax=s.count(s[0])
if s!="":
    while i<len(s):
        if s.count(s[i])>=nmax:
            smax=s[i]
            nmax=s.count(s[i])

        i=i+1    
    print(smax)
else:
    print("la parola inserita è vuota")
       
        
        
