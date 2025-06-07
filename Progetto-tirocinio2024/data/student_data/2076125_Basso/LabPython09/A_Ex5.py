def A_Ex5(filename,oggetto):
    f=open(filename)
    riga=f.readline()
    anni=riga.strip().split(',')
    anno=anni[1]

    d=0
    riga=f.readline()
    dati=riga.strip().split(',')
    
    while oggetto not in dati:
        riga=f.readline()
        dati=riga.strip().split(',')
    for a in range(1,len(dati)-1):
        if (int(dati[a+1])-int(dati[a])) >= d:
            anno=anni[a+1]
            d=(int(dati[a+1])-int(dati[a]))
    f.close()
    return int(anno)
            
        
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
