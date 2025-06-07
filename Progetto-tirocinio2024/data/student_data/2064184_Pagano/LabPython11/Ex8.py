def Ex8(file):
    months = {"A": "01", "B": "02", "C": "03", "D": "04", "E": "05", "H": "06", "L": "07", "M": "08", "P": "09", "R": "10", "S": "11", "T": "12"}
    m31 = {"A", "C", "E", "L", "M", "R", "T"}
    m30 = {"D", "H", "P", "S"}
    
    ris = []
    with open(file, encoding="UTF-8") as f:
        pattern = r"[A-Z]{3}[ ]?[A-Z]{3}[ ]?(\d{2})([A-Z])(\d{2})[ ]?[A-Z]\d{3}[A-Z]"
        # 1: anno
        # 2: mese
        # 3: giorno

        for cf in f.readlines():
            m = re.match(pattern, cf)
            if m:
                year = int(m.group(1))
                year = year+1900 if year>20 else year+2000
                
                month = m.group(2)
                if month not in months:
                    ris.append("Mese errato")
                    continue
                
                day = int(m.group(3))
                day = day-40 if day>40 else day
                if (month in m31 and day > 31) or (month in m30 and day > 30) or (month == "B" and day > 28):
                    ris.append("Giorno errato")
                    continue
                day = "0"+str(day) if day < 10 else str(day)

                ris.append(day + "/" + months[month] + "/" + str(year))
            else:
                ris.append("Codice errato")

    return ris
    
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
