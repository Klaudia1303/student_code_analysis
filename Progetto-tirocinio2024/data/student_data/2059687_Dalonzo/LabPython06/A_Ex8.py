s1 = input('Inserire una stringa: ')
s2 = input('Inserire la seconda stringa: ')
n = int(input('Inserire il valore n :'))
firstPos = -1
lastPos = -1
final = ''
for i in range(0,len(s1)):
    carattere = s1[i]
    for c in range(0,len(s2)):
        
        if(s2[c] == carattere):
            if(abs((i + 1) - (c + 1)) <= n):
                final += carattere

print(final)