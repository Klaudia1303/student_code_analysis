def A_Ex3(fileName):
    f=open(fileName,'r',encoding='UTF-8')
    riga=f.readline()
    info=riga.strip().split(',')
    insieme=set()
    l=[]
    l1=[]
    mat=0
    for righe in f:
        dati=righe.strip().split(',')
        l.append(dati)
    for i in range(len(l)):
        if int(l[i][1])>=29:
            l1.append(l[i][2])
            if l1.count(l[i][2])>=2:
                insieme.add(l[i][2])
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
