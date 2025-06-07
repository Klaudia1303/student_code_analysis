def A_Ex5(filename,oggetto):
    fin=open(filename, encoding="UTF-8"); d={}
    riga1=fin.readline().strip().split(",");
    anno=[int(r) for r in riga1[1:]]
    for elem in fin:
        elem=elem.strip().split(","); mas=elem[1]; d[elem[0]]=anno[0]
        for c in elem:
            if not(c.isalpha()) and mas<c:   d[elem[0]]=anno[elem.index(c)-1]
    fin.close()
    return d.get(oggetto)
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
