#Jacopo Corsani - Corso di Laurea in Ingegneria Informatica e Automatica A.A. 2022-23 - Laboratorio di Fondamenti di Programmazione - ES.9


def A_Ex9(fileName,squadra):
    f = open(fileName,encoding="UTF-8")
    f.readline()
    pti = 0
    for i in f:
        x = i.strip().split(',')
        if x[0]==squadra:
            if int(x[2])>int(x[3]):
                pti += 3
            elif int(x[2])==int(x[3]):
                pti += 1
        elif x[1]==squadra:
            if int(x[3])>int(x[2]):
                pti += 3
            elif int(x[3])==int(x[2]):
                pti += 1
    f.close()
    return pti
            


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
