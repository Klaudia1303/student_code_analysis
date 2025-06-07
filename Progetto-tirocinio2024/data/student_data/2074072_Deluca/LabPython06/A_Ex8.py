s1=input("stringa a: ")
s2=input("stringa b: ")
n=int(input("numero: "))
s=""
for i in range(len(s1)-n):
    if i-n>0:
        if s2[i-n:i+n].find(s[i])!=-1 :
            s+=s[i]
print(s)
        
    
