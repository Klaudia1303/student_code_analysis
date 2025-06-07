def A_Ex9(fileName,squadra):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    file=open(fileName,encoding='UTF-8')
    lines=file.readline().strip().split(',')
    lines=file.readline().strip().split(',')
    list=[]
    goals=0
    while lines!=['']:
        list.append(lines)
        lines=file.readline().strip().split(',')
    for line in list:
        if squadra in line:
            if int(line[2])==int(line[3]):
                goals+=1 
            else:
                analisis=line.index(squadra)
                if line.index(squadra)==0:
                    if line[line.index(squadra)+2]>line[3]:
                        goals+=3
                if line.index(squadra)==1:
                    if line[line.index(squadra)+2]>line[2]:
                        goals+=3
    return goals 
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
