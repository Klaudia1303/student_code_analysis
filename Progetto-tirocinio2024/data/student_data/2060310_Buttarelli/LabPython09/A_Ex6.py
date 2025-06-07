def A_Ex6(filename):
    f = open(filename, encoding = "UTF-8")
    l = []
    somma = 0
    massimo = 0
    annoMassimo = 0
    for i in f:
        i = i.strip().split(",")
        l.append(i)
    for i in range(1, len(l[0])):
        for j in range(1, len(l)):
            for m in range(1, len(l[j])):
                if l[0].index(l[0][i]) == l[j].index(l[j][m]):
                    somma += int(l[j][m])
            if somma > massimo:
                massimo = somma
                annoMassimo = int(l[0][i])
            somma = 0
    f.close()
    return annoMassimo
 
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
