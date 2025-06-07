def A_Ex9(fileName,squadra):
    f = open(fileName, encoding="UTF-8")
    s = f.read().split("\n")
    f.close()
    k = 0
    for i in range(1, len(s)):
        j = s[i].split(",")
        for l in range(2):
            if j != [""] and j[l] == squadra:
                if int(j[l+2])> int(j[3-l]):
                    k +=3
                elif int(j[l +2]) == int(j[3-l]):
                    k += 1
    return k

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
