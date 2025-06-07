s = input('Inserisci una stinga alfanumerica non nulla: ')

count = 0
carattere = ''
maxocc = 0
ultimo = ''

for i in range(1,len(s)):
    

    if s[i-1] == s[i] or s[len(s)-1] == ultimo:
        count += 1
        ultimo = s[i]
        
    if count > maxocc or (s[len(s)-1] == ultimo and count+1>maxocc):
        maxocc = count
        carattere = s[i]
        

    elif s[i-1] != s[i] or not s[len(s)-1]:
        count = 0

    
              
print(carattere,maxocc+1)


    
    
