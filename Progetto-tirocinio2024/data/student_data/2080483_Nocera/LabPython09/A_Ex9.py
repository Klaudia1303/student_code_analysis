def A_Ex9(fileName,squadra):
    fin=open(fileName,encoding="UTF-8")
    f1=fin.readline()
    
    
    puntisquadra=0
    for riga in fin:
        r=riga.strip().split(",")

        if squadra in r:   
            Tuple=tuple(r)
            posizionesquadra1=0
            posizionesquadra2=1

            if squadra==Tuple[1]:
                posizionesquadra1=1
                posizionesquadra2=0

            
            if int(Tuple[posizionesquadra1+2])>int(Tuple[posizionesquadra2+2]):
                puntisquadra+=3
            elif int(Tuple[2])==int(Tuple[3]):
                puntisquadra+=1
    fin.close()
    return puntisquadra
                
            
    
    
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
