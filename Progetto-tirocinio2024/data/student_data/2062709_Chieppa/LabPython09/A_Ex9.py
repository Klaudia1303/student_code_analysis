def A_Ex9(fileName,squadra):
    f=open(fileName)
    sv=[]
    l=[]
    m=[]
    for elem in f:
        elem=elem.strip().split(',')
        sv.append(elem)

        
    for i in range(1,len(sv)):
        if int(sv[i][2])>int(sv[i][3]):
            l.append(sv[i][0])
        elif int(sv[i][2])<int(sv[i][3]):
             l.append(sv[i][1])
        elif int(sv[i][2])==int(sv[i][3]):
            m.append(sv[i][0])
            m.append(sv[i][1])


    punti=l.count(squadra)*3+m.count(squadra)
    f.close()
    return punti







    
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
