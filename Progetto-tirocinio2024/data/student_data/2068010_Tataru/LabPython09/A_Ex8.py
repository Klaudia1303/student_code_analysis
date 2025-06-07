def A_Ex8(fileName):
    f=open(fileName,encoding="UTF-8")
    s=f.readlines()
    for i in range(0,len(s)):
        s[i]=s[i].replace("\n","")
        for elem in ' .,;:!?<>"-«»()\'':
            s[i]=s[i].replace(elem,"")
    mx=0
    ind=1
    ci=0

    for i in s:
        ci+=1
        c=0
        i=sorted(i)
        for j in i:
            if(j.isupper()==True):
                c+=1
            else:
                break
        if (c>=mx):
            ind=ci
            mx=c
    return ind

            

        
        
     
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
