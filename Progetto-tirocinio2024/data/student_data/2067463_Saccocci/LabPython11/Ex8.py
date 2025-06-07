def Ex8(file):
    import re
    f=open(file)
    l=[]
    for riga in f:
        pattern=r'\b[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]\b'
        m=re.search(pattern,riga)
        if m:
            mesi = 'ABCDEHLMPRST'
            mese=m.group(2)
            giorno=int(m.group(3))
            anno=m.group(1)
            if giorno>71:
                l.append('Giorno errato')
                continue
            elif giorno==0:
                l.append('Giorno errato')
                continue
            elif 40<giorno<=71:
                giorno=giorno-40
            elif 32<=giorno<=40:
                l.append('Giorno errato')
                continue
            else:
                giorno=giorno
            if mese in mesi:
                mese=mesi.index(mese)+1
                if int(mese)==4 or int(mese)==6 or int(mese)==9 or int(mese)==11:
                    giorni=30
                    if giorno>giorni:
                        l.append('Giorno errato')
                        continue
                    else:
                        if giorno<10:
                            giorno='0'+str(giorno)
                        else:
                            giorno=str(giorno)
                elif int(mese)==2:
                    giorni=28
                    if giorno>giorni:
                        l.append('Giorno errato')
                        continue
                    else:
                        if giorno<10:
                            giorno='0'+str(giorno)
                        else:
                            giorno=str(giorno)
                else:
                    giorni=31
                    if giorno>giorni:
                        l.append('Giorno errato')
                        continue
                    else:
                        if giorno<10:
                            giorno='0'+str(giorno)
                        else:
                            giorno=str(giorno)
                if int(mese)<10:
                    mese='0'+str(mese)
                else:
                    mese=str(mese)
            else:
                l.append('Mese errato')
                continue
            if int(anno)<=20:
                anno='20'+str(anno)
            else:
                if int(anno)<10:
                    anno='190'+str(anno)
                else:
                    anno='19'+str(anno)
            data=str(giorno)+'/'+str(mese)+'/'+str(anno)
            l.append(data)
        else:
            l.append('Codice errato')
            continue
    f.close()
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
