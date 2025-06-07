s=input('inserisci una stringa')
n=int(input('inserisci un numero'))
for c in range(len(s)):
    for d in range(len(s)):
        if (s[c]==s[d]) and (c-d==n):
            print(s[c])
            print ('True')                    
else:
    print('False')
            
            
    
