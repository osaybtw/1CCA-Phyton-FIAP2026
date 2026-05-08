lista_bebidas = ["Guarana", "Coca-Cola", "Pepsi"]

print(lista_bebidas[1])

lista_bebidas.append("Fanta")
print(lista_bebidas[-1])
print()

for i in range(len(lista_bebidas)):
    print(lista_bebidas[i])

print()

for bebida in lista_bebidas:
    print (bebida)

print()

print("Oi fulano!")

msg = "Oi fulano!"

for i in range(len(msg)):
    print(msg[i])