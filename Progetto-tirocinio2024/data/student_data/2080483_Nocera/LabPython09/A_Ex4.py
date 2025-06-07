def A_Ex4(filename,anno):
    strn=[]
    Maxv=0
    fin=open(filename,encoding="UTF-8")
    f=fin.readline()
    f1=f.strip().split(",")
    posizione=f1.index(str(anno))
    for riga in fin:
        r=riga.strip().split(",")
        strn.append(r)
    for vendita in strn:
        if int(vendita[posizione])>Maxv:
             Maxv=int(vendita[posizione])
             oggetto=vendita[0]
        elif int(vendita[posizione])==Maxv:
            if ord(vendita[0][0])<ord(oggetto[0]):
                oggetto=(vendita[0])
    fin.close()
    return oggetto
        
        
        
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
     
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
