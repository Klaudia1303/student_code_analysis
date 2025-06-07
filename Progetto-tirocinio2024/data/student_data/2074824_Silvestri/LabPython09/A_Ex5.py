def A_Ex5(filename,oggetto):
    anno = "2010"
    
    
    
    with open(filename, encoding="UTF-8") as file:
        csv = file.readlines()
        
        for i in range(1,len(csv)):
            csvI = csv[i].split(",")
            
            if csvI[0] == oggetto:
                maxVendita = 0
                for i in range(1,len(csvI)):
                    if int(csvI[i]) >= maxVendita:
                        maxVendita = int(csvI[i])
                        anno = "201"+str(i-1)
    
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
