def A_Ex4(fileName,anno):

    numeroAnni = 0
    anni = list()

    articoli = list()
    vendite = list()
    
    with open(fileName, "r", encoding = "UTF-8") as file:
        titoli = file.readline().strip().split(",")

        print(titoli)
        
        for i in range(1,len(titoli)):
            anni.append(titoli[i])

        #print(anni)
        
        riga = file.readline()
       

        while len(riga) > 0:
            dati = riga.strip().split(",")
            print(dati)
            
            if str(anno) in anni:
                pos = titoli.index(str(anno))

                articoli.append(dati[0])
                vendite.append(dati[pos])
                
            
            riga = file.readline()

    print(articoli)
    print(vendite)

    articolo = ""
    massimo = 0
    
    for i in vendite:
        if int(i) > int(massimo):
            massimo = i
            articolo = articoli[vendite.index(i)]
        elif i == 0:
            if articolo > articoli[vendite.index(i)]:
                massimo = i
                articolo = articoli[vendite.index(i)]

    return articolo

###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ['Vendite1.csv',2012] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2012] , 'Maglione')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite2.csv',2013] , 'Zaino')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2011] , 'Giubbotto')
    counter_test_positivi += tester_fun(A_Ex4, ['Vendite3.csv',2010] , 'Cellulare')
    
    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
