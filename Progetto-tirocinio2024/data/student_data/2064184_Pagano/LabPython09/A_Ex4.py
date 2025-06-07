def A_Ex4(filename,anno):
    f = open(filename, encoding="UTF-8")
    dataset = [row.strip().split(",") for row in f.readlines()]
    years = dataset.pop(0)

    i = years.index(str(anno))
    maxOgg = ""
    maxVend = 0
    for data in dataset:
        if data[i] > str(maxVend):
            maxOgg = data[0]
            maxVend = data[i]
        elif data[i] == str(maxVend):
            if data[0] > maxOgg:
                maxOgg = data[0]
                maxVend = data[i]
    
    return maxOgg
     
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
