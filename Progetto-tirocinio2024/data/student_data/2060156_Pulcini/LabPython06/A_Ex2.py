s=input('inserire una stringa:')
livello=0
i=0

while i<len(s):
    
    if s[i]==s[len(s)-1-i]:
        livello+=1
    i+=1
    if i>len(s)//2-1:
        break
print(livello)
