def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    file=open(filename, encoding='UTF-8')
    lista=[]
    for elem in file:
        elem=elem.strip().split(',')
        lista.append(elem)
    oggetti=[]
    for counter in lista:
        oggetti.append(counter[0])
    ogPos=oggetti.index(oggetto)
    topYear=lista[0][1]
    for counter in range(1,len(lista[ogPos])-1):
        if (int(lista[ogPos][counter+1]))-(int(lista[ogPos][counter]))>0:
            print((int(lista[ogPos][counter+1]))-(int(lista[ogPos][counter])))
            topYear=lista[0][counter+1]
    file.close()    
    return int(topYear)
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
