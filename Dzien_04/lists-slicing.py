"""
"Krojenie" list
"""
#         0   1   2   3   4   5   6   7  8    9
list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#       -10  -9  -8  -7  -6  -5  -4  -3  -2  -1
#
print(list1[8], list1[-2])

# Zasada 3xS
# [ START : STOP : STEP ]
# 30, 40, 50, 60, 70
print(list1[2:7:1])

# 40 - 100
#print(list1[3:10])
print(list1[3:])

# 10-30
#print(list1[0:3])
print(list1[:3])

# co drugi element listy
print(list1[::2])

# odwrócona lista
print(list1[::-1])

list1.reverse() # funkcja zmiany listy na odwrocona
print(list1)

# sortowanie
list2 = [9, -10, 11, -100, 20, 0, 0.1, -1234]
list2.sort(reverse=True) # od najwiekszej do najmniejszej
print(list2)

#sortowanie krotki z funkcja
def sort_tuple(x):
    return x[1]
lista3 = [ ("Marek",2), ("Julian", 4), ("Zenek", 1) ]
lista3.sort(key=sort_tuple)
print(lista3)