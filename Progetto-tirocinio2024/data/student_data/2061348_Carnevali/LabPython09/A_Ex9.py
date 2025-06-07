def A_Ex9(fileName,squadra):
    a=open(fileName)
    b=a.readlines()
    x=0
    for n in range(1,len(b)):
        c=b[n].strip().split(",")
        if c[0]==squadra:
            if int(c[2])>int(c[3]):
                x=x+3
            if int(c[2])==int(c[3]):
                x=x+1
        if c[1]==squadra:
            if int(c[3])>int(c[2]):
                x=x+3
            if int(c[3])==int(c[2]):
                x=x+1
    a.close()
    return x
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
