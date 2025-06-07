def A_Ex9(fileName,squadra):
    f = open(fileName, encoding = "UTF-8")
    l = []
    punti = 0
    for i in f:
        i = i.strip().split(",")
        l.append(i)
    for i in range(1, len(l)):
        if squadra in l[i]:
            if l[i][0] == squadra:
                if l[i][2] > l[i][3]:
                    punti += 3
                elif l[i][2] == l[i][3]:
                    punti += 1
            if l[i][1] == squadra:
                if l[i][2] < l[i][3]:
                    punti += 3
                elif l[i][2] == l[i][3]:
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
