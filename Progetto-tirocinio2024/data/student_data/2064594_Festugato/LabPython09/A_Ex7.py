def A_Ex7(fileName):
    somma = 0
    file = open(fileName,'r',encoding= 'UTF-8')
    

    

    s = file.read().strip().split() #lista di parole e numeri
    #print(s)

    for c in s :
        
        if c.isdigit() == True : #verifica che c sia un numero
            print(c)
            c = int(c)
            somma += c

    file.close()

    return somma
    
            

















    

 
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex7, ["file1.txt"] , 14)
    counter_test_positivi += tester_fun(A_Ex7, ["file2.txt"] , 17)
    counter_test_positivi += tester_fun(A_Ex7, ["file3.txt"] , 18)
    counter_test_positivi += tester_fun(A_Ex7, ["file4.txt"] , 20)
    counter_test_positivi += tester_fun(A_Ex7, ["file5.txt"] , 0)

    print('La funzione',A_Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
