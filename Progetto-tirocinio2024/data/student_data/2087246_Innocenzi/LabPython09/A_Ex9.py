def A_Ex9(fileName,squadra):
    file = open(fileName,encoding="UTF-8") 
    file.readline()
    points=0
    for i in file:
        l=i.strip().split(',') 
        if l[0]==squadra: 
            if int(l[2])>int(l[3]): 
                points += 3 
            if int(l[2])==int(l[3]): 
                points+=1 
        elif l[1]==squadra: 
            if int(l[3])>int(l[2]): 
                points+=3 
            if int(l[3])==int(l[2]): 
                points+=1 
    file.close() 

    return points 
 
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
