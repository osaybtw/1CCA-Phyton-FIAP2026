duplas = ["Bob", "Luis", "Ana", "Jô"]

for i in range(len(duplas)):
    for j in range(i+1, len(duplas)):
        print(duplas[i], duplas[j])
print()

musicas = [
    ["Hero", "Mili"],
    ["Color Your Night", "Lotus Juice"],
    ["Hyervetilation", "Radwimps"]
]

for song in musicas:
    for info in song:
        print(info)