def A_Ex6(filename):
    f = open(filename, "r")
    righe = []
    anno = 0

    for x in f:
        righe.append((x.strip().split(",")))

    f.close()

    somma = 0
    somma_maggiore = 0

    print(righe)

    for a in range(1,len(righe[0])):
        for b in range(1, len(righe)):
            print(b, len(righe[0]))
            print(righe[b][a])
            somma = somma + int(righe[b][a])
        if somma > somma_maggiore:
            somma_maggiore = somma
            anno = righe[0][a]
        somma = 0

    return int(anno)
    

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
