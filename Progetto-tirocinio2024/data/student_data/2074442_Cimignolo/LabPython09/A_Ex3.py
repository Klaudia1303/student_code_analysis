def A_Ex3(fileName):
    fi=open(fileName,encoding='UTF-8')
    fin=fi.readlines()
    lista=[]
    insieme=set()
    for elem in range(1, len(fin)):
        fin[elem]=fin[elem].strip().split(',')
        if int(fin[elem][1])>=29:
            lista.append(fin[elem][2])
            for n in lista:
                if lista.count(n)>1:
                    insieme.add(n)
    fi.close()    
    return insieme

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
