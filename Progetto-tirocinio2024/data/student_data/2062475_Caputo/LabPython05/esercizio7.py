s = input ("inserire la stringa s: ")
for i in range (0, len(s)):
    for j in range (0, len(s)):
        if ( i != j and s[i] == s[j]):
            verifica = True
            break
        else:
            verifica = False
    if verifica == True:
        print (verifica)
        break
if verifica == False:
    print (verifica)
    
        
