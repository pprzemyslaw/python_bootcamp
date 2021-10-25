"""
Proszę napisać program wyliczający opłatę za pobyt w hotelu.
Użytkownik podaje swój wiek i ile nocy spędzi w hotelu, a program
wylicza, ile trzeba zapłacić. Zasady są takie:
- nieletni (poniżej 18 roku życia) płacą 100 zł za noc
- dorośli (ci, którzy mają przynajmniej 18 lat ale mniej niż 65 lat) płacą:
    - 200 zł za noc, jeśli nocują jedną noc
    - 180 zł za noc, jeśli nocują przynajmniej dwie ale mniej niż pięć nocy
    - 150 zł za noc, jeśli nocują pięć lub więcej nocy
- emeryci (ci, którzy mają przynajmniej 65 lat), płacą jak dorośli,
ale z 10% zniżki
Przykładowo: jeśli użytkownik ma 70 lat i spędzi w hotelu dziesięć
nocy, zapłaci 150 zł za noc z 10% zniżki, czyli 150-15 zł za noc,
czyli 135 zł za noc, czyli 1350 zł.

"""



"""
Version 1.
wiek = int(input("Podaj swój wiek:"))
liczba_nocy = int(input("Podaj liczbe nocy w hotelu:"))

if wiek < 18:
    cena_noc = 100
elif wiek >= 65:
    if liczba_nocy == 1:
        cena_noc = 200 - (200 * 10)/100
    elif liczba_nocy >= 5:
        cena_noc = 150 - (150 * 10)/100
    else:
        cena_noc = 180 - (180 * 10)/100
else :
    if liczba_nocy == 1:
        cena_noc = 200
    elif liczba_nocy >= 5:
        cena_noc = 150
    else:
        cena_noc = 180

do_zaplaty = cena_noc* liczba_nocy
print(f"Cena do zapłaty: {do_zaplaty} zł.")
"""
#Version 2
wiek = int(input("Podaj swój wiek:"))
liczba_nocy = int(input("Podaj liczbe nocy w hotelu:"))

if liczba_nocy == 1:
    cena_noc = 200
elif liczba_nocy >= 5:
    cena_noc = 150
else:
    cena_noc = 180

if wiek < 18:
    cena_noc = 100
elif wiek >= 65:
    cena_noc = cena_noc - (cena_noc * 10)/100

do_zaplaty = cena_noc* liczba_nocy
print(f"Cena do zapłaty: {do_zaplaty} zł.")


