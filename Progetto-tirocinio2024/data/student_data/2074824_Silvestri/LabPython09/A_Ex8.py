def A_Ex8(fileName):
    with open(fileName, encoding="UTF-8") as file:
        kFile = file.readlines()
        
        
        maxCount = 0
        index = 0
        
        
        for i in range(len(kFile)):
            kLinea = kFile[i].strip()
            for char in kLinea:
                if not char.isupper():
                    kLinea = kLinea.replace(char,"")
                    
            
            if len(kLinea.strip()) >= maxCount:
                maxCount = len(kLinea)
                index = i+1
                
    return index
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
