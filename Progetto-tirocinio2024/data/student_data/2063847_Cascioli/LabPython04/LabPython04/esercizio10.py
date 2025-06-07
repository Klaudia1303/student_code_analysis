s=input("Inserire la stringa")
p=''
s1=''
while(len(s1+p)!=len(s)):
    s1=p
    p=s
    s=input("Inserire la stringa")

print(s1,p,s)
    
