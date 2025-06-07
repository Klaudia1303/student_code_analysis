def A_Ex3(fileName):
    fin=open(fileName,encoding="UTF-8")
    f=fin.readlines()
    fin.close()
    insieme=set()
    for i in range(1,len(f)):
        conta=0
        ri=f[i].strip().split(",")
        if int(ri[1])>=29:
            conta+=1
            materia=ri[2]
            for j in range (1,len(f)):
                if materia in f[j]:
                    ri2=f[j].strip().split(",")
                    if int(ri2[1])>=29:
                        conta+=1
        if conta-1>=2:
            insieme.add(materia)
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
