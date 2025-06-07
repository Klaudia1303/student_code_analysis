s=input('inserisci stringa:')
i=1
x=True
a=0
while i<int(len(s)/2)+1 and x==True:
    if s[i-1]==s[len(s)-i]:
        x=True
        a+=1
    else:
        x=False
    i+=1
if a==int(len(s)/2):
    a=len(s)
print("la stringa è palindroma di livello",a)

        

        
