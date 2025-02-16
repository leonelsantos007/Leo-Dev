# Programa que lê uma distância em metros e mostra os valores relativos em outras medidas

# Solicitando a distância em metros
metros = float(input("Digite uma distância em metros"))

# Mostrando as distâncias relativas em outras medidas

kilometro = metros/1000
hectometro = metros/100
decametro = metros/10
decimetro = metros*10
centimetro = metros*100
milimetro = metros*1000

print(f"A distância de {metros} metros corresponde a: ")
print(f"{kilometro}Km")
print(f"{hectometro}Hm")
print(f"{decametro}Dam")
print(f"{decimetro}dm")
print(f"{centimetro}cm")
print(f"{milimetro}mm")