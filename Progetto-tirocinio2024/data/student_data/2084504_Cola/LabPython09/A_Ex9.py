def A_Ex9(fileName,squadra):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(fileName,encoding='UTF-8')
    x=0
    for riga in f:
        s=riga.strip().split(',')
        if squadra not in s or not s[2].isdecimal():
            continue
        if s[s.index(squadra)+2]==s[2]:
            y=3
        elif s[s.index(squadra)+2]==s[3]:
            y=2
        if s[s.index(squadra)+2]>s[y]:
            x+=3
        elif s[2]==s[3]:
            x+=1
    f.close()
    return x
    
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
