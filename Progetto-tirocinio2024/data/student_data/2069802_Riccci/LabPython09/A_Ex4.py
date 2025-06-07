def A_Ex4(filename,anno):
    f = open(filename, encoding="UTF-8")
    s = f.readline().replace('\n','')
    indice = 0
    cont = len(s.split(','))
    for i in range(0, cont):
        if(s.split(',')[i] == str(anno)):
            indice = i
            break
    file = []
    for riga in f:
        file.append(riga.replace('\n',''))
    f.close()
    nome = ''
    cont = 0
    for riga in file:
        if(int(riga.split(',')[indice]) > cont):
            cont = int(riga.split(',')[indice])
            nome = riga.split(',')[0]
        elif(int(riga.split(',')[indice]) == cont and ord(riga.split(',')[0][0] >= ord(nome)[0])):
             nome = riga.split(',')[0]
    return(nome)
    
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
