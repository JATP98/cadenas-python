#Crear un programa que lea por teclado una cadena, y muestre la siguiente información

cadena=str(input("Introduce una cadena: "))
print ("Las dos primeras letras de la cadena son: ",cadena[0:2])
print ("Los 3 ultimos caracteres son ",cadena[-3:])
print ("La cadena de dos en dos quedaria : ",cadena[::2])
print ("La cadena al reves quedaria: ",cadena[::-1])
print ("La cadena al derecho y al reves quedaria: ",cadena+cadena[::-1])