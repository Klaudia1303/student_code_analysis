def A_Ex7(fileName):
    f=open(fileName, 'r', encoding='UTF-8')
    s=f.read()
    f.close()
    l2=[]
    lista=[]
    somma=0

    l=s.strip().split()

    for i in l:
        if(i.isdecimal()==True):
            l2.append(i)
    
    for j in l2:
        somma+=int(j)

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
