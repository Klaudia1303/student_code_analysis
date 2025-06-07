def A_Ex9(fileName,squadra):
    f=open(fileName,encoding="UTF-8")
    d={}
    d[squadra]=0
    butta=f.readline()
    for riga in f:
        riga=riga.strip().split(",")
        if riga[0]==squadra:
            if riga[2]>riga[3]:
                d[squadra]+=3
            elif riga[2]==riga[3]:
                d[squadra]+=1
        elif riga[1]==squadra:
            if riga[2]<riga[3]:
                d[squadra]+=3
            elif riga[2]==riga[3]:
                d[squadra]+=1
    return d.get(squadra)
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
