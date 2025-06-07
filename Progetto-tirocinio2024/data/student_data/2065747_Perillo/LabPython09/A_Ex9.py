def A_Ex9(fileName,squadra):
    fin=open(fileName,encoding="utf-8")
    partite=[]
    punti=0
    for i in fin:
        i=i.strip().split(",")
        partite.append(i)
    partite.remove(partite[0])
    for match in partite:
        if squadra in match:
            if squadra==match[0]:
                if match[2]>match[3]:
                    punti+=3
                elif match[2]==match[3]:
                    punti+=1
            elif squadra==match[1]:
                 if match[3]>match[2]:
                    punti+=3
                 elif match[2]==match[3]:
                    punti+=1
    return(punti)
                
                
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
