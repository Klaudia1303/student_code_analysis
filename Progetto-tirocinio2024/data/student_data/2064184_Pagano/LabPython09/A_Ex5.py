def A_Ex5(filename,oggetto):
    f = open(filename, encoding="UTF-8")
    dataset = [row.strip().split(",") for row in f.readlines()]
    years = dataset.pop(0)

    for data in dataset:
        if data[0] == oggetto:
            i = 2
            maxYear = int(years[1])
            maxCres = 0
            while i < len(data):
                cres = int(data[i]) - int(data[i-1])
                if cres > maxCres or (cres == maxCres and int(years[i]) > maxYear):
                    maxCres = cres
                    maxYear = int(years[i])
                i += 1

    return maxYear

###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
