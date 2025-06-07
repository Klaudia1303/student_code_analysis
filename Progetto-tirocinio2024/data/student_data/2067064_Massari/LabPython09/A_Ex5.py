def A_Ex5(filename,oggetto):
    f=open(filename,encoding="UTF-8")
    t=f.readlines()
    testo=[]
    riga_ogg=''
    numax=0
    posizione=''

    for i in t:
        testo.append(i.strip().split(","))

    for x in range(len(testo)):
        riga=testo[x]
        if oggetto in riga:
            riga_ogg=x

    frase=testo[riga_ogg]
            
    for elem in range(1,len(frase)):
        numero=int(frase[elem])
        if numero>=numax:
            numax=numero
            posizione=elem

    riga1=testo[0]

    f.close()
    

    
    return int(riga1[posizione])




    
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
