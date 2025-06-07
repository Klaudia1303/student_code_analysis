def A_Ex5(filename,oggetto):
    fin=open(filename,encoding="UTF-8")
    crescitamax=0
    Caratt=fin.readline().strip().split(",")
    annomax=int(Caratt[1])
    for riga in fin:
        dati=riga.strip().split(",")
        if oggetto in dati:
            qiniz=int(dati[1])
            for i in range(2,len(dati)):
                if int(dati[i])-qiniz > crescitamax:
                    crescitamax=int(dati[i])-qiniz
                    annomax=int(Caratt[i])
                elif int(dati[i])-qiniz == crescitamax:
                    if int(Caratt[i])>annomax:
                        crescitamax=int(dati[i])-qiniz
                        annomax=int(Caratt[i])
                qiniz=int(dati[i])
                        
    fin.close()
    return annomax
        

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
