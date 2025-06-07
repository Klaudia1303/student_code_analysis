def A_Ex6(filename):
    f=open(filename, encoding='UTF-8')
    pRiga=f.readline()
    anno=pRiga.strip().split(',')
    riga=f.readlines()
    lr=[]
    for i in riga:
        lr.append(i.strip().split(','))
    massimo=0
    for x in range(1, len(anno)):
        somma=0
        for j in lr:
            somma=somma+int(j[x])
        if somma>=massimo:
            massimo=somma
            anno1=int(anno[x])
    f.close()
    return anno1    



    
   # """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
