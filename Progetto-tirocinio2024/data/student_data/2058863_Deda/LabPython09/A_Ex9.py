def A_Ex9(fileName,squadra):
    f=open(fileName,'r',encoding="UTF-8")
    s=f.readlines()
    x=s[0].strip().split(',')
    a=0
    for i in range(1,len(s)):
        y=s[i].strip().split(',')
        for j in range(len(y)):
            d=y[j]
            if d==squadra and j%2==0:
                v=int(y[2])
                p=int(y[3])
                if v>p:
                    a+=3
                elif v==p:
                    a+=1
                elif v<p:
                    a+=0
            if d==squadra and j%2!=0:
                p=int(y[2])
                v=int(y[3])
                if v>p:
                    a+=3
                elif v==p:
                    a+=1
                elif v<p:
                    a+=0
    f.close()
    return a



    
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
