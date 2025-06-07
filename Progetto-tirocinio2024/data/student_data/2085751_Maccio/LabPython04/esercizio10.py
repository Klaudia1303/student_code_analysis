s=input("Inserire una stringa:  ")
g=input("Inserire una stringa:  ")
t=input("Inserire una stringa:  ")
while len(s)+len(g)!=len(t):
    s=g
    g=t
    t=input("Inserire una stringa:  ")
print(s,g,t)
    
    
