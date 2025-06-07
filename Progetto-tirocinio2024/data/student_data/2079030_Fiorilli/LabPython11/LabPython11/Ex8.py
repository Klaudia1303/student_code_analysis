def Ex8(file):
    f=open(file, encoding='UTF-8')
    riga=f.readline().strip()
    mesi='ABCDEHLMPRST'
    L=[]
    patt=r'[A-Z]{3} ?[A-Z]{3} ?(\d{2}) ?([A-Z]) ?(\d{2}) ?[A-Z] ?\d{3} ?[A-Z]'
    while len(riga)>0:
        if not re.match(patt, riga):
            L.append('Codice errato')
        else:
            cod=re.match(patt, riga)
            if cod.group(2) not in mesi:
                L.append('Mese errato')
            elif int(cod.group(3))>71 or 31<int(cod.group(3))<41 or \
            (int(cod.group(3))==31 and cod.group(2) not in 'ACELMRT') or \
            (28<int(cod.group(3))<31 and cod.group(2)=='B'):
                L.append('Giorno errato')
            else:
                if int(cod.group(1))>20:
                    anno='19'+cod.group(1)
                else:
                    anno='20'+cod.group(1)
                giorno=int(cod.group(3))
                if giorno>31:
                    giorno=giorno-40
                giorno=str(giorno)
                if len(giorno)==1:
                    giorno='0'+giorno
                mese=str(int(mesi.find(cod.group(2)))+1)
                if len(mese)==1:
                    mese='0'+mese
                data=giorno+'/'+mese+'/'+anno
                L.append(data)
        riga=f.readline()
    return L
                
            
            
    
    
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
