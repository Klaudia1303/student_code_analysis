def A_Ex3(fileName):
    a=open(fileName, encoding="UTF-8")
    z=set()
    sv=[]
    for elem in a:
        elem=elem.strip().split(",")
        sv.append(elem)
        for i in range (1,len(sv)):
            if int(sv[i][1])>=29:
                for j in range(i+1,len(sv)):
                    if int(sv[j][1])>=29 and sv[j][2]==sv[i][2] and int(sv[j][0])!=int(sv[i][0]):
                        z.add(sv[i][2])
    return z
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
