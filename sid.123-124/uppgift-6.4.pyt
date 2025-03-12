värden = []
antal = int(input("Hur många värden vill du mata in? "))

for _ in range(antal):
    värde = float(input("Ange ett värde: "))
    värden.append(värde)

värden.sort()

längd = len(värden)
if längd % 2 == 1:
    median = värden[längd // 2]
else:
    mitten1 = värden[längd // 2 - 1]
    mitten2 = värden[längd // 2]
    median = (mitten1 + mitten2) / 2

print(f"Medianen är: {median}")