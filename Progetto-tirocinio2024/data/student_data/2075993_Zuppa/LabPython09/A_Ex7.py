def A_Ex7(fileName):
    fin=open(fileName,encoding='UTF-8')
    st=fin.read()
    fin.close()
    s=0
    i=0
    while i <len(st):
        if st[i].isdecimal():
            c=st[i]
            for j in range(i+1,len(st)):
                if st[j].isdecimal():
                    c+=st[j]
                    i+=1
                else:
                    break
            s+=int(c)
        i+=1
    return s
 
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
