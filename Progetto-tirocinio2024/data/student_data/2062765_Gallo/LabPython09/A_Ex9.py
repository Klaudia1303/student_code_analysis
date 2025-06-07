def A_Ex9(fileName,squadra):
    f=open(fileName,"r",encoding="UTF-8")
    dati=f.read().split("\n")
    a=0
    for i in range(1,len(dati)):
        team=dati[i].split(",")
        for j in range(2):
            if team!="" and (team[j])==squadra:
                if int(team[j+2])==int(team[3-j]):
                    a+=1
                elif int(team[j+2])>int(team[3-j]):
                    a+=3
    return a
                    
    
 
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
