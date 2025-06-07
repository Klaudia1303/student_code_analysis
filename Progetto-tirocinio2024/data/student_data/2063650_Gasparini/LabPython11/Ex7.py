def Ex7(file):
    with open(file, encoding="UTF-8") as f:
        res = {
            "invalidi": 0,
            "domestici": 0,
            "altri": 0,
        }
        for line in f:
            kind = "invalidi"
            match = re.fullmatch(r'([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})', line.rstrip())
            if match:
                invalid = False
                for i in range(1, 5):
                    component = int(match.group(i))
                    if component > 255:
                        invalid = True
                if not invalid:
                    if match.group(1) == "192" and match.group(2) == "168":
                        kind = "domestici"
                    else:
                        kind = "altri"
            res[kind] += 1
        return res
    
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
