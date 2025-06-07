def A_Ex7(fileName):
    f= open (fileName,encoding="UTF-8")
    s = f.read()
    f.close()
    totale = 0
    i = 0
    while i < len(s):
        if s[i].isnumeric() == True:
            numero = ''
            while s[i].isnumeric() == True:
                numero = numero + s[i]
                i= i+1
            numero = int(numero)
            totale = totale +numero
        i = i + 1
    return(totale)


 
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
