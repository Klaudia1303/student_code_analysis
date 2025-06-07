def A_Ex8(fileName):
    file=open(fileName,encoding="UTF-8") 
    j=0 
    max=0 
    for i in file: 
        s="".join(i.strip().split(" ")) 
        c=0 
        j+= 1 
        for j in s: 
            if j.isupper(): 
                c += 1 
        if c>=max: 
            max=c 
            riga=j 
            
    file.close() 

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
