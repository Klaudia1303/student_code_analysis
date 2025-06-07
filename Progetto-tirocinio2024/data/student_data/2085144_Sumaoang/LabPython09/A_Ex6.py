def A_Ex6(filename):
    f = open(filename,encoding="UTF-8")

    f1 = f.readline()
    f2 = f1.strip()
    f3 = f2.split(",")
    if len(f3) <= 1:
        return

    anno = [0] * len(f3)

    for x in f:
        i1 = x.strip()
        i2 = i1.split(",")
        for y in range(1, len(i2)):
            vendita = int(i2[y])
            anno[y] += vendita

    vendita_massima = 1
    for y in range(1, len(anno)):
        if (anno[y] > anno[vendita_massima]) or ((anno[y] == anno[vendita_massima])) and (int(f3[y]) > int(f3[vendita_massima])):
            vendita_massima = y
            
    return int(f3[vendita_massima])
            
    

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
