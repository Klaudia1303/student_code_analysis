def A_Ex5(filename,oggetto):
    listaAnni = list()
    file = open(filename,'r',encoding='UTF-8')

    anni = file.readline()
    colonne = anni.strip().split(',')

    for a in range(1,len(colonne)):
        listaAnni.append(colonne[a])
    print('anni',listaAnni)


    
    print(colonne)
    M = 0
    anno = 1

    for riga in file:
        riga = riga.strip().split(',')
        if riga[0] == oggetto:

            for i in range(2,len(riga)):
                dif = int(riga[i]) - int(riga[i-1])
                print(dif)

                

                if dif > M:
                    M= dif
                    anno = i
                    print(anno,i)
                if dif == M:
                    M = dif
                    anno = i


    file.close()

    return int(listaAnni[anno-1])
                
                    

                

                
    

    

    

    




                    
                

                    

            

            

            

        
    
















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
