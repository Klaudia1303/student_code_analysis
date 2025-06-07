def A_Ex9(fileName,squadra):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

    f=open(fileName,"r",encoding="UTF-8")
    t=f.readline()

    vittorie=[]
    sconfitte=[]
    pareggi=[]
    indice_sq=0
    for riga in f:
        riga=riga.strip().split(",")
        for i in range(len(riga)):
            if riga[i]==squadra and i<2:
                indice_sq=i
                if riga[2]==riga[3]:
                    pareggi.append(1)
                    continue
                if indice_sq==0:
                    if riga[2]>riga[3]:
                        vittorie.append(1)
                    else:
                        sconfitte.append(1)
                else:
                    if riga[3]>riga[2]:
                        vittorie.append(1)
                    else:
                        sconfitte.append(1)
    somma_pareggi=sum(pareggi)
    somma_vittorie=sum(vittorie)
    somma_sconfitte=sum(sconfitte)
    
    punteggio=(3*somma_vittorie)+((0)*somma_sconfitte)+(1*somma_pareggi)
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
