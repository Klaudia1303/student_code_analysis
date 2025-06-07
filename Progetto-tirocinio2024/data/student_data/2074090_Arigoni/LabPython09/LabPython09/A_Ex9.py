def A_Ex9(fileName,squadra):
    f=open(fileName,encoding="utf-8")
    s=f.read()
    sol=s.split()
    z=0
    for i in range(1,len(sol)):
        k=sol[i].split(",")
        for e in range(2):
            if(k!=[""] and k[e]==squadra):
                if (int(k[e+2])>int(k[3-e])):
                    z=z+3
                elif (int(k[e+2])==int(k[3-e])):
                    z=z+1
    return z
    































    
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
