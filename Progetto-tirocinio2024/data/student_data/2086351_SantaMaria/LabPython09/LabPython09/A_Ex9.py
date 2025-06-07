def A_Ex9(fileName,squadra):
    fin=open(fileName,encoding='UTF-8')
    p=[]
    punti=0
    for i in fin:
        i=i.strip().split(',')
        p.append(i)
    p.remove(p[0])
    for m in p:
        if squadra in m:
            if squadra==m[0]:
                if m[2]>m[3]:
                    punti+=3
                elif m[2]==m[3]:
                    punti+=1
            elif squadra==m[1]:
                if m[3]>m[2]:
                    punti+=3
                elif m[2]==m[3]:
                    punti+=1
    return punti
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
