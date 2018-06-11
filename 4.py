#Crear un programa que lea por teclado una cadena y un carácter, y reemplace todos los dígitos en la cadena por el carácter
cadena=str(input("Introduce una cadena: "))
caracter=str(input("Introduce un caracter: "))
for i in cadena:
	cadena=cadena.replace(i, caracter)
print(cadena)