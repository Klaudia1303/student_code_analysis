def Ex7(file):
    import re
    f = open(file,encoding="UTF-8")
    l = []
    for e in f:
        l.append(e.strip().split(','))
        
    f.close()
    d = {"invalidi":0,"domestici":0,"altri":0}
    p1 = r"192\.168\.(2[0-5][0-5]|[0-1][0-9][0-9]|[0-9][0-9]|[0-9])\.(2[0-5][0-5]|[0-1][0-9][0-9]|[0-9][0-9]|[0-9])"
    p2 = r"(2[0-5][0-5]|[0-1][0-9][0-9]|[0-9][0-9]|[0-9])\.(2[0-5][0-5]|[0-1][0-9][0-9]|[0-9][0-9]|[0-9])\.(2[0-5][0-5]|[0-1][0-9][0-9]|[0-9][0-9]|[0-9])\.(2[0-5][0-5]|[0-1][0-9][0-9]|[0-9][0-9]|[0-9])"
    for i in range(len(l)):
        for j in range(len(l[i])):
            if re.match(p1,l[i][j]) and len(re.match(p1,l[i][j]).group()) == len(l[i][j]):
                d["domestici"]+=1
                print(l[i][j])
            else:
                if re.match(p2,l[i][j]) and len(re.match(p2,l[i][j]).group()) == len(l[i][j]):
                    d["altri"]+=1
                else:
                    d["invalidi"]+=1
    return d
        
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex7, ["ip1.txt"] , {'invalidi': 0, 'domestici': 0, 'altri': 5})
    counter_test_positivi += tester_fun(Ex7, ["ip2.txt"] , {'invalidi': 2, 'domestici': 1, 'altri': 2})
    counter_test_positivi += tester_fun(Ex7, ["ip3.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex7, ["ip4.txt"] , {'invalidi': 1, 'domestici': 1, 'altri': 3})
    counter_test_positivi += tester_fun(Ex7, ["ip5.txt"] , {'invalidi': 3, 'domestici': 0, 'altri': 2})
    
    print('La funzione',Ex7.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
