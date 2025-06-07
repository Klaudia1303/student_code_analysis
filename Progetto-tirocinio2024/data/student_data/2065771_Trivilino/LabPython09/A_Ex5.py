def A_Ex5(filename,oggetto):
    f=open(filename,encoding="UTF-8")
    anni=f.readline().strip().split(",")

    dati=[]
    while oggetto not in dati:
        riga=f.readline()
        dati=riga.strip().split(",")

    incremento=0
    for vendite in range(2,len(dati)):
        if int(dati[vendite])-int(dati[vendite-1])>=incremento:
            anno=int(anni[vendite])
            incremento=int(dati[vendite])-int(dati[vendite-1])
    if incremento==0:
        anno=int(anni[1])

    f.close()
        
    return anno
     

    
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
