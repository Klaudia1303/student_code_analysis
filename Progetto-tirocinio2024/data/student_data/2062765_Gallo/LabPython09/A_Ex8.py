def A_Ex8(fileName):
    f=open(fileName,"r",encoding="UTF-8")
    riga=f.readline()
    sos=0
    j=0
    numero=0
    massimo=0
    while len(riga)>0:
        for i in riga:
            if i.isalpha:
                numero+=1
        j+=1
        if numero>massimo:
            massimo=numero
            sos=j
        riga=f.readline()
    return sos
            




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
