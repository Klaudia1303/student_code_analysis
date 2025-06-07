def A_Ex7(fileName):
    f=open(fileName,encoding="UTF-8")
    s=f.readlines()
    for i in range(0,len(s)):
        s[i]=s[i].replace("\n","")
        for elem in '.,;:!?<>"-«»()\'':
            s[i]=s[i].replace(elem," ")
    c=0
    for i in s:
        l=i.split()
        for j in l:
            if (j.isnumeric()==True):
                c+=int(j)
    return c
        
 
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
