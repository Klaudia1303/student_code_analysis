def A_Ex9(fileName,squadra):
    f=open(fileName,'r',encoding='UTF-8')
    consegna=f.readline()
    punteggio=0
    for riga in f:
        riga=riga.strip().split(',')
        if riga[0]==squadra:
            if int(riga[2])>int(riga[3]):
                punteggio+=3
            elif int(riga[2])==int(riga[3]):
                punteggio+=1
        elif riga[1]==squadra:
            if int(riga[2])<int(riga[3]):
                punteggio+=3
            elif int(riga[2])==int(riga[3]):
                punteggio+=1
            
    f.close()
    return punteggio
    
    
 
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
