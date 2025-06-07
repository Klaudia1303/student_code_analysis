def A_Ex4(filename,anno):
    f = open(filename, encoding="UTF-8")
    lines = f.readlines()
    f.close()

    vendite_oggetto=[]
    oggetti = []
    l = []

    for line in lines:
        l.append(line.strip().split(","))

    for i in range(len(l)):
        for j in range(len(l[i])):
            if anno==l[i][j]:
                for i in range(1, len(l)):
                    vendite_oggetto.append(l[i][j])
    print(vendite_oggetto)            
    for i in range(1,len(l)):
        oggetti.append(l[i][0])
                    
    vendite_int=[]
    for k in vendite_oggetto:
        vendite_int.append(int(k))
    print(vendite_int)

    max_vendite = max(vendite_int)
    pos = vendite_int.index(max_vendite)

    return oggetti[pos]
        
        
            
    
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
