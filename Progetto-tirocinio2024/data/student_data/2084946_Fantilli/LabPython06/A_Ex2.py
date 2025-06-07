s=input()
p=0
i=0
while s[i]==s[len(s)-i-1] and i<len(s)/2:
    p+=1
    i+=1
if i<len(s)//2:
    print("Livello di palindromicità della stringa:",p)
elif i>=len(s)//2:
    print("Livello di palindromicità della stringa:",len(s))
