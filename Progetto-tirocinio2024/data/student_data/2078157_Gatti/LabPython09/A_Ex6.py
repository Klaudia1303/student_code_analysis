def A_Ex6(filename):
    f = open(filename,encoding="UTF-8")
    s = f.readline()
    x = s.strip().split(',')
    anni = []
    for i in range(1,len(x)):
        anni.append(x[i])
    vendite = [0 for i in range(len(x))]
    for i in f:
        x = i.strip().split(',')
        for j in range(1,len(x)):
            vendite[j-1] += int(x[j])
    f.close()
    return int(anni[vendite.index(max(vendite))])
        
            
                
            
 
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
