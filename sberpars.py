from bs4 import BeautifulSoup
from pprint import pprint
from datetime import datetime


def normal(list_item):
    list_item = iter(list_item)
    l = []
    while True:
        try:
            dat = next(list_item)
            dat = datetime.strptime(dat, '%d.%m.%Y')
            sum = next(list_item)
            sum = sum.replace('\xa0', '')
            if sum.startswith('+'):
                prih = True
            else:
                prih = False
            sum = sum.replace('+', '').replace(' RUB', '').replace(' ', '').replace(',', '.')
            opis = next(list_item)
            l.append((dat, float(sum), opis, prih))
        except StopIteration:
            break
    l = sorted(l)
    l = [(item[0].strftime('%d.%m.%Y'), item[1], item[2], item[3]) for item in l]
    return l

def seter(list_norm):
    d = {}
    for line in list_norm:
        if d.get(line[0]):
            if d[line[0]].get(line[2]):
                d[line[0]][line[2]][0] += line[1]
            else:
                d[line[0]][line[2]] = [line[1], line[3]]
        else:
            d[line[0]] = {line[2]: [line[1], line[3]]}
    return d


# don't run on import
if __name__ == "__main__":
    with open('26012020093451.html', encoding='utf-8') as resp:
        html = resp.read() # считываем содержимое
    s = str(html).replace('&#034;', '"').replace('\t', ' ')
    soup = BeautifulSoup(s, 'html.parser') # делаем суп
    table = soup.find('table', attrs={'id': 'rrr'})
    for tr in table.find_all('tbody'):
        td = [td.text for td in tr.find_all('td')]
    td = normal(td)
    pprint(td)
    slov = seter(td)
    pprint(slov)