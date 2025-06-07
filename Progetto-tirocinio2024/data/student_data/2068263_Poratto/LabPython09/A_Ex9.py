def A_Ex9(fileName,squadra):
    f=open(fileName)
    d={}
    key=[]
    for riga in f:
        riga=riga.strip().split(',')
        for i in range(2):
            if riga[i] not in key:
                d[riga[i]]=0
                key.append(riga[i])
    f.close
    f=open(fileName)
    for riga in f:
        riga=riga.strip().split(',')
        if riga[2]>riga[3]:
            d[riga[0]]+=3
        if riga[2]==riga[3]:
            d[riga[0]]+=1
            d[riga[1]]+=1
        if riga[2]<riga[3]:
            d[riga[1]]+=3
    f.close()
    if squadra in key:
        return d[squadra]
    else: return 0

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
