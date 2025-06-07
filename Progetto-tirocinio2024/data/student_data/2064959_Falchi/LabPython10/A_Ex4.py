def A_Ex4(fileName):
    d = dict()
    votoMinimo = 18
    
    with open(fileName, "r", encoding="UTF-8") as file:
        titoli = file.readline().strip().split(",")

        riga = file.readline().strip().split(",")
        
        while len(riga) > 1:
            matricola = int(riga[0])
            voto = int(riga[1])
            materia = riga[2]

            if matricola not in d: #Inizializza la chiave.
                d[matricola] = 0

            if voto >= votoMinimo:
                d[matricola] += 1

            riga = file.readline().strip().split(",")

        filtro = list()
        
        for chiave in d:
            if d[chiave] == 0:
                filtro.append(chiave)

        for elem in filtro:
            d.pop(elem)
            
        return d
            

###############################################################################


"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex4, ["esami1.csv"] , {1345: 1, 1346: 1, 1896: 1, 1753: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami2.csv"] , {1346: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami3.csv"] , {1347: 2, 1348: 1, 1349: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami4.csv"] , {1100: 1, 1012: 1, 1021: 1})
    counter_test_positivi += tester_fun(A_Ex4, ["esami5.csv"] , {1345: 1, 1987: 1, 1346: 1, 1896: 1})

    print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
