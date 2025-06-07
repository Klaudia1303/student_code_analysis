s=input("inserisci stringa ")
i=0
ri=0
c=""
while i<len(s)-1:
    i+=1
    if s.count(s[i])>=ri:
       ri=s.count(s[i])
       c=s[i]
print(c)
    
