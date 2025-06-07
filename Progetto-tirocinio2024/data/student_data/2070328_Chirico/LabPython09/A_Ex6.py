def A_Ex6(filename):
    x = open(filename,'r',encoding= 'UTF-8')
    m = x.readline().strip().split(',')
    a = []
    c = 0
    n = 0
    
    for i in x:
        y = i.strip().split(',')
        y.remove(y[0])
        a.append(y)

        
    for j in range(len(a[0])):
        b = 0
        for z in a:
            b = int(z[c]) +b

        if b >= n:
            n = b
            N = c+1
            
        c = c+1



    x.close()
    return  int(m[N])
        





    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
