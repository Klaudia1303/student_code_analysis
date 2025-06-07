def A_Ex6(filename):
    with open(filename,encoding="UTF-8") as f:
        fields = [line.rstrip("\n").split(",") for line in f]
        years = [int(year) for year in fields[0][1:]]
        max_count = 0
        max_year = 0
        for i in range(len(years)):
            count = 0
            year = years[i]
            for obj in fields[1:]:
                count += int(obj[i + 1])
            if count > max_count or (count == max_count and year > max_year):
                max_count = count
                max_year = year
        return max_year
 
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
