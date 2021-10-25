"""

Napisać metodę do sprawdzania czy podana liczba przez użytkownika jest
liczbą pierwszą (https://pl.wikipedia.org/wiki/Liczba_pierwsza).
Wartość ma być pobierana z klawiatury.
Opis algorytmu/ów można znaleźć na ->
https://eduinf.waw.pl/inf/alg/001_search/0010.php

"""

number = int(input("Podaj liczbe:"))
result = True
if number == 2:
    result = True
elif number % 2 == 0 or number <= 1:
    result = False
else:
    pierw = int(number**0.5) + 1
    for zm in range(3, pierw, 2):
            if number % zm == 0:
                result = False
if result:
    print(f"Liczba {number} jest liczba pierwsza")
else:
    print(f"Liczba {number} NIE jest liczba pierwsza")