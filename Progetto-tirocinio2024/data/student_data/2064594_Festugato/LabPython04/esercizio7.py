s= input('inserisci una stringa: ')
i = 0
c = 0
m = 0
l = ''
while i>= 0 and i<len(s):
    c = s.count(s[i])
    if c>=m:
        m = c
        l = s[i]
    i+=1
print(l)
    
    
    
