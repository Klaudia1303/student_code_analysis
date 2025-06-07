def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    fin=open(filename, encoding="UTF-8")
    ranni=fin.readline().strip().split(",")
    sommavendite=[0]
    for anno in ranni[1:]:
        sommavendite.append(0)
    for r in fin:
        lr=r.strip().split(",")
        for i in range(1,len(lr)):
            sommavendite[i]=sommavendite[i]+int(lr[i])
    return int(ranni[sommavendite.index(max(sommavendite))])
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
