def A_Ex5(filename,oggetto):
    f = open(filename,encoding='UTF-8')
    head = f.readline().strip().split(',')
    
    for l in f.readlines():
        data = l.strip().split(',')
        if data[0] != oggetto:
            continue
        
        cresc, cresc_ind = 0, 1
        for v in range(2, len(data)):
            diff = int(data[v])-int(data[v-1])
            if diff >= cresc:
                cresc, cresc_ind = diff, v
        
    f.close()        
    return int(head[cresc_ind])
    

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
