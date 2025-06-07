def A_Ex3(fileName):
    c=open(fileName, encoding='UTF-8')
    l=set()
    c.readline()
    lista=c.readlines()
    for i in lista:
        s=i.strip().split(',')
        for j in lista:
            b=j.strip().split(',')
            if s[0] != b[0]:
                if int(s[1])>=29 and int (b[1])>=29:
                    if s[2] ==b[2]:
                        l.add(b[2])
    c.close()
    return(l)
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun
    
    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex3, ["esami1.csv"], {'Fisica'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami2.csv"], set())
    counter_test_positivi += tester_fun(A_Ex3, ["esami3.csv"], {'Ricerca Operativa','Analisi'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami4.csv"], {'Basi di Dati'})
    counter_test_positivi += tester_fun(A_Ex3, ["esami5.csv"], set())

    print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
