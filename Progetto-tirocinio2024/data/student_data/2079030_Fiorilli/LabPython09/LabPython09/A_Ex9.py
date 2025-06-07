def A_Ex9(fileName,squadra):
    f=open(fileName, encoding="UTF-8")
    riga=f.readline()
    punt=0
    partita=f.readline()
    while len(partita)>0:
        partita=partita.strip().split(',')
        if squadra in partita:
            if ((int(partita[2])-int(partita[3]))>0 and partita[0]==squadra) or ((int(partita[2])-int(partita[3]))<0 and partita[1]==squadra):
                punt+=3
            elif (int(partita[2])-int(partita[3]))==0:
                punt+=1
        partita=f.readline()
    f.close()
    return punt
                
 
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
