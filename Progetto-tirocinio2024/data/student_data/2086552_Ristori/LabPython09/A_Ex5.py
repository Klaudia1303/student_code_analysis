def A_Ex5(fileName,oggetto):
    fin=open(fileName,"r",encoding="UTF-8")
    riga=fin.readline()
    b=True
    while b:
        dati=riga.strip().split(",")
        if dati[0]==oggetto:
            b=False
        else:
            riga=fin.readline()
    crescitaMax=0
    indexMax=1
    for i in range(1,len(dati)-1):
        if int(dati[i+1])-int(dati[i])>=crescitaMax:
            crescitaMax=int(dati[i+1])-int(dati[i])
            indexMax=i+1
    fin.close()
    fin=open(fileName,"r",encoding="UTF-8")
    riga=fin.readline()
    dati=riga.strip().split(",")
    anno=int(dati[indexMax])
    return anno
    
    
    
            
        












    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
