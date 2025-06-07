s=input("Inserire una stringa: ")
c=0
for i in range(len(s)//2):
    if(s[i]==s[len(s)-i-1]):
        c=c+1
    else:
        break
if(c==len(s)//2):
    c=c*2
    if(len(s)%2!=0):
        c=c+1
print("La stringa è una palindroma di livello: ",c)
