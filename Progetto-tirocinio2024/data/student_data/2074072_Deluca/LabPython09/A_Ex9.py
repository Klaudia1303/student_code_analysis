def A_Ex9(fileName,squadra):
    f=open(fileName,encoding="UTF-8")
    S=f.readline()
    s=f.read()
    s1=s.strip().replace("\n",";")
    l=s1.strip().split(";")
    l1=[]
    punti=0
    for elem in l:
        elem1=elem.strip().split(",")
        l1.append(elem1)
    for elem in l1:
        if elem[0]==squadra:
            if int(elem[2])>int(elem[3]):
                punti+=3
            elif int(elem[2])==int(elem[3]):
                punti+=1
        elif elem[1]==squadra:
            if int(elem[2])<int(elem[3]):
                punti+=3
            elif int(elem[2])==int(elem[3]):
                punti+=1
        else:
            continue
    f.close()     
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
