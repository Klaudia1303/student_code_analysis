def A_Ex6(filename):
    f=open(filename,encoding='UTF-8')
    s=f.readline()
    a=s.strip().split(',')
    l=[]
    for c in range(1,len(a)):
        l.append(a[c])
    k=[0 for c in range(len(a))]
    for i in f:
        a=i.strip().split(',')
        for j in range(1,len(a)):
            k[j-1]+=int(a[j])
    f.close()
    ris=int(l[k.index(max(k))])
    return ris
    



    
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
