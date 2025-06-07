def A_Ex3(fileName):
    f=open(fileName, encoding="UTF-8")
    f.readline()
    s=f.read()
    l=s.strip().split('\n')
    res=set()
    for riga in l:
        ll=riga.strip().split(',')
        if int(ll[1])>28:
            for x in l:
                xx=x.strip().split(',')
                if ll[2]==xx[2] and ll[0]!=xx[0]and int(xx[1])>28:
                    res.add(ll[2])
        
    return res
        
            
           
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
