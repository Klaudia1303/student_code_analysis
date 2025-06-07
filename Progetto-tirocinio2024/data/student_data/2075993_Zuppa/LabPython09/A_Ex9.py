def A_Ex9(fileName,squadra):
    fin=open(fileName,encoding='UTF-8')
    fin.readline()
    p=0
    r=fin.readline()
    lr=r.strip().split(',')
    while len(r)>0:
        if squadra in lr:
            if lr[2]==lr[3]:
                p+=1
            if squadra==lr[0] and lr[2]>lr[3]:
                p+=3
            elif squadra==lr[1] and lr[3]>lr[2]:
                p+=3
        r=fin.readline()
        lr=r.strip().split(',')
    fin.close()
    return p
                
 
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
