def A_Ex6(filename):
    f=open(filename,encoding='UTF-8')
    riga=f.readline()
    anno=riga.strip().split(',')
    riga=f.readline()
    dati=riga.strip().split(',')
    massimo=0
    for i in range(1,len(anno)):
        f=open(filename,encoding='UTF-8')
        riga=f.readline()
        anno=riga.strip().split(',')
        riga=f.readline()
        dati=riga.strip().split(',')
        somma=0
        for j in f:
            somma=somma+int(dati[i])
            riga=f.readline()
            dati=riga.strip().split(',')
        if somma>massimo:
            massimo=somma
            a=anno[i]
        if somma==massimo and a<anno[i]:
            massimo=somma
            a=anno[i]
        f.close()
    return int(a)
 
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
