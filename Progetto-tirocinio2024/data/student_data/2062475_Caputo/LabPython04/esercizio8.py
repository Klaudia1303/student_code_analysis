s1 = input ("inserire la stringa s1: ")
s2 = input ("inserire la stringa s2: ")
if ( s1[len(s1)-1] == s2[0]):
        verifica = False
else:
    verifica = True
while verifica:
    s = input ("inserire una stringa s: ")
    if ( s2[len(s2)-1] == s[0]):
        break
    s2 = s
print (s2, s)
    
