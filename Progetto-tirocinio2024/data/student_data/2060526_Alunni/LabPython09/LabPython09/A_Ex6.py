def A_Ex6(filename):
    c=open(filename,encoding='UTF-8')
    s=c.readline()
    p=s.strip().split(',')
    a=[]
    for i in range(1,len(p)):
        a.append(p[i])
    k=[0 for i in range(len(p))]
    for j in c:
        p= j.strip().split(',')
        for l in range(1,len(p)):
            k[l-1]+= int(p[l])
    c.close()
    return int(a[k.index(max(k))])


    
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
