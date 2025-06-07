def Ex8(file):
    f=open(file,encoding="UTF-8")
    s=f.readlines()
    l=[]
    pattern=r"\b[A-Z]{3} ?[A-Z]{3} ?(\d\d)([A-Z])(\d\d) ?[A-Z]\d\d\d[A-Z]\b"
    mesi={"A":["01",31],"B":["02",28],"C":["03",31],"D":["04",30],"E":["05",31],"H":["06",30],"L":["07",31],"M":["08",31],"P":["09",30],"R":["10",31],"S":["11",30],"T":["12",31]}
    for i in s:
        elem=re.search(pattern,i)
        if elem:
            if int(elem.group(1))<=20:
                anno=str(2000+int(elem.group(1)))
            else:
                anno=str(1900+int(elem.group(1)))
            if elem.group(2) in mesi:
                mese=mesi[elem.group(2)][0]
                giorno=int(elem.group(3))
                if giorno>40:
                    giorno=giorno-40
                if 0<giorno<mesi[elem.group(2)][1]:
                    if giorno>9:
                        giorno=str(giorno)
                    else:
                        giorno="0"+str(giorno)
                    data=giorno+"/"+mese+"/"+anno
                else:
                    data="Giorno errato"
            else:
                data="Mese errato"
        else:
            data="Codice errato"
        l.append(data)
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
