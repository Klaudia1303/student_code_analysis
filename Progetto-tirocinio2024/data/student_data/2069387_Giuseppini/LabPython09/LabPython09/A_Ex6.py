def A_Ex6(filename):
    f=open(filename, encoding='utf-8')
    s1=f.readline()
    anni=s1.strip().split(',')
    s=f.read()
    l=s.strip().split('\n')
    somma=0
    c=0
    for i in range(1,len(anni)-1):
        for riga in l:
            ll=riga.strip().split(',')
            somma=somma+int(ll[i])
            if somma>c:
                c=somma
                a=int(anni[i])
            somma=0
    return a
            
            

        
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
