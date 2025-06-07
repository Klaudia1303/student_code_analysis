def A_Ex9(fileName,squadra):
    elenco={}
    f=open(fileName,encoding="UTF-8")
    for i in f:
        i=i.strip().split(",")
        if i[2].isdecimal()==True:
            if int(i[2])>int(i[3]):
                if i[0] in elenco:
                    elenco[i[0]]+=3
                else:
                    elenco[i[0]]=3
                    elenco[i[1]]=0
            elif int(i[2])==int(i[3]):
                if i[0] in elenco and i[1] in elenco:
                    elenco[i[0]]+=1
                    elenco[i[1]]+=1
                else:
                    elenco[i[0]]=1
                    elenco[i[1]]=1
            else:
                if i[1] in elenco:
                    elenco[i[1]]+=3
                else:
                    elenco[i[1]]=3
                    elenco[i[0]]=0
    if squadra not in elenco:
        ris=0
    else:
        ris=elenco[squadra]
    return ris
                    
                        
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
