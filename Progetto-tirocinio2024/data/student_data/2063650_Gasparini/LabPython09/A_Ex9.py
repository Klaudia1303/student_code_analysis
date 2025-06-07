def A_Ex9(fileName,squadra):
    with open(fileName,encoding="UTF-8") as f:
        fields = [line.rstrip("\n").split(",") for line in f][1:]
        score = 0
        for row in fields:
            if squadra not in row:
                continue
            goals = (int(row[2]), int(row[3]))
            scores = (1, 1)
            if goals[0] > goals[1]:
                scores = (3, 0)
            elif goals[1] > goals[0]:
                scores = (0, 3)
            score += scores[row.index(squadra)]
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
