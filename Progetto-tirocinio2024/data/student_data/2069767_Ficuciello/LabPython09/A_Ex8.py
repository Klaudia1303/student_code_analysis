def A_Ex8(fileName):
    f=open(fileName,encoding="UTF-8")
    r=0
    mass=0
    for i in f:
        x="".join(i.strip().split(" "))
        c=0
        r+=1
        for j in x:
            if j.isupper():
                c+=1
        if c>=mass:
            mass=c
            riga=r
    f.close()
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
