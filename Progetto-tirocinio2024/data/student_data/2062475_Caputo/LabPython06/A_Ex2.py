s = input ("inserire la stringa s: ")
somma = 0
for i in range ( 0, int((len(s))/2) ):
    if ( s[i] == s[(len(s)-1)-i]):
        somma = somma + 1
    else:
        break
if ( somma == int ( len(s)/2 ) ):
     print ("la stringa s è palindroma di livello:", somma*2)
else:
    print ("la stringa s è palindroma di livello:", somma)
    
