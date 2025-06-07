def A_Ex4(filename,anno):
    f = open(filename, encoding="UTF-8")
    l = f.readlines()
    f.close()
    pos = (l[0].find (str(anno)))-1 #restituisce la posizione del 2 012 (-1 per virgola)
    virgola = 0
    massimo = 0
    while pos > 0 :
        pos = pos - 5
        virgola = virgola + 1
    for i in range (1,len(l)):
        l[i]=l[i].replace(',',' ',virgola-1) #lascio solo la virgola dell'anno
    for j in range (1,len(l)):
        l[j]= l[j]+'A'
        elem = l[j]
        k = 1
        num = ''
        while elem [elem.find(',')+k]!='A' and elem [elem.find(',')+k]!=',':
            num = num + elem[elem.find(',')+k]
            k = k+1
        num1 = int(num)
        if num1 > massimo :
            massimo = num1
            h = 0
            finale = ''
            while elem[h]!= ' ' and elem[h]!= ',':
                finale = finale + elem[h]
                h = h+1
    return(finale)

     
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
