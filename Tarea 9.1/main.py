
datosEntrada = input("Introduce paises separados por coma:\n ")


paises = []
for pais in datosEntrada.split(","):
    paises.append(pais)

print(",".join(sorted(list(set(paises)))))

