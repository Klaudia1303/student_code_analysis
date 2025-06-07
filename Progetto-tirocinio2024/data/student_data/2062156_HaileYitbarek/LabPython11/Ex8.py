def Ex8(file):
    l=[]
    f=open(file,encoding='UTF-8')
    d={'A':'01','B':'02','C':'03','D':'04','E':'05','H':'06','L':'07','M':'08','P':'09','R':'10','S':'11','T':'12'}
    pattern=r'[A-Z]{3} ?[A-Z]{3} ?([0-9])([0-9])([A-Z])([0-9])([0-9]) ?[A-Z][0-9]{3}[A-Z]'
    for riga in f:
        r=riga.strip()
        m=re.match(pattern,riga)
        aa=m.group(1)+m.group(2)
        anno=int(aa)
        mese=m.group(3)
        gg=m.group(4)+m.group(5)
        giorno=int(gg)
        if m:
            if anno<=20:
                anno='20'+str(anno)
            if anno>20:
                anno='19'+str(anno)
            if mese not in d:
                l.append('Mese errato')
            if giorno>71:
                l.append('Giorno errato')
            if mese in d:
                if mese=='B':
                    if 28<giorno<41 or 68<giorno:
                        l.append('Giorno errato')
                    else:
                        if 1<=giorno<=28:
                            l.append(gg+'/'+d['B']+'/'+anno)
                        if 41<=giorno<=68:
                            giorno=giorno-40
                            l.append(gg+'/'+d['B']+'/'+anno)
                if 31<giorno<41 or 71<giorno:
                    l.append('Giorno errato')
                else:
                    if 1<=giorno<=31:
                        l.append(gg+'/'+d[mese]+'/'+anno)
                    if 41<=giorno<=71:
                        giorno=giorno-40
                        l.append(gg+'/'+d[mese]+'/'+anno)
        else:
            l.append('Codice errato')
        m=0
        aa=0
        mese=0
        gg=0
        return l
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
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
