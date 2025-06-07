def A_Ex3(fileName):
    f=open(fileName,'r',encoding='UTF-8')
    nomi=f.readline()
    listamaterie=[]
    for riga in f:
        riga=riga.strip().split(',')
        if int(riga[1])>28:
            listamaterie.append(riga[2])
    lista=[]
    for elem in listamaterie:
       if listamaterie.count(elem)>=2:
           lista.append(elem)
    a=set(lista)  
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
