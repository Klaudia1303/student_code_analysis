def A_Ex4(filename,anno):
    f=open(filename,encoding="utf-8")
    sol=[]
    ris=[]
    fin=[]
    for elem in f:
        elem=elem.strip().split(",")
        sol.append(elem)
    for i in range(1,len(sol)):
        for e in range(1,len(sol[0])):
            if int(sol[0][e])==anno:
                ris.append(sol[i][e])
                x=max(ris)
    for i in range(1,len(sol)):
        for e in range(1,len(sol[0])):
            if int(sol[0][e])==anno:
                if sol[i][e]==x:
                    fin.append(sol[i][0])
    for y in fin:
        return y


                        











    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
     
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
