def A_Ex9(fileName,squadra):
    f=open(fileName,'r',encoding='UTF-8')
    f.readline() #salta la prima riga perchè non ci sono dati, solo riga di testa
    punti=0
    for line in f:
        l=line.strip().split(',')
        if l[0]==squadra:
            if int(l[2])>int(l[3]):
                punti+=3
            elif int(l[2])==int(l[3]):
                punti+=1
        elif l[1]==squadra:
            if int(l[3])>int(l[2]):
                punti+=3
            elif int(l[2])==int(l[3]):
                punti+=1
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
