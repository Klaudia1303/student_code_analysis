def A_Ex3(fileName):
    f=open(fileName,encoding="UTF-8")
    f.readline()
    
    lista_completa=[]
    lista_29=[]
    res=[]
    
    for elem in f:
        elem=elem.strip().split(',')
        lista_completa.append(elem)
    f.close()

    for i in lista_completa:
        if int(i[1])>=29:
            lista_29.append(i[2])
            
    for i in lista_29:
        if lista_29.count(i)>=2:
            res.append(i)
        
    res=set(res)

    return(res)

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
