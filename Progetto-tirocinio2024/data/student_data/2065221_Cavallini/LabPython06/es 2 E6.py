s = input('inserisci una stringa: ')
s2 = s[::-1] 
var = 0
for i in range (len(s)):
    if s[i]==s2[i]:
        var+=1
    else:
        break
print(var)
