"""
Petla while

"""
counter = 10
while counter > 0:
    print(f"counter={counter}")
    counter -= 1 # counter = counter -1
    if counter == 5:
        break
print("juz po petli...")


# Petla while "nieskonczona" , prosimu usera o podanie liczby ktore jest >= 100 lub <10
while True: #petla nieskonczona
    value = int(input("Podaj liczbe >= 100 lub < 10:"))
    if value >= 100 or value < 10:
        print(f"Podales: {value}")
        break



