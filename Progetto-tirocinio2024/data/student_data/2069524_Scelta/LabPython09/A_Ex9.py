def A_Ex9(fileName,squadra):
    file=open(fileName,'r',encoding='UTF-8')
    f=file.readlines()
    punti_squad_1=0
    for elem in f:
        elem=elem.strip().split(",")
        
    
        if elem[0]==squadra:
            if int(elem[2])>int(elem[3]):
                punti_squad_1+=3
            
            if int(elem[2])==int(elem[3]):
                punti_squad_1+=1
                
        if elem[1]==squadra:
            if int(elem[3])>int(elem[2]):
                punti_squad_1+=3
                
            if int(elem[2])==int(elem[3]):
                punti_squad_1+=1
                
    file.close()
    return punti_squad_1
            
      

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
