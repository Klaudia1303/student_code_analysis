def A_Ex6(filename):
    fin=open(filename,encoding='UTF-8')
    s=fin.readline()
    s=s.strip().split(',')
    s.remove(s[0])
    b=[]
    ris=0
    somma=0
    for riga in fin:
        riga=riga.strip().split(',')
        riga.remove(riga[0])
        b.append(riga)
    for i in range(len(s)):
        for k in b:
            for costo in range(len(k)):
                if costo==i:
                    somma=somma+int(k[costo])
        if somma>=ris:
            ris=somma
            annoDef=i
        somma=0
    return int(s[annoDef])
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
