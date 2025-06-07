def A_Ex5(filename,oggetto):
    f=open(filename,"r",encoding="UTF-8")
    riga=f.readline()
    anni=riga.strip().split(",")
    a=0
    massimo=0
    while len(riga)>0:
        riga=f.readline()
        if len(riga)>0:
            dati=riga.strip().split(",")
            if str(dati[0])==str(oggetto):
                for i in range (len(dati)-1,0,-1):
                    if int(dati[i])>=massimo:
                        massimo=int(dati[i])
                        a=i
    f.close()
    return int(anni[a])
        
            
    

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
