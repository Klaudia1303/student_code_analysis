def A_Ex3(fileName):
    c=set()
    s=open(fileName, encoding='UTF-8').readlines()
    for riga in s[1:]:
        l=[]
        r=riga.strip().split(',')
        for elem in s[1:]:
            f=elem.strip().split(',')
            if f[2]==r[2]:
                l.append(f[1])
        p=0
        for v in l:
            if int(v)>=29:
                p+=1
                if p>=2:
                    c.add(r[2])
    return c
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
