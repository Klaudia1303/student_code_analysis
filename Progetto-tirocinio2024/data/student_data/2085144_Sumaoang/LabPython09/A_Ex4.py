def A_Ex4(filename,anno):
    file = open(filename, encoding="UTF-8")
    headings = file.readline().strip().split(",")
    year_column = get_index(headings, str(anno))
    if year_column == len(headings):
        return

    item = '' 
    occurrencies = -1
    for line in file:
        record = line.strip().split(",")
        if (int(record[year_column]) > occurrencies) or ((int(record[year_column]) == occurrencies) and record[0].lower() > item.lower()):
            item = record[0]
            occurrencies = int(record[year_column])
    
    return item

def get_index(l: list, item) -> int:
    index = 0
    while index < len(l) and l[index] != item:
        index += 1
    return index

###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

