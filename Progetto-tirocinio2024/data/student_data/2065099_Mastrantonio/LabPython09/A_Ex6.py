def A_Ex6(filename):
    f=open(filename, encoding="UTF-8")
    l=[]
    for elem in f:
        elem=elem.strip().split(",")
        l.append(elem)
    f.close()
    massimo = 0
    for i in range (1,len(l[1])):
        somma = 0
        for j in range(1,len(l)):
            elem = l[j]
            somma = somma + int(elem[i])
        if somma >= massimo :
            massimo = somma
            anno = (l[0])[i]
    anno = int(anno)
    return(anno)
 
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
