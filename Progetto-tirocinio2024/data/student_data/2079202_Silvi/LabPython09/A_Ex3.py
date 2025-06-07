def A_Ex3(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(fileName, encoding="UTF-8")
    d={}
    for elem in f:
        if elem.split(",")[1].isdecimal():
            if int(elem.split(",")[1])>=29:
                if elem.split(",")[2].strip() in d:
                    d[elem.split(",")[2].strip()]+=1
                else:
                    d[elem.split(",")[2].strip()]=1
    for elem in list(d.keys()):
        if d[elem]<2:
            del d[elem]
    return set(d.keys())
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
