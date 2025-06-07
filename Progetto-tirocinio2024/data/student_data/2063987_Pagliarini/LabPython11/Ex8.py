def Ex8(file):
    f=open(file,encoding='UTF-8')
    l=[]
    mesi={'A':'01','B':'02','C':'03','D':'04','E':'05','H':'06','L':'07','M':'08','P':'09','R':'10','S':'11','T':'12'}
    giornimesi={'A':'31','B':'28','C':'31','D':'30','E':'31','H':'30','L':'31','M':'31','P':'30','R':'31','S':'30','T':'31'}
    for i in f:
        i="".join(i.strip().split())
        print(i)
        patt=r'\b[A-Z]{3}[A-Z]{3}([0-9]{2})([A-Z])([0-9]{2})[A-Z][0-9]{3}[A-Z]\b'
        if not re.search(patt,i):
            l.append('Codice errato')
            continue
        else:
            m=re.search(patt,i)
            anno=m.group(1)
            mese=m.group(2)
            giorno=m.group(3)
            if int(anno)<=20:
                data='20'+str(anno)
            else:
                data='19'+str(anno)
            if mese not in mesi:
                l.append('Mese errato')
                continue
            else:
                data=mesi[mese]+'/'+data
                if int(giorno)>40:
                    giorno=int(giorno)-40
                if int(giorno)<1 or int(giorno)>int(giornimesi[mese]):
                    l.append('Giorno errato')
                    continue
                else:
                    giorno=str(giorno).zfill(2)
                    data=str(giorno)+'/'+data
                    l.append(data)
    f.close()
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
