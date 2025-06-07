def A_Ex9(fileName,squadra):
    f=open(fileName, mode="r", encoding="UTF-8")
    s=squadra
    l=[]
    for e in f:
        e = e.strip().split(",")
        l.append(e)
        p=0
    for i in range(1,len(l)):
        if s in l[i]:
            if l[i].index(s)==0:
                if int(l[i][2])>int(l[i][3]):
                    p=p+3
                elif int(l[i][2])==int(l[i][3]):
                    p=p+1
                else:
                    continue
            else:
                if int(l[i][2])<int(l[i][3]):
                    p=p+3
                elif int(l[i][2])==int(l[i][3]):
                    p=p+1
                else:
                    continue
    f.close()

    return p
    
        
        
        
        
        



















    
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
