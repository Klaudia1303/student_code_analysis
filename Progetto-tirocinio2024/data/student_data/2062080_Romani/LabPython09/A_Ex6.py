def A_Ex6(filename):
    with open(filename, 'r', encoding='UTF-8') as f:
        headers = f.readline().strip().split(',')
        (_, years) = (headers[0], headers[1:])
        max_sales = 0
        max_year = 0
        lines = f.readlines()
        for i in range(len(years)):
            current_sales = 0
            for line in lines:
                line = line.strip().split(',')
                current_sales += int(line[i + 1])
            if current_sales > max_sales:
                max_sales = current_sales
                max_year = int(years[i])
            elif current_sales == max_sales:
                max_year = max(max_year, int(years[i]))
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
