def A_Ex9(fileName,squadra):
    fopen=open(fileName, encoding='UTF-8')
    s=fopen.readline()
    s=''
    s=fopen.readlines()
    punti=0
    for i in s:
        t=i.strip().split(',')
        if squadra in t:
            num=t.index(squadra)
            if num==0:
                latoa=3
                latos=2
            elif num==1:
                latoa=2
                latos=3
            if int(t[latos])>int(t[latoa]):
                punti+=3
            elif int(t[latos])==int(t[latoa]):
                punti+=1
    fopen.close()
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
