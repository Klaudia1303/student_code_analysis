def A_Ex9(fileName,squadra):
    file=open(fileName,'r',encoding='UTF-8')
    primariga=file.readline()
    punti=0
    for riga in file:
        riga=riga.strip().split(',')
        primasquadra=riga[0]
        secondasquadra=riga[1]
        goal1=int(riga[2])
        goal2=int(riga[3])
        if primasquadra==squadra:
            if goal1>goal2:
                punti+=3
            elif goal1==goal2:
                punti+=1
            elif goal1<goal2:
                punti+=0
        if secondasquadra==squadra:
            if goal1<goal2:
                punti+=3
            elif goal1==goal2:
                punti+=1
            elif goal1>goal2:
                punti+=0
    file.close()
    return punti
        
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
