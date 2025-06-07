def A_Ex5(filename,oggetto):
    f=open(filename,encoding="utf-8")
    sol=[]
    ris=[]
    fin=[]
    for elem in f:
        elem=elem.strip().split(",")
        sol.append(elem)
    for i in range(1,len(sol)):
        for e in range(1,len(sol[0])):
            if sol[i][0]==oggetto:
                ris.append(sol[i][e])
                x=max(ris)
    for i in range(1,len(sol)):
        for e in range(1,len(sol[0])):
            if sol[i][0]==oggetto:
                if sol[i][e]==x:
                    fin.append(sol[0][e])
    for y in fin:
        return int(y)
                
    
            
            
    














    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
