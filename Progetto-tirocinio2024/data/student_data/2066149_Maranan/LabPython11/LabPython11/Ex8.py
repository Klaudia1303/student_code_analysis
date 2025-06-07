def Ex8(file):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    l = []
    dM = {'A': 1, 'B': 2, 'C':3, 'D':4, 'E':5, 'H':6, 'L':7, 'M':8, 'P':9, 'R':10, 'S':11, 'T':12}
    patt = r'^[A-Z]{3} ?[A-Z]{3} ?([0-9]{2})([A-Z])([0-9]{2}) ?[A-Z][0-9]{3}[A-Z]$'
    with open (file, encoding='UTF-8') as f:
        for code in f:
            m = re.match(patt, code)
            if m:
                yy = m.group(1)
                mm = m.group(2)
                dd = int(m.group(3))
                if int(yy)<=20:
                    anno = 2000+int(yy)
                else:
                    anno = 1900+int(yy)
                #anno

                if mm in dM:
                    if dM[mm]<10:
                        mese = '0'+str(dM[mm])
                    else:
                        mese = str(dM[mm])
                else:
                    l.append('Mese errato')
                    continue
                #mese

                if 40 < dd <= 71:
                    dd = dd - 40

                if dd <= 31:
                    if (mm=='B' and (dd<= 28)) or (mm in 'ACELMRT' and (dd <= 31)) or (mm in 'DHPS' and (dd <= 30)):
                        if dd<10:
                            giorno = '0'+ str(dd)
                        else:
                            giorno = str(dd)
                    else:
                        l.append('Giorno errato')
                        continue
                else:
                    l.append('Giorno errato')
                    continue
                #giorno
                
                l.append(giorno+'/'+mese+'/'+str(anno))
                continue
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
