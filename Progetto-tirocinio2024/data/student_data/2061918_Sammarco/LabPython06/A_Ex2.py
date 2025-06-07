s=input("inserisci una stringa palindroma:")
r=0
g=-1
for i in range(len(s)//2):
    if s[i]==s[g]:
        r+=1
        g-=1
if r==len(s)//2:
    print("stringa totalmente palindroma")
else:
    print("stringa palindroma di tipo:",r)
    
    
