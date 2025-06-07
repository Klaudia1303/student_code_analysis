def Ex5(file):
    regex = [r"\b[A-Z]{2}\d{3}[A-Z]{2}\b", r"\b[A-Z]{2}\d{5}\b", r"\b([A-Z0-9]){5}\b", r"\b([A-Z0-9]){6}\b"]
    mezzo = ["auto", "moto", "ciclomotore1", "ciclomotore2"]
    d = {}

    for x in mezzo:
        d[x] = 0
    d["errata"] = 0

    f = open(file, "r", encoding="UTF-8")
    riga = f.readline()

    while len(riga) > 0:
        for x in range(len(mezzo)):
            if re.search(regex[x], riga):
                d[mezzo[x]] = d[mezzo[x]] + 1
                break
            if x == len(mezzo) - 1:
                d["errata"] += 1
        riga = f.readline()

    f.close()

    return d


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
