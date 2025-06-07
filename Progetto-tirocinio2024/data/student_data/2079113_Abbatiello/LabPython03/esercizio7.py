c = input('inserisci carattere :')
s = input('inserisci stringa :')
k = 0
l = 0
while k <= 2:
    if l < len(s):
        if s[l] == k:
            k = k + 1
            l = l + 1
             
          
            
          
        else :
            l += 1
    if l == len(s):
        s = input('inserisci stringa : ')

print(k)
        
