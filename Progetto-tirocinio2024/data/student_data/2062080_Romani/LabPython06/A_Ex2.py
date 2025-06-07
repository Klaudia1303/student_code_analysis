s=input('Inserire stringa: ')
i=0
liv=0
while i<len(s) and s[i]==s[len(s)-i-1]:
    liv+=1
    i+=1
print('Livello',liv)
