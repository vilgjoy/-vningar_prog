


antal_elever = int(input("Hur många elever? "))

elever = {}

for _ in range(antal_elever):
    namn = input("Ange elevens namn: ")
    resultat = list(map(int, input("Ange elevens provresultat, separerade med mellanslag: ").split()))
    elever[namn] = resultat


print("\nSammanställning av elevernas resultat:")
for namn, resultat in elever.items():
    medelvärde = sum(resultat) / len(resultat)
    print(f"{namn}: Resultat: {resultat}, Medelvärde: {medelvärde:.2f}")