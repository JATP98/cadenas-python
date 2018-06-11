#Crear un programa que lea por teclado una cadena y un carácter, e inserte el caracter cada 3 dígitos en la cadena. Ej. 2552552550 y . debería devolver 255.255.255.0
cadena=str(input("Introduce una cadena: "))
caracter=str(input("Introduce un caracter: "))
contador=0
cadena2=""
for i in cadena:
	contador=contador+1
	cadena2=cadena2+i
	if contador%3==0:
		cadena2=cadena2+caracter
print(cadena2)