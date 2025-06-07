def A_Ex9(fileName,squadra):
    f = open(fileName, encoding="UTF-8")
    l = f.readlines()
    f.close()
    print(l)

    listElem = []

    for line in l:
        listElem.append(line.strip().split(","))
    print(listElem)

    totalScore = 0

    for line in listElem:
        if squadra in line:
            score_sq1 = 0
            score_sq2 = 0
            if line[2] > line[3]:
                score_sq1 = 3
            elif line [2] < line[3]:
                score_sq2 = 3
            else:
                score_sq1 = 1
                score_sq2 = 1

            if squadra == line[0]:
                totalScore += score_sq1
            elif squadra == line[1]:
                totalScore += score_sq2
    return totalScore
 
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
