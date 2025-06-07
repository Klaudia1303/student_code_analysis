def Ex8(file):
    ret = []

    encoded_month_to_month = {
        'A': '01', 'B': '02',
        'C': '03', 'D': '04',
        'E': '05', 'H': '06',
        'L': '07', 'M': '08',
        'P': '09', 'R': '10',
        'S': '11', 'T': '12'
    }

    month_days = {
        'A': 31, 'B': 28,
        'C': 31, 'D': 30,
        'E': 31, 'H': 30,
        'L': 31, 'M': 31,
        'P': 30, 'R': 31,
        'S': 30, 'T': 31
    }

    with open(file, 'r', encoding='UTF-8') as f:
        for line in f.readlines():
            line = line.strip()

            pattern = '^[A-Z]{3}\W*[A-Z]{3}\W*(\d{2})([A-Z])(\d{2})\W*[A-Z]{1}\d{3}[A-Z]{1}$'

            if re.match(pattern, line) is None:
                ret.append('Codice errato')
                continue
            else:
                matches = re.search(pattern, line, re.IGNORECASE)
                (encoded_year, encoded_month, encoded_day) = matches.groups()

                if encoded_month not in encoded_month_to_month:
                    ret.append('Mese errato')
                    continue

                year = f'20{encoded_year}' if int(encoded_year) <= 20 else f'19{encoded_year}'
                month = encoded_month_to_month[encoded_month.upper()]
                day = int(encoded_day) - 40 if int(encoded_day) > 40 else int(encoded_day)

                if day > month_days[encoded_month]:
                    ret.append('Giorno errato')
                    continue

                ret.append(f'{day:>02}/{month:>02}/{year}')

    return ret
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
