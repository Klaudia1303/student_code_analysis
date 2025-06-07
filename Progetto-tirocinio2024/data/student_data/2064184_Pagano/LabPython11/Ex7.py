def Ex7(file):
    d = {"invalidi": 0, "domestici": 0, "altri": 0}
    with open(file, encoding="UTF-8") as f:
        patternDomestici = r"192\.168\.(\d{1,3})\.(\d{1,3})$"
        pattern = r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

        for ip in f.readlines():
            match1 = re.match(patternDomestici, ip)
            if match1:
                if 0 <= int(match1.group(1)) < 256 and 0 <= int(match1.group(2)) < 256:
                    d["domestici"] += 1
                else:
                    d["invalidi"] += 1
            else:
                match2 = re.match(pattern, ip)
                if match2:
                    if 0 <= int(match2.group(1)) < 256 and 0 <= int(match2.group(2)) < 256 and 0 <= int(match2.group(3)) < 256 and 0 <= int(match2.group(4)) < 256:
                        d["altri"] += 1
                    else:
                        d["invalidi"] += 1
                else:
                    d["invalidi"] += 1
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
