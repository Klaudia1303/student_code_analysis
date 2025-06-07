def A_Ex4(fileName):
    f=open(fileName, encoding='UTF-8')
    s=f.readline()
    riga=f.readline()
    dati=riga.strip().split(',')
    d={}
    while len(riga)>0:
        conta=0
        if int(dati[1])>=18:
            conta+=1
            if int(dati[0]) in d:
                d[int(dati[0])]=d.get(int(dati[0]))+1
            else:
                d[int(dati[0])]=conta
        riga=f.readline()
        dati=riga.strip().split(',')    
    f.close()
    return d




    
   # """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################


"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ["esami1.csv"] , {1345: 1, 1346: 1, 1896: 1, 1753: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami2.csv"] , {1346: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami3.csv"] , {1347: 2, 1348: 1, 1349: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami4.csv"] , {1100: 1, 1012: 1, 1021: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami5.csv"] , {1345: 1, 1987: 1, 1346: 1, 1896: 1})

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
