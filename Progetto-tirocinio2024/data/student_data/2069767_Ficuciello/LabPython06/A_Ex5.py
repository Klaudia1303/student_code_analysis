s=input('Inserire una stringa alfanumerica:')
n=0
for i in range(len(s)-1,-1,-1):
    if s[i]==s[i-1]:
        i-=1
        print(s[i], s.count(s[i]))
        
