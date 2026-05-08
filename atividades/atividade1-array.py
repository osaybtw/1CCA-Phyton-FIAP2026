duplas = ["Bob", "Luis", "Ana", "Jô"]

for i in range(len(duplas)):
    for j in range(i+1, len(duplas)):
        print(duplas[i], duplas[j])