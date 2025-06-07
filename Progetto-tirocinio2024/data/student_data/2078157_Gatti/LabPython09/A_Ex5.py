def A_Ex5(filename,oggetto):
    f = open(filename)
    anni = f.readline().strip().split(',')
    for riga in f:
        if oggetto in riga:
            l = riga.strip().split(',')
    massimo = 0
    top = 0
    for i in range(2,len(l)):
        if int(l[i]) - int(l[i - 1]) >= massimo:
            massimo = int(l[i]) - int(l[i - 1])
            top = int(l[i])
            pos = i
    if massimo == 0:
        return int(anni[1])
    f.close()
    for anno in anni:
        if anni.index(anno) == l.index(l[pos]):
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
