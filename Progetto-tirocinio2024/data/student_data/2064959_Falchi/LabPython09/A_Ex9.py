def A_Ex9(fileName,squadra):
    
    squadre = set()
    
    with open(fileName, "r", encoding="UTF-8") as file:
        titoli = file.readline().strip().split(",")

        #print(titoli)

        for rigaGrezza in file.readlines():
            riga = rigaGrezza.strip().split(",")
            
            #print(riga)
            squadre.add(riga[0])
            squadre.add(riga[1])

    squadre = list(squadre)
    squadre.sort()
    print(squadre)

    punteggi = [0 for i in range(len(squadre))]

    with open(fileName, "r", encoding="UTF-8") as file:
        titoli = file.readline().strip().split(",")

        #print(titoli)

        for rigaGrezza in file.readlines():
            riga = rigaGrezza.strip().split(",")
            
            if int(riga[2]) > int(riga[3]):
                punteggi[squadre.index(riga[0])] += 3
            elif int(riga[2]) == int(riga[3]):
                punteggi[squadre.index(riga[0])] += 1
                punteggi[squadre.index(riga[1])] += 1
            else:
                punteggi[squadre.index(riga[1])] += 3

            #print(riga)
    
    
    print(punteggi)
    
    #######################################################
    #EXTRA: (stampa la classifica ordinata delle squadre)
    classifica = list()

    for i in range(len(squadre)):
        stringa = str(punteggi[i]), "\t - \t", str(squadre[i])
        classifica.append(stringa)
        print(str(squadre[i]), "-", punteggi[i], sep="\t")

    classifica.sort()
    classifica.reverse()
    ######################################################

    if squadra in squadre:
        output = punteggi[squadre.index(squadra)]
    else:
        output = 0

    return output 

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
