"""
Listy w Pythonie
"""

list1 = list() # pusta lista
list1 = [] # pusta lista
list1 = [1, "ala ma kota", True, 999.99, (1,), ["A", "B"], None] # deklaracja listy # None - synonim pustej wartosci
print(list1)

list1.append(2)
print(list1)
#dodaj liste na koniec listy
list1.extend([9,8,7, 1])
print(list1)

#wstawienie do srodka listy
list1.insert(1, 6789)
print(list1)

#usuwanie z listy
list1.remove("ala ma kota")
print(list1)

list1.remove(1)
print(list1)

#detekcja liczby elementów o podanej wartosci w liscie
print(list1.count(1))

#przed usunieciem, sprawdzam czy sa wartosci do usuniecia
if list1.count("Alka ma kota"):
    list1.remove("Alka ma kota")

if "Alka ma kota" in list1:
    list1.remove("Alka ma kota")

# ile jest elementów #uzycie index
print(f"Liczba elementów = {len(list1)}")
print (f"Pozycja liczby 9999.99 to {list1.index(999.99)}")

#usuwanie 1-go elementu w liscie
del(list1[0])
# modyfikacja wartosci elementu listy
print(list1)
list1[0] = "ABC"


list1.pop(2)
print(f"usuniecie drugiego obiekt {list1}" )

# kopiowanie list, # = daje referencje nie jest to nowa zmienna, listy nalezy kopiowac poprz funkcje copy()
list2 = list1.copy()
list2[0] = "XYZ"
print(f"list1 = {list1}") , print(f"list2 = {list2}")
print(f"list1: {id(list1)}") # print - id w pamieci obiektu
print(f"list2: {id(list2)}") # print - id w pamieci obiektu
