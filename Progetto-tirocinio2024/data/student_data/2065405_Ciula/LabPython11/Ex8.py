def Ex8(file):
    f=open(file, encoding='UTF-8')
    pattern=r'\b[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]\b'
    l=[]
    for elem in f:
        verifica=re.match(pattern, elem)
        if verifica:
            a=verifica.group(1)
            if int(a)<=20:
                anno='20'+a
            else:
                anno='19'+a
            m=verifica.group(2)
            if m=='A':
                mese='01'
            elif m=='B':
                mese='02'
            elif m=='C':
                mese='03'
            elif m=='D':
                mese='04'
            elif m=='E':
                mese='05'
            elif m=='H':
                mese='06'
            elif m=='L':
                mese='07'
            elif m=='M':
                mese='08'
            elif m=='P':
                mese='09'
            elif m=='R':
                mese='10'
            elif m=='S':
                mese='11'
            elif m=='T':
                mese='12'
            else:
                l.append('Mese errato')
                continue
            
            g=verifica.group(3)
            if int(g)>40:
                g=int(g)-40
        
            if (m=='A' and int(g)<=31) or (m=='B' and int(g)<=28) or (m=='C' and int(g)<=31) or (m=='D' and int(g)<=30) or (m=='E' and int(g)<=31) or (m=='H' and int(g)<=30) or (m=='L' and int(g)<=31) or (m=='M' and int(g)<=31) or (m=='P' and int(g)<=30) or (m=='R' and int(g)<=31) or (m=='S' and int(g)<=30) or (m=='T' and int(g)<=31):
                giorno= g
                if len(str(giorno))==1:
                    giorno='0'+str(giorno)
            else:
                l.append('Giorno errato')
                continue

            l.append(str(giorno)+'/'+str(mese)+'/'+str(anno))
            
        else:
            l.append('Codice errato')
            continue
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
