s1 = input("Inserire una stringa non vuota:")
s2 = input("Inserire una stringa non vuota:")
n = int(input("Inserire un numero:"))

s_new = " "

for i in range(len(s1)):
    if (i - n > 0):
        inf = i - n
    else :
        inf = 0
    if(i + n < len(s2)):
        sup = i + n 
    else:
        sup = len(s2) - 1
        
    for j in range(inf, sup + 1):
        if s1[i] == s2[j]:
            s_new += s1[i]
            break

print(s_new)
