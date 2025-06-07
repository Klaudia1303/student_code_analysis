def Ex7(file):
    f = open(file)
    r = f.readlines()
    diz = {"invalidi":0, "domestici":0, "altri":0}
    for i in r:
        pattern = r"^(\d\d?\d?)\D(\d\d?\d?)\D(\d\d?\d?)\D(\d\d?\d?)$"
        match = re.search(pattern, i)
        if match and 0 <= int(match.group(3)) <= 255 and 0 <= int(match.group(4)) <= 255 and match.group(1) == "192" and match.group(2) == "168":
            diz["domestici"] += 1
        elif match and 0 <= int(match.group(3)) <= 255 and 0 <= int(match.group(4)) <= 255 and 0 <= int(match.group(1)) <= 255 and 0 <= int(match.group(2)) <= 255:
            diz["altri"] += 1
        else:
            diz["invalidi"] += 1
    return diz
                
    
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
