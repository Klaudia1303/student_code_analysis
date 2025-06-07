def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    file = open(filename,'r',encoding='UTF-8')
    incremento = 1
    anno = 1
    anni = file.readline().strip().split(',')
    for riga in file:
        val = riga.strip().split(',')
        for i in range(2,len(val)):
            if(val[0] == oggetto):
                if(int(val[i]) - int(val[i - 1]) >= incremento):
                    anno = anni[i]
          
                    incremento = int(val[i]) - int(val[i - 1])
                    print('faccio :' + (val[i]) + ' - ' + (val[i - 1] ))
                    print(incremento)
                if(int(val[i]) - int(val[i - 1]) == incremento):
                    if(int(anno) < int(anni[i])):
                        anno = anni[i]
                        incremento = int(val[i]) - int(val[i - 1])
    if(anno == 1):
        anno = anni[1]
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
