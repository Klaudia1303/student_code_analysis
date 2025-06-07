def A_Ex6(filename):
    f=open(filename,encoding='UTF-8')
    r0=f.readline().strip().split(',')
    d={}
    f.close()
    for e in r0[1:]:
        f=open(filename,encoding='UTF-8')
        d[e]=0
        a=r0.index(e)
        for riga in f:
            riga=riga.strip().split(',')
            d[e]+=int(riga[a])
        f.close()
    c=0
    print(d)
    for key in d:
        if int(d[key])>c:
            c=int(d[key])
    for key in d:
        if c==d[key]:
            return int(key)
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
