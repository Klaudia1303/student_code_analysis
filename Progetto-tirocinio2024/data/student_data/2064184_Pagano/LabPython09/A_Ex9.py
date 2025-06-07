def A_Ex9(fileName,squadra):
    with open(fileName, encoding="UTF-8") as f:
        dataset = [row.strip().split(",") for row in f.readlines()]
        dataset.pop(0)

        # ciclo per ottenere le squadre
        teams = set()
        for data in dataset:
            teams.add(data[0])
            teams.add(data[1])

        # ciclo per ottenere il punteggio della squadra
        score = 0
        for data in dataset:
            if squadra in data:
                ind = data.index(squadra) # indice punteggio team
                step = 1 if ind==0 else -1 # indice punteggio avversario
                score1 = int(data[ind+2]) # team
                score2 = int(data[ind+2+step]) # avversario
                if score1 > score2:
                    score += 3
                elif score1 == score2:
                    score += 1
        return score

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
