def A_Ex6(filename):
    f=open(filename,encoding='UTF-8')
    s=f.readline()
    s=s.strip().split(',')
    f.close()
    somma=0
    totale=0
    pos=0
    n=0
    i=1
    while i<len(s):
        f=open(filename,encoding='UTF-8')
        s=f.readline()
        s=s.strip().split(',')
        for riga in f:
            riga=riga.strip().split(',')
            n=int(riga[i])
            somma+=n
        if somma>=totale:
            totale=somma
            pos=i
        somma=0
        f.close()
        i+=1
    f=open(filename,encoding='UTF-8')
    s=f.readline()
    s=s.strip().split(',')
    f.close()
    k=int(s[pos])
    return k
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
