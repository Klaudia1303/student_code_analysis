def A_Ex3(fileName):
    f=open(fileName,encoding='UTF-8')
    f.readline()
    l=[]
    lr=[]
    for i in f:
        l.append(i.strip().split(','))
    for i in range(len(l)):
        if int(l[i][1])>28:
            for j in range(i+1,len(l)):
                if l[i][2] in l[j] and int(l[j][1]) >28:
                    lr.append(l[j][2])
    return set(lr)
            

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
