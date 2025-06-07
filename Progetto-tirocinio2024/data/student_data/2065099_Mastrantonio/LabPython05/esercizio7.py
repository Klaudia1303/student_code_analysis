s = input('Inserisci una stringa: ')
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            val = True
            break
        else:
            val= False
    if val == True :
        break
print(val)
