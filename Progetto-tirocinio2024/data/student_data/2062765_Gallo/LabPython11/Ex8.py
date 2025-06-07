def Ex8(file):
    f=open(file,encoding='UTF-8')
    l=[]
    patternvalido=r'\b[A-Z]{3} ?[A-Z]{3} ?[0-9]{2}([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]\b'
    for riga in f:
        dati="".join(riga.split())
        if re.match(patternvalido,riga) and len(dati)==16:
            giorno=int(dati[9:11])
            mese=dati[8]
            anno=int(dati[6:8])
            err=0
            if mese=="A" or mese=="B" or mese=="C" or mese=="D" or mese=="E" or mese=="H" or mese=="L" or mese=="M" or mese=="P" or mese=="R" or mese=="S" or mese=="T":
                if mese=="A":
                    mese="01"
                elif mese=="B":
                    mese="02"
                elif mese=="C":
                    mese="03"
                elif mese=="D":
                    mese="04"
                elif mese=="E":
                    mese="05"
                elif mese=="H":
                    mese="06"
                elif mese=="L":
                    mese="07"
                elif mese=="M":
                    mese="08"
                elif mese=="P":
                    mese="09"
                elif mese=="R":
                    mese="10"
                elif mese=="S":
                    mese="11"
                elif mese=="T":
                    mese="12"
                    
                if giorno>40:
                    giorno=giorno-40
                    if giorno<10:
                        giorno="01"
                if mese=="02" and int(giorno)>28:
                    l.append('Giorno errato')
                    err+=1
                elif (mese=="11" or mese=="04" or mese=="06" or mese=="09") and int(giorno)>30:
                    l.append('Giorno errato')
                    err+=1
            else:
                l.append('Mese errato')
                err+=1   
            if anno<=20:
                anno+=2000
            else:
                anno+=1900
            if err==0:
                m=(str(giorno) + "/"+ str(mese) +"/"+ str(anno))
                l.append(m)
        else:
            l.append('Codice errato')
    return l
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
