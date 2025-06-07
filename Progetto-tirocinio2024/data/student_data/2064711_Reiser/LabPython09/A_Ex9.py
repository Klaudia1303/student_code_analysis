def A_Ex9(fileName,squadra):
    f=open(fileName,encoding='UTF-8')
    f.readline()
    s=f.read().strip().split()
    punti=0
    for i in s:
        j=i.split(',')
        if squadra in j:
            pos=j.index(squadra)
            gg=j[(j.index(squadra)+2)]
            if pos==0:
                if gg>(j[j.index(squadra)+3]):
                    punti+=3
                elif gg<(j[j.index(squadra)+3]):
                    punti+=0
                elif gg==(j[j.index(squadra)+3]):
                    punti+=1
            elif pos==1:
                if gg>(j[j.index(squadra)+1]):
                    punti+=3
                if gg<(j[j.index(squadra)+1]):
                    punti+=0
                if gg==(j[j.index(squadra)+1]):
                    punti+=1
    return punti
    f.close()
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
