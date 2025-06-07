def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    with open(filename,'r',encoding="UTF-8") as f:
        anni=f.readline().strip().split(',')
        
        massimo_aumento=0
        massimo_aumento_anno=0
        righe=f.readlines()
        for riga in righe:
            riga=riga.strip().split(',')
            (ogg, vendite)=(riga[0],riga[1:])

            aumentato=False
                
            if ogg==oggetto:
                for i in range(len(vendite)-1):
                    diff=int(vendite[i+1])-int(vendite[i])

                    if diff>massimo_aumento:
                        massimo_aumento_anno=int(anni[i+2])
                        massimo_aumento=diff
                        aumento=True
                    elif diff==massimo_aumento:
                        massimo_aumento_anno=max(massimo_aumento_anno,int(anni[i+2]))
                        aumentato=True
                    elif diff<massimo_aumento and not aumentato:
                        massimo_aumento_anno=int(anni[1])
        return massimo_aumento_anno
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Giubbotto'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite1.csv','Zaino'] , 2010)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Maglione'] , 2012)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite2.csv','Zaino'] , 2013)
    counter_test_positivi += tester_fun(A_Ex5, ['Vendite3.csv','Giubbotto'] , 2013)

    print('La funzione',A_Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
