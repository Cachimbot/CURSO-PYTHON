#creacion del archivo de texto
archivo = open('archivo.txt', 'w')

#Escribir en el archivo
archivo = open('archivo.txt', 'a')
archivo.write("Sere un Data Scientist\n")
archivo.write("Viajare por el mundo :) \n")
archivo.close()