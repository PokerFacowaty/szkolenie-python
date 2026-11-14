"""
- W pliku znajdziesz linijkę, z której w podobny sposób co nasze IP chcemy wyciągnąć wszystkie ciągi znaków, które składają się z
    - Jednej cyfry
    - Następującej zaraz po niej jednej litery (od a do z, znaki łacińskie)
    - Następującej zaraz po niej jednej cyfry
- Przygotuj odpowiedni regex i wypisz listę wszystkich ciągów spełniających warunek
    - Pytanie pomocnicze: jakim znakiem w wyrażeniu regularnym oznaczymy cyfrę?
    - Pytanie pomocnicze: jak możemy oznaczyć zakres od a do z?
    - Protip: odpowiedzi na obydwa te pytania można znaleźć w "Quick reference" w prawym dolnym rogu regex101
- Powinnaś przy okazji pobawić się regex101 wpisując tam jakieś głupoty i sprawdzając, co się stanie
    - Nie zapomnij ustawić trybu na Python!
- Czas: 10 minut
"""
import re

text = "123 abc cba 1ab aa1 c2b c2z 7a8 0a2"
pattern = r""

found = re.findall(pattern, text)
print(found)
