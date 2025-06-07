s=input("inserisci stringa ")
c=input("inserisci stringa ")
t=input("inserisci stringa ")
while len(s)+len(c)!=len(t):
    s=c
    c=t
    t=input("inserisci stringa ")
   
print (s,c,t)
   
    
