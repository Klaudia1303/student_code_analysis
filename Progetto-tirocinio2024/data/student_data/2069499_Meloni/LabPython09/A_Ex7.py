def A_Ex7(fileName):
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    fin=open(fileName,encoding="UTF-8")
    s=fin.read()
    fin.close()

    s1=s
    utili='1234567890'
    inutili=''

    for i in range(len(s)):
        if s[i] not in utili:
            s1=s1.replace(s[i],' ')

    somma=0
    numeri=[int(n)for n in s1.split() if n.isdigit()]

    for i in numeri:
        somma+=i
        
    return (somma)
 
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
