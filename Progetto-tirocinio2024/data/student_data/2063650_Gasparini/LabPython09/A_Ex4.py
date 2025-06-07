def A_Ex4(filename,anno):
    with open(filename,encoding="UTF-8") as f:
        fields = [line.rstrip("\n").split(",") for line in f]
        years = [int(year) for year in fields[0][1:]]
        col = years.index(anno) + 1
        max_obj = ""
        max_count = 0
        for obj in fields[1:]:
            count = int(obj[col])
            if count > max_count or (count == max_count and obj[0] > max_obj):
                max_obj = obj[0]
                max_count = count
        return max_obj
     
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
