def A_Ex9(fileName,squadra):
    f=open(fileName,'r',encoding="UTF-8")
    lfile=[]
    somma=0
    for el in f:
        l=el.split(',')
        for c in range(len(l)):
            l[c]=l[c].strip()
        lfile.append(l)
    for i in range(1,len(lfile)):
        for j in range(len(lfile[i])):
            if lfile[i][j]==squadra:
                if j==0:
                    if int(lfile[i][2])>int(lfile[i][3]):
                        somma+=3
                    elif int(lfile[i][2])==int(lfile[i][3]):
                        somma+=1
                if j==1:
                    if int(lfile[i][3])>int(lfile[i][2]):
                        somma+=3
                    elif int(lfile[i][2])==int(lfile[i][3]):
                        somma+=1
    return somma
                
 
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
