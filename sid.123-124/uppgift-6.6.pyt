matris = []
n = int(input("Ange storleken på matrisen (n x n): "))

print("Mata in matrisen rad för rad, med siffror erperade med mellanslag:")
for _ in range(n):
    rad = list(map(int, input().split()))
    if len(rad) != n:
        print("Fel: varje rad måste ha exakt", n, "element")
        exit()
    matris.append(rad)

symmetrisk = True
for i in range(n):
    for j in range(n):
        if matris[i][j] != matris[j][i]:
            symmetrisk = False
            break
    if not symmetrisk:
        break


if symmetrisk:
    print("Matrisen är symmetrisk")
else:
    print("Matrisen är inte symmetrisk")