def A_Ex5(filename,oggetto):
    f=open(filename, encoding='UTF-8')
    years=f.readline().strip().split(',')
    increment=0
    max_year=0
    for line in f.readlines():
        line=line.strip().split(',')
        (obj,sales)=(line[0],line[1:])
        increased=False
        if obj==oggetto:
            for i in range(len(sales)-1):
                difference=int(sales[i+1])-int(sales[i])
                if difference>increment:
                    max_year=int(years[i+2])
                    increment=difference
                    increased=True
                elif difference==increment:
                    max_year=max(max_year,int(years[i+2]))
                    increased=True
                elif difference<increment and not increased:
                    max_year=int(years[1])
    return max_year
                    
    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

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
