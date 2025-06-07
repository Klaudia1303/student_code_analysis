def A_Ex5(filename,oggetto):
    a=open(filename, encoding="UTF-8")
    sv=[]
    y=0
    for elem in a:
        elem=elem.strip().split(",")
        sv.append(elem)
    anno=int(sv[0][1])
    for i in range(len(sv)):
        if str(oggetto) in sv[i]:
            break
    for j in range(3,len(sv[i])):
        if int(sv[i][j])-int(sv[i][j-1])>int(sv[i][j-1])-int(sv[i][j-1]):
            y=int(sv[i][j])
            anno=int(sv[0][j])
    return anno
        

    
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
