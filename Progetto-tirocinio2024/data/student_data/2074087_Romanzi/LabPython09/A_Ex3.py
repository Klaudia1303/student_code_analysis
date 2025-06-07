def A_Ex3(fileName):
    
    f=open(fileName,encoding="UTF-8")
    ls=set()
    lt=[]
    for i in f:
        i=i.strip().split(",")
        lt.append(i)
    for j in range(1,len(lt)):
        if int(lt[j][1])>=29:
            for z in range(j,len(lt)):
                if lt[j][2]==lt[z][2] and int(lt[z][1])>=29 and j!=z:
                    ls.add(lt[j][2])
    f.close()
    return ls

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
