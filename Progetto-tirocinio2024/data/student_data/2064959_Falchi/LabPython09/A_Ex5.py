def A_Ex5(fileName,oggetto):

    numeroAnni = 0
    anni = list()

    year = None
    
    with open(fileName, "r", encoding = "UTF-8") as file:
        titoli = file.readline().strip().split(",")

        for i in range(1, len(titoli)):
            numeroAnni += 1
            anni.append(titoli[i])

        print(numeroAnni, anni)

        #riga = file.readline()
        
        '''while len(riga) > 0:
            dati = riga.strip().split(",")
            #print(dati)

            if dati[0] == oggetto:

                vendite = list()
                
                for i in dati:
                    if i.isalpha():
                        continue
                    vendite.append(i)

                prec = int(vendite[0])
                crescita = list()
                
                for i in range(1, len(vendite)):

                    annoCorr = dati[i]
                    differenza = 0
                    prec = int(vendite[i-1])

                    if int(vendite[i]) - prec >= differenza:
                        differenza = int(vendite[i]) - prec
                        crescita.append(differenza)
                    else:
                        year = annoCorr
                        break

                print(crescita)
                
                year = int(anni[crescita.index(max(crescita))])
            
            riga = file.readline()'''

        for rigaGrezza in file:
            riga = rigaGrezza.strip().split(",")
            #print(riga)

            if riga[0] != oggetto:
                continue
            
            crescita = list()

            differenza = 0
            storedValue = 0

            for i in range(2, len(riga)):


                differenza = int(riga[i]) - int(riga[i-1])
                #print("diff", differenza)
                #print("stor", storedValue)
                if differenza >= storedValue:
                    storedValue = differenza
                    year = int(anni[i - 1])
            
            if year == None:
                year = int(anni[0])
    return year
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
