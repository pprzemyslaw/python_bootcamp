miastoa = input("Miasto A:")
miastob = input("Miasto B:")
dystans = int(input(f"Dystans {miastoa} - {miastob} :"))
cena = float(input("Cena paliwa:"))
spalanie = float(input("Spalanie na 100km:"))

oblicz = (dystans/100)*spalanie*cena

print(f"Koszt przejazdu {miastoa} - {miastob} to {oblicz}")
