def A_Ex7(fileName):
    #"""MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    f=open(fileName,encoding='UTF-8')
    s=f.read()
    s=s.strip().split(',')
    stringa=s[0]
    f.close()
    L=[]
    k=0
    Numeri=['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(stringa)):
        if k!=0:
            k-=1
            continue
        numero=''
        if i+1<len(stringa) and Numeri.count(stringa[i+1])==0 and Numeri.count(stringa[i])==1:
            numero+=stringa[i]
            L.append(int(numero))
        if i+1<len(stringa) and Numeri.count(stringa[i+1])==1 and  Numeri.count(stringa[i])==1:
            numero+=stringa[i]
            while i+1<len(stringa) and Numeri.count(stringa[i+1])==1:
                k+=1
                numero+=stringa[i+1]
                i+=1
            L.append(int(numero))
    return sum(L)
        

 
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
