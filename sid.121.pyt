n = int(input("Hur många rader ska multiplikationstabellen ha? "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i * j}", end="\t")
        print()