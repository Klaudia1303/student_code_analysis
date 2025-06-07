def A_Ex3(fileName):
    fin=open(fileName,encoding="UTF-8")
    insieme=set()
    f=fin.readlines()
    for i in range(1,len(f)):
        conta=0
        r=f[i].strip().split(",")
        rs=tuple(r)
        if int(rs[1])>=29:
            conta+=1
            materia=rs[2]
            for j in range(1,len(f)):
                if materia in f[j]:
                    r1=f[j].strip().split(",")
                    rs1=tuple(r1)
                    if int(rs[1])>=29:
                        conta+=1
        if conta-1>=2:
             insieme.add(materia)
    fin.close()
    return insieme
             
                      
            
        
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
