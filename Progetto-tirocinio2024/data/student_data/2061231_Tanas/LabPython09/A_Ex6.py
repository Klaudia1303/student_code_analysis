def A_Ex6(filename):
    f = open(filename,encoding='UTF-8')
    
    head = f.readline().strip().split(',')
    vendite_tot = [0 for _ in range(len(head)-1)]
    
    for l in f.readlines():
        data = l.strip().split(',')
        for v in range(1, len(data)):
            vendite_tot[v-1] += int(data[v])
            
    max_v, year = 0, int(head[1])
    for i in range(len(vendite_tot)):
        if vendite_tot[i] > max_v or \
            (vendite_tot[i] == max_v and year < int(head[i+1])):
            max_v, year = vendite_tot[i], int(head[i+1])
            
    f.close()
    return year
 
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
