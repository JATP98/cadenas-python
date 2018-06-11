#Crear un programa que lea por teclado una cadena y un carácter, e inserte el carácter entre cada letra de la cadena.
cadena=str(input("Introduce una cadena: "))
caracter=str(input("Introduce un caracter: "))
print("Así quedaria la cadena con el caracter unido.",caracter.join(cadena))