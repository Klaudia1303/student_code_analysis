def A_Ex3(fileName):
    file=open(fileName,encoding='UTF-8')
    sv=[]
    insieme=set()
    for riga in file:
        riga=riga.strip().split(',')
        sv.append(riga)
    conta=0
    materia=[]
    for i in range(1,len(sv)):
        dati=sv[i]
        if int(dati[1])>=29:
            conta+=1
            materia.append(dati[2])
    if conta>=2:
        for n in range(len(materia)):
            if int(materia.count(materia[n]))>=2:
                insieme.add(materia[n])
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
