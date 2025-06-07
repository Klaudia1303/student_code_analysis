def A_Ex9(fileName,squadra):
    f = open(fileName,encoding='UTF-8')
    f.readline()
    
    punti = 0
    for l in f:
        if not squadra in l:
            continue
        data = l.strip().split(',')
        if (data[0] == squadra and int(data[2]) > int(data[3])) or \
            (data[1] == squadra and int(data[3]) > int(data[2])):
            punti += 3
        elif data[2] == data[3]:
            punti += 1
            
    f.close()
    return punti
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Chelsea'] , 3)
    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Tottenham'] , 1)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Arsenal'] , 4)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Bayern'] , 0)
    counter_test_positivi += tester_fun(A_Ex9, ["partite3.csv",'Bayern'] , 4)

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
