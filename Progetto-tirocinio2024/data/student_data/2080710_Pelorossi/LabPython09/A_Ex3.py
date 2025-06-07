def A_Ex3(fileName):
    l=[]
    l1=[]
    l2=[]
    f=open(fileName,encoding="UTF-8")
    for riga in f:
        l.append(riga)
    for i in range(1,len(l)):
        x=l[i].strip().split(',')
        if int(x[1])>=29:
            l1.append(x[2])
            for j in range(len(l1)):
                if l1.count(l1[j])>=2:
                    l2.append(l1[j])
    return set(l2)
            
            
        







    
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
