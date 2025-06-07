s1 = input ("inserire la stringa s1: ")
s2 = input ("inserire la stringa s2: ")
for i in range (0, len(s1)):
    for j in range (0, len(s2)):
        if s1[i] == s2[j]:
            verifica = True
            break
        else:
            verifica = False
    if verifica == False:
        print (s1[i], end='')
        
