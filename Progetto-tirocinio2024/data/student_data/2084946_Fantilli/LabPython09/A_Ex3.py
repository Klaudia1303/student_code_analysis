def A_Ex3(fileName):
    f=open(fileName,encoding="UTF-8")
    intestazione=f.readline()
    riga=f.readline().strip().split(',')
    l=[]
    a=set()
    while len(riga)>1:
        if int(riga[1])>=18:
            l.append(riga[2])
        riga=f.readline().strip().split(',')
    for i in l:
        if l.count(i)>1:
            a.add(i)
    f.close()
    return a
    

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
