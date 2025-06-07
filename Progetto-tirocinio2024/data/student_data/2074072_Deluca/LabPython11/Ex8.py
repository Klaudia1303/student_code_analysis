def Ex8(file):
    f= open(file, encoding="UTF-8")
    l=[]
    pattern="([A-Z][A-Z][A-Z])[ ]*([A-Z][A-Z][A-Z])[ ]*([0-9][0-9])([A-Z])([0-9][0-9])[ ]*([A-Z])[0-9][0-9][0-9][A-Z]"
    for line in f:
        elem=line.strip()
        l.append(elem)
    l1=[]
    d={"A":("01", 31), "B":("02", 28), "C":("03",31), \
       "D":("04",30), "E":("05",31), "H":("06",30), \
       "L":("07",31), "M":("08",31), "P":("09", 30), \
       "R":("10", 31), "S":("11",30), "T":("12",31)}
    for elem in l:
        s=[]
        m= re.search(pattern, elem)
        if m:
            if int(m.group(3))<=20:
                s="/20"+m.group(3)
            else:
                s="/19"+m.group(3)
            if m.group(4) in d:
                s= "/"+d[m.group(4)][0]+s
            else:
                l1.append("Mese errato")
                continue
            if int(m.group(5))>=40:
                giorno=int(m.group(5))-40
                fem=True
            else:
                fem=False
                giorno=int(m.group(5))
            if giorno==0 or giorno> d[m.group(4)][1]:
                l1.append("Giorno errato")
                continue
            else:
                s=m.group(5)[1]+s
                if fem:
                    s=str(int(m.group(5)[0])-4)+s
                else:
                    s=m.group(5)[0]+s
            l1.append(s)
        else:
            l1.append("Codice errato")
            
    return l1
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
##############################################################################

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
