def A_Ex9(fileName,squadra):
    file=open(fileName,'r',encoding='UTF-8')
    a=0
    for riga in file:
        riga=riga.strip().split(',')
        if squadra in riga:
            if squadra==riga[0]:
                if int(riga[2])>int(riga[3]):
                    a=a+3
                elif int(riga[2])==int(riga[3]):
                    a=a+1
            elif squadra==riga[1]:
                if int(riga[3])>int(riga[2]):
                    a=a+3
                elif int(riga[2])==int(riga[3]):
                    a=a+1
    return a
                    
        
        

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
