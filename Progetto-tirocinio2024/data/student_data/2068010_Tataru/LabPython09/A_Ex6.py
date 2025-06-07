def A_Ex6(filename):
    f=open(filename,encoding="UTF-8")
    a=f.readline()
    s=f.readlines()
    a=a.replace("\n","")
    for elem in '.,;:!?<>"-«»()\'':
        a=a.replace(elem," ")
    for i in range(0,len(s)):
        s[i]=s[i].replace("\n","")
        for elem in '.,;:!?<>"-«»()\'':
            s[i]=s[i].replace(elem," ")
    c=[]
    for i in range(1,len(a.split())):
        c.append(0)
    for i in s:
        l=i.split()
        for j in range(1,len(l)):
            c[j-1]+=int(l[j])
    return int(a.split()[c.index(max(c))+1])
    
     
###############################################################################

"""NON MODIFICARE, codice di testing della funzione"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(A_Ex6, ['Vendite1.csv'] , 2010)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite2.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite3.csv'] , 2013)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite4.csv'] , 2020)
    counter_test_positivi += tester_fun(A_Ex6, ['Vendite5.csv'] , 2022)

    print('La funzione',A_Ex6.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
