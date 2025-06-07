def A_Ex6(filename):
    fin=open(filename, encoding="UTF-8"); d={}; massimo=anno=0
    riga1=fin.readline().strip().split(",");
    for elem in fin:
        elem=elem.strip().split(",");
        for a in range(1,len(riga1)):
            d[int(riga1[a])]=0
            for i in range(1,len(elem)):
                if a==i:    d[int(riga1[a])]+=int(elem[i]); break
            if massimo<d[int(riga1[a])]: anno=riga1[i]; massimo=d[int(riga1[a])]
            elif massimo==d[int(riga1[a])]: anno=max(anno,riga1[i])
    fin.close()
    return int(anno)
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
