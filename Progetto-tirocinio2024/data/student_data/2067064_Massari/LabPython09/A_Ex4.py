def A_Ex4(filename,anno):
    f=open(filename,encoding="UTF-8")
    testo=f.readlines()
    testo_pulito=[]
    risultato=''
    massimo=0
    posizione_data=''

    

    for riga in testo:
        testo_pulito.append(riga.strip().split(","))
    riga1=testo_pulito[0]

    for x in range(1,len(riga1)):
        data=riga1[x]
        if int(data)==anno:
            posizione_data=x

    for y in range(1,len(testo_pulito)):
        riga_t=testo_pulito[y]
        vendita_ogg=int(riga_t[posizione_data])
        ogg=riga_t[0]
        if vendita_ogg>massimo:
            massimo=vendita_ogg
            risultato=ogg
        if vendita_ogg==massimo and ogg>risultato:
            risultato=ogg

    f.close()
        
            

    return risultato











    
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
