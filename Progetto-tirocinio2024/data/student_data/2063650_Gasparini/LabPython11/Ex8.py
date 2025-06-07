import re

def Ex8(file):
    res = []
    with open(file, encoding="UTF-8") as f:
        for line in f:
            line = line.rstrip()
            match = re.fullmatch(r'[A-Z]{3}\s*[A-Z]{3}\s*([0-9]{2})\s*([A-Z])\s*([0-9]{2})\s*[A-Z]\s*[0-9]{3}\s*[A-Z]', line)
            if not match:
                res.append("Codice errato")
                continue

            year = int(match.group(1))
            if year <= 20:
                year += 2000
            else:
                year += 1900

            months = {
                "A": 1,
                "B": 2,
                "C": 3,
                "D": 4,
                "E": 5,
                "H": 6,
                "L": 7,
                "M": 8,
                "P": 9,
                "R": 10,
                "S": 11,
                "T": 12,
            }
            month = match.group(2)
            if month not in months:
                res.append("Mese errato")
                continue
            month = months[month]
        
            day = int(match.group(3))
            if day >= 40:
                day -= 40
            max_days = [
                31,
                28,
                31,
                30,
                31,
                30,
                31,
                31,
                30,
                31,
                30,
                31,
            ]
            if day == 0 or day >= max_days[month - 1]:
                res.append("Giorno errato")
                continue
            
            s = ""
            if day < 10:
                s += "0"
            s += str(day) + "/"
            if month < 10:
                s += "0"
            s += str(month) + "/" + str(year)
            res.append(s)
    return res
    
###############################################################################

if __name__ == '__main__':
    from tester import tester_fun
    import re

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex8, ["codici1.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici2.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato'])
    counter_test_positivi += tester_fun(Ex8, ["codici3.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921'])
    counter_test_positivi += tester_fun(Ex8, ["codici4.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931'])
    counter_test_positivi += tester_fun(Ex8, ["codici5.txt"] , ['12/03/1971', 'Codice errato', '15/04/2011', 'Mese errato', 'Giorno errato', 'Giorno errato', 'Codice errato', 'Giorno errato', '01/11/1921', '01/11/1931', 'Codice errato', 'Giorno errato'])

    print('La funzione',Ex8.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
