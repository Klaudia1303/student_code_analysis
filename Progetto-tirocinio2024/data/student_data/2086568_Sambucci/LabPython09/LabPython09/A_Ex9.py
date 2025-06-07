def A_Ex9(fileName,squadra):
    fin=open(fileName,encoding="UTF-8")
    f=fin.readline()
    punteggio=0
    for riga in fin:
        risultato=riga.strip().split(",")
        if squadra in risultato:
            pos=risultato.index(squadra)
            golsquadra1=int(risultato[pos+2])
            if pos == 0:
                golsquadra2=int(risultato[pos+3])
            else:
                golsquadra2=int(risultato[pos+1])
            if golsquadra1 > golsquadra2:
                punteggio+=3
            elif golsquadra1 == golsquadra2:
                punteggio+=1
    
    fin.close()
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
