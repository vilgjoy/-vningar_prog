# 4.4

n = int(input("Ange antal rader: "))

# if n < 1 or n > 9:
#     print("Lägg till ett nummer mellan 1 och 9 som inte är ett decimaltal")
# else:
for i in range(1, n+1): # går från 1 till n och styr raderna
    for j in range(1, n+1): # går också från 1 till n och beräknar produkterna
        print(f"{i*j:2}", end="  ") #ser snyggare ut
    print() # ny rad efter varje rad