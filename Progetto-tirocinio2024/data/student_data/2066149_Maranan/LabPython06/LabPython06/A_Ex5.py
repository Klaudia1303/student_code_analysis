s = input('Inserisci una stringa: ')
n = 0
a = ''
if s.isalnum() and len(s)>0:
    for i in range(len(s)):
        if s.count(s[i]) >= n:
            n = s.count(s[i])
            a = s[i]
    print(a, n)
            
    
