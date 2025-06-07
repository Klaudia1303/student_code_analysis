def A_Ex3(fileName):
    l=[]
    l1=[]
    i=set()
    f=open(fileName,encoding="UTF-8")
    riga=f.readline()
    for riga in f:   
        dati= riga.strip().split(",")
        t=tuple(dati)
        l.append(t)
    for elem in l:
        voto = elem[1]
        voto=int(voto)
        if voto>28:
            l1.append(elem[2])
            for elem in l1:
                if l1.count(elem)>1:
                    i.add(elem)
    return i
        
            
            
            
        
        
    
    
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
