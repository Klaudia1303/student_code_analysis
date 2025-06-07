h = input ('hh: ')
m = input ('mm: ')
s = input ('ss: ')

if h.isdecimal() and m.isdecimal() and s.isdecimal():
    
    a = (int(h)*3600+int(m)*60+int(s))
    print('L\'orario in secondi è:', a) 
else:
    print('Errore! Ricontrolla i dati!')
