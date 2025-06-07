def A_Ex9(fileName,squadra):
    
    punti = 0
    listaPartite = []
    
    ptiVittoria = 3
    ptiPareggio = 1
    
    with open(fileName, encoding="UTF-8") as file:
        csv = file.readlines()
        
        for elem in csv:
            listaPartite.append(elem.strip().split(","))
        print(listaPartite)
        
        for partita in listaPartite:
            if squadra in partita:
                if squadra == partita[0]:
                    risultatoSquadra = partita[2]
                    if risultatoSquadra > partita[3]:
                        punti += ptiVittoria
                    elif risultatoSquadra == partita[3]:
                        punti += ptiPareggio
                else:
                    risultatoSquadra = partita[3]
                    if risultatoSquadra > partita[2]:
                        punti += ptiVittoria
                    elif risultatoSquadra == partita[2]:
                        punti += ptiPareggio
                        
                        
    return punti
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Chelsea'] , 3)
    counter_test_positivi += tester_fun(A_Ex9, ["partite1.csv",'Tottenham'] , 1)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Arsenal'] , 4)
    counter_test_positivi += tester_fun(A_Ex9, ["partite2.csv",'Bayern'] , 0)
    counter_test_positivi += tester_fun(A_Ex9, ["partite3.csv",'Bayern'] , 4)

    print('La funzione',A_Ex9.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
