def A_Ex5(filename,oggetto):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    file=open(filename)
    file=file.readlines()
    aumento=0
    year=0
    firstLine=file[0].strip().split(",")
    for i in range(1,len(file)):
        line = file[i].strip().split(",")
        if line[0]==oggetto:
            for j in range(2, len(line)):
                if int(line[j])-int(line[j-1])>aumento:
                    aumento=int(line[j])-int(line[j-1])
                    year=firstLine[j]
                    print(year)
                if int(line[j])-int(line[j-1])==aumento:
                    if firstLine[j] > firstLine[j-1]:
                        year=firstLine[j]
                    else:
                        year=firstLine[j-1]
    return int(year)
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
