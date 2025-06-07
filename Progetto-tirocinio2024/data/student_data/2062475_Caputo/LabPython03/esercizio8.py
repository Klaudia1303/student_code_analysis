verifica = False
while verifica == False:
    s = input ("inserire una stringa palindroma: ")
    if ( s == s[::-1] ):
        print ("stringa palindroma di lunghezza:", len (s))
        verifica = True
    else:
        print ("la stringa inserita non è palindroma, inserirne un\'altra") 
        verifica = False
