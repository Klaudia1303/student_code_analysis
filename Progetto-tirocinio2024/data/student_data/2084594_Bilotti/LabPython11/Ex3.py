def Ex3(file):
    var1 = open(file,encoding="utf-8")
    var2 = var1.read()
    var3 = r'\b\w*(\w)(\w)\w*\b\W*\b\w*\1\1\w*\b\W*\b\w*\1\1\w*\b'
    var4 = 0
    for var5 in var1:
        var6 = "".join(var5.strip().split("\n"))
        var7 = re.finditer(var3,var6,re.I)
        for var8 in var7:
            var4 += 1
    return var4
    
    """MODIFICARE IL CONTENUTO DI QUESTA FUNZIONE PER SVOLGERE L'ESERCIZIO"""
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ["file2_1.txt"] , 1)
    counter_test_positivi += tester_fun(Ex3, ["file2_2.txt"] , 2)
    counter_test_positivi += tester_fun(Ex3, ["file2_3.txt"] , 3)
    counter_test_positivi += tester_fun(Ex3, ["file2_4.txt"] , 4)
    counter_test_positivi += tester_fun(Ex3, ["file2_5.txt"] , 5)

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
