def A_Ex8(fileName):
    f=open(fileName, encoding="UTF-8")
    file=f.readlines()
    f.close()
    mass=0
    maiuscole=0
    rigamass=0
    print(file)
    for i in range(len(file)):
        riga=file[i].strip()
        for elem in riga:
            if elem.isupper()==True:
                maiuscole=maiuscole+1
        if maiuscole>=mass:
            mass=maiuscole
            rigamass=i+1
        maiuscole=0
    return rigamass
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
