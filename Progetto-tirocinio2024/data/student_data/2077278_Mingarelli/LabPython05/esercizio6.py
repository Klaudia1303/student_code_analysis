s=input('inserisci una stringa')
l=0
for i in range(len(s)):
    if (s.rfind(s[i])-s.find(s[i]))>l:
        l=s.rfind(s[i])-s.find(s[i])
print(l)
        
