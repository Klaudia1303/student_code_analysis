def A_Ex6(filename):
    file=open(filename,'r',encoding='UTF-8')
    lista1=file.readline().strip().split(',')
    l=[0 for i in range(len(lista1))]
    for riga in file:
        r=riga.strip().split(',')
        for i in range(len(r)):
            if r[i].isdecimal():
                l[i]+=int(r[i])
    l.reverse()
    lista1.reverse()
    file.close()
    return int(lista1[l.index(max(l))])

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
