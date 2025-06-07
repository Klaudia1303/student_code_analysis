def A_Ex7(fileName):
    f=open(fileName,encoding="UTF-8")
    s=f.read()
    count=0
    countpar="0"
    i=0
    while i<len(s)-1:
        if s[i].isdecimal():
            countpar+=s[i]
            if s[i+1].isdecimal():
                 countpar+=s[i+1]
                 i+=1
            else:
                count+=int(countpar)
                countpar="0"
        else:
            count+=int(countpar)
            countpar="0"
        i+=1
    f.close()
    return count

 
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
