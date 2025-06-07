import re

def Ex5(file):
    with open(file, encoding="UTF-8") as f:
        res = {
            "auto": 0,
            "moto": 0,
            "ciclomotore1": 0,
            "ciclomotore2": 0,
            "errata": 0,
        };
        for line in f:
            kind = "errata"
            line = line.rstrip()
            if re.fullmatch(r'[A-Z]{2}[0-9]{3}[A-Z]{2}', line):
                kind = "auto"
            elif re.fullmatch(r'[A-Z]{2}[0-9]{5}', line):
                kind = "moto"
            elif re.fullmatch(r'[A-Z0-9]{6}', line):
                kind = "ciclomotore2"
            elif re.fullmatch(r'[A-Z0-9]{5}', line):
                kind = "ciclomotore1"
            res[kind] += 1
        return res
      
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex5, ["targhe1.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 1})
    counter_test_positivi += tester_fun(Ex5, ["targhe2.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 2})
    counter_test_positivi += tester_fun(Ex5, ["targhe3.txt"] , {'auto': 3, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 3})
    counter_test_positivi += tester_fun(Ex5, ["targhe4.txt"] , {'auto': 3, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 4})
    counter_test_positivi += tester_fun(Ex5, ["targhe5.txt"] , {'auto': 2, 'moto': 1, 'ciclomotore1': 1, 'ciclomotore2': 1, 'errata': 5})
    
    print('La funzione',Ex5.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
