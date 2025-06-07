def A_Ex9(fileName,squadra):
    a=open(fileName, encoding="UTF-8")
    a.readline()
    pti=0
    for i in a:
        x=i.strip().split(',')
        if x[0]==squadra:
            if int(x[2])>int(x[3]):
                pti+=3
            elif int(x[2])==int(x[3]):
                pti+=1
        if x[1]==squadra:
            if int(x[2])<int(x[3]):
                pti+=3
            elif int(x[2])==int(x[3]):
                pti+=1
    return pti

        
        
                    
                
        
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
