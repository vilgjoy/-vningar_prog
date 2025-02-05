# 6.1

n = int(input("Hur många tal vill du ha i talföljden? "))

a = 2 # första talet
k = 3 # konstanten

talföljd = []

for i in range(n):
    talföljd.append(a * k**i)

print("Den geometriska talföljden är: ", talföljd)