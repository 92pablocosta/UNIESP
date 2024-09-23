carros = ["GM", "FIAT", "Volkswagen", "Ford",
          "Honda", "Toyota", "Gurgel", "Dodge"]

#Inserindo objetos nas respectivas posições na lista
carros.insert(3, "Hyunday")
carros.insert(4, "BMW")
carros.insert(5, "Nissan")

carros[0] = "Chevrolet"

carros.remove("Gurgel")

print(carros)
print(sorted(carros))
