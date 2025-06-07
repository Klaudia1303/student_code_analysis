def A_Ex9(fileName,squadra):
    file=open(fileName,encoding='UTF-8')
    file=file.read().split('\n')
    score=0
    for i in range(1,len(file)):
        i=file[i].split(',')
        for j in range(2):
            
            if i!=[''] and i[j]==squadra:
                if int(i[j+2])>int(i[3-j]):
                    score+=3
                elif int(i[j+2])==int(i[3-j]):
                    score+=1
        
       
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
