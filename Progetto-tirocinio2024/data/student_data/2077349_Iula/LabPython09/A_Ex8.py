def A_Ex8(fileName):
    f=open(fileName,'r',encoding="UTF-8")
    lfile=[]
    s=""
    conto=0
    for el in f:
        l=el.split()
        for c in range(len(l)):
            s+=l[c]
        lfile.append(s)
    for i in range(len(lfile)):
        count=0
        for j in range(len(lfile[i])):
            if lfile[i][j].isupper:
                count+=1
        if count>=conto:
            conto=count
            riga=i+1
        else:
            riga=i
    return riga
        
 
###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex8, ["file1.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file2.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file3.txt"] , 2)
    counter_test_positivi += tester_fun(A_Ex8, ["file4.txt"] , 3)
    counter_test_positivi += tester_fun(A_Ex8, ["file5.txt"] , 3)

    print('La funzione',A_Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
