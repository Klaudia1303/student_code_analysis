verifica = True
while (verifica == True):
    s = input ("inserire una tsringa s: ")
    s = str (s)
    if ( (s.islower() == True) and (s.isalpha() == True)):
        print(s[0]+s[len(s)-1])
        verifica = False
    else:
        print (s[0]+s[len(s)-1])
