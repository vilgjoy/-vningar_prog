antal_stationer = int(input("Hur många mätstationer? "))

temperaturer = []
for i in range(1, antal_stationer + 1):
    temp = float(input(f"Ange temperaturen vid mätstation {i}: "))
    temperaturer.append(temp)

medelvärde = sum(temperaturer) / antal_stationer
print(f"\nTemperaturer högre än medelvärdet:")
for i, temp in enumerate(temperaturer, start=1):
    if temp > medelvärde:
        print(f"Mätstation {i}: {temp:.2f} °C")