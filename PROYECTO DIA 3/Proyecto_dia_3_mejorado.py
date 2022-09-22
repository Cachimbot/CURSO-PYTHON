
texto = input("Ingrese un texto: ")
letras = []
texto = texto.lower()
letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())
print("\n")

#Codigo de la 1era tarea contar las letras que digitamos en el texto cuantas veces aparece
print("                    CANTIDAD DE LETRAS                    ")
print("----------------------------------------------------------")
print(f"La letra '{letras[0]}' aparece {texto.count(letras[0])} veces")
print(f"La letra '{letras[1]}' aparece {texto.count(letras[1])} veces")
print(f"La letra '{letras[2]}' aparece {texto.count(letras[2])} veces")
print("\n")

#codigo de la 2da tarea: contar las palabras que ingrese en el texto
print("                   CANTIDAD DE PALABRAS                   ")
print("----------------------------------------------------------")
palabra_texto = texto.split()
print(f"La cantidad de palabras que contiene el texto es: {len(palabra_texto)}")
print("\n")

#codigo de la 3era tarea: cuál es la primera y última letra del texto
print("                  LETRAS DE INICIO Y FIN                  ")
print("----------------------------------------------------------")
lista_primera_palabra = list(palabra_texto[0])
lista_ultima_palabra = list(palabra_texto[int(len(palabra_texto)-1)])
contador_ultima_palabra = len(lista_ultima_palabra) - 1
print(f"La primera letra del texto introducido es: {lista_primera_palabra[0]}")
print(f"La ultima letra del texto introducido es: {lista_ultima_palabra[contador_ultima_palabra]}")
print("\n")

#codigo de la 4ta tarea: palabras del texto en orden inverso
print("                      TEXTO INVERTIDO                     ")
print("----------------------------------------------------------")
palabra_texto.reverse()
texto_invertido = ' '.join(palabra_texto)
print(f"El texto introducido en orden inverso es: {texto_invertido}")
print("\n")

#codigo de la 5ta tarea: si aparece python en el texto introducido
print("                BUSCANDO LA PALABRA PYTHON                ")
print("----------------------------------------------------------")
buscar_python = "python" in texto
dic = {True:'si', False:'no'}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto ")
print()

