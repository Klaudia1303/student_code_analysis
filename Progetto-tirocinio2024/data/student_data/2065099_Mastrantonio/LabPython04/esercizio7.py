s = input ('Inserisci una stringa :')
i= len(s)-1
conta = 0 
while i != 0:
    if s.count(s[i]) > conta:
        conta = s.count (s[i])
        i = i - 1
        cara = s[i]
    else :
        i = i-1
print (cara)
