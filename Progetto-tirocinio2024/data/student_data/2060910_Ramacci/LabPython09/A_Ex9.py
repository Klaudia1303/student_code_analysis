def A_Ex9(fileName,squadra):
    s=open(fileName,encoding='UTF-8').readlines()
    r=0
    for elem in s:
        p=elem.strip().split(',')
        if p[0]==squadra:
            if int(p[2])-int(p[3])>0:
                r+=3
            elif int(p[2])-int(p[3])==0:
                r+=1
        elif p[1]==squadra:
            if int(p[3])-int(p[2])>0:
                r+=3
            elif int(p[3])-int(p[2])==0:
                r+=1
    return r
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
 
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
