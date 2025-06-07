def A_Ex9(fileName,squadra):
    file=open(fileName,encoding='UTF-8')
    lista=[]
    for elem in file:
        elem=elem.strip().split(',')
        lista.append(elem)
    punti=0
    for partita in lista:
        if squadra in partita:
            if partita[0]==squadra:
                if int(partita[2])>int(partita[3]):
                    punti+=3
                elif int(partita[2])==int(partita[3]):
                    punti+=1
            elif partita[1]==squadra:
                if int(partita[3])>int(partita[2]):
                    punti+=3
                elif int(partita[3])==int(partita[2]):
                    punti+=1
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
