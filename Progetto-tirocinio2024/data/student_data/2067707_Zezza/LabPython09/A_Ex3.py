def A_Ex3(fileName):
    l=[]
    L=[]
    f=open(fileName,encoding='UTF-8')
    for riga in f:
        riga=riga.strip().split(',')
        if riga[1].isalpha()==True:
            continue
        else:
            if int(riga[1])>=29:
                if riga[2] not in l:
                    l.append(riga[2])
                else:
                    L.append(riga[2])
    I=set(L)
    f.close()
    return I
            

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
