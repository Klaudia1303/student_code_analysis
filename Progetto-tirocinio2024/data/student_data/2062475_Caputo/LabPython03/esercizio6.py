s = input ("inserire la stringa s: ")
i = 0
while i < len(s):
    if (ord (s[i]) > 100):
        print ("il primo carattere con unicode maggiore di 100 è:",s[i])
        break
    i = i+1
if (i == len (s)):
    print ("stringa consumata e carattere non trovato")
