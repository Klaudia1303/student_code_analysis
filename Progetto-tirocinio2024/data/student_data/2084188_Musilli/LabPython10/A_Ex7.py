def A_Ex7(file):
    with open(file,encoding="UTF-8") as f:
        Data=[line.strip().split(",") for line in f.readlines()[1:]] #Data è una tabella che contiene le rige
    squadre=[line[:2] for line in Data] # prendo le prime 2 colonne di Data che sono le squadre
    squadre={item for line in squadre for item in line} #si trasforma la lista multidimensionale in unidimensionale
    squadre={key:0 for key in squadre} #creazione alternativa del dizionario
    #per abbreviare le precedenti 2 istruzioni si può scrivere direttamente
    #squadre={item:0 for line in squadre for item in line}
    for key in squadre: #vediamo le siangoli chiavi all'interno del dizionario
        for line in Data:   #andiamo a prendere la singola riga proveniente da Data 
            if key in line: #se presente la chiave nella riga procede con le istruzioni
                #da qui in poi si effettuano i calcoli per ridare i punteggi
                if line[2]==line[3]: squadre[key]+=1    
                else:
                    squadra1={line[0]:int(line[2])};    squadra2={line[1]:int(line[3])}
                    if key in squadra1.keys():
                        if int(line[2])>int(line[3]):   squadre[key]+=3 
                    else:
                        if int(line[2])<int(line[3]):   squadre[key]+=3 
    return squadre
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""

 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, ["partite1.csv"] , {'Chelsea': 3, 'Everton': 3, 'Arsenal': 4, 'Tottenham': 1})
    counter_test_positivi += tester_fun(A_Ex7, ["partite2.csv"] , {'Chelsea': 4, 'Everton': 6, 'Arsenal': 4, 'Tottenham': 2})
    counter_test_positivi += tester_fun(A_Ex7, ["partite3.csv"] , {'Bayern': 4, 'Schalke': 3, 'Amburgo': 4, 'Werder': 1, 'Colonia': 4, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite4.csv"] , {'Bayern': 8, 'Schalke': 6, 'Amburgo': 8, 'Werder': 2, 'Colonia': 8, 'Stoccarda': 0})
    counter_test_positivi += tester_fun(A_Ex7, ["partite5.csv"] , {'Bayern': 5, 'Schalke': 6, 'Amburgo': 5, 'Werder': 5, 'Colonia': 5, 'Stoccarda': 6})

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
