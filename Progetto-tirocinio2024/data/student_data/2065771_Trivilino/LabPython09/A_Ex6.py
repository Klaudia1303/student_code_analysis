def A_Ex6(filename):
        f=open(filename, encoding='UTF-8')
        anni=f.readline().strip().split(",")
        (_, anni) = (anni[0], anni[1:])

        venditemax= 0
        anno= 0

        dati = f.readlines()

        for i in range(len(anni)):
            venditeanno = 0

            for vendite in dati:
                vendite = vendite.strip().split(',')
                venditeanno += int(vendite[i + 1])

            if venditeanno > venditemax:
                venditemax = venditeanno
                anno = int(anni[i])
            elif venditeanno == venditemax:
                anno = max(anno, int(anni[i]))

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
