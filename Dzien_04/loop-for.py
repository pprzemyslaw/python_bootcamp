"""

Petla for

"""
list1 = [9, -10, 11, -100, 20, 0, 0.1, -1234]
list_res = []
for i in list1:
    if i > 0:
        list_res.append(i)
print(list_res)


list_res = []
for ix, value in enumerate(list1,1): #enumerate(list1, odjakiejliczby) # mozna numerowac od dowolnej liczby
    if value == -10:
        continue

    if value == 0.1:
        break
    if value > 0:
        list_res.append(value)
        print(f"wartosc {value} jest na pozycji {ix}")

print(list_res)