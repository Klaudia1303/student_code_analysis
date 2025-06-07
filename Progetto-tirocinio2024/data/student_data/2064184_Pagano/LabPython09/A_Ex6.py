def A_Ex6(filename):
    f = open(filename, encoding="UTF-8")
    dataset = [row.strip().split(",") for row in f.readlines()]
    years = dataset.pop(0)

    maxVend = 0
    maxYear = 0
    i = 1
    while i < len(years):
        year = int(years[i])
        n = 0
        for data in dataset:
            n += int(data[i])
        if n > maxVend or (n == maxVend and year > maxYear):
            maxVend = n
            maxYear = year
        i += 1

    return maxYear
 
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
