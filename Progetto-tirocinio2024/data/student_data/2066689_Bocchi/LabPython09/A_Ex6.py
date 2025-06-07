def A_Ex6(filename):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    x=0
    ris=1
    somma_prec=0
    sv=[]
    f= open(filename,encoding='UTF-8')
    for el in f:
        el=el.strip().split(',')
        sv.append(el)
    for b in range(1,len(sv[0])):
        somma=0
        for x in range(1,len(sv)):
            somma= somma + int(sv[x][b])
        if somma >= somma_prec:
            somma_prec= somma
            ris=sv[0][b]
    anno= int(ris)
    f.close()
    return anno
 
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
