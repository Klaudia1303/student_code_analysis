def A_Ex5(filename,oggetto):
    with open(filename,encoding="UTF-8") as f:
        fields = [line.rstrip("\n").split(",") for line in f]
        years = [int(year) for year in fields[0][1:]]
        obj_names = [obj[0] for obj in fields[1:]]
        obj_index = obj_names.index(oggetto)
        obj_counts = [int(count) for count in fields[obj_index + 1][1:]]
        max_i = 0
        max_growth = 0
        for i in range(1,len(obj_counts)):
            growth = obj_counts[i] - obj_counts[i - 1]
            if growth >= max_growth:
                max_growth = growth
                max_i = i
        return years[max_i]

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
