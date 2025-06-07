def A_Ex4(filename,anno):
    f=open(filename, encoding="UTF-8")
    fin=f.readline()
    anni=fin.strip().split(',')
    contatore=0
    mass=0
    num=0
    prodotto=''
    for i in range(len(anni)):
        if anni[i]== str(anno):
            contatore=i
    fin=f.readlines()
    for j in range( len(fin)):
        s=fin[j].strip().split(',')
        num=s[contatore]
        print(num)
        if(int(num)>mass):
            mass=int(num)
            prodotto=s[0]
        if(int(num)==mass):
            if(s[0]>prodotto):
               prodotto=s[0]
    f.close()
    return prodotto
    
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
