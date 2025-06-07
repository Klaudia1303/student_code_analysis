def A_Ex5(filename,oggetto):
    f=open(filename,'r',encoding='UTF-8')
    a=f.readline().strip().split(',') #prendo la prima riga, non tutte perchè fuori dal ciclo for, e crea una lista
    M=0 #inizializza il massimo
    pos=1
    for line in f: 
        s=line.strip().split(',') #trasforma tutte le stringhe in liste
        if oggetto in s: #controlla se l'oggetto sta nella stringa, stringa per stringa
            for i in range(2,len(s)): #controllo i numeri presenti nella lista dalla posizione 2
                                        #alla fine per trovare quale differenza tra il numero e il
                                        #suo precedente è maggiore!!
                if int(s[i])-int(s[i-1])>=M:
                    M=int(s[i])-int(s[i-1])
                    pos=i

    f.close()
    res=int(a[pos])
    return res

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
