import time
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
RED = '\033[31m'
GREEN = '\033[32m'
print("\nHola mundo ___ Iniciando")
print("\033[34m Este texto es azul \033[39m")

print(BLUE+"No te olvides de poner el RESET")
print("o seguira pintando del mismo color"+RESET)

#x = int(input("numero de filas :"))
#y=0
#while y<= x
#	z=0 
	#while z<y:
##		print ("+", end = "")
#			z=z+1
#	print("")
#	y=y+1

#z = input("\nIngrese la palabra:")
#x = int(input("numero de veces"))
#y = 0
#while y>x:
# print(z)
#y= y + 1




#siempre acuerdate importar la libreria
import random
puntaje= random.randint(0,11)

print("Bienvenido a mi trivia sobre computacion")
print("Pondremos a prueba tus conocimientos")
print("Comenzaras con :", puntaje,"puntos\n")


nombre = input ("Ingresa tu nombre: ") 

print ("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")


print ("1) ¿Quién fue el creador de windows?")
print ("a) Linus Torvalds")
print ("b) Bill Gates")
print ("c) Mark Zuckerberg")
print ("d) Dennis Ritchie")
respuesta_1 = input("\nTu respuesta: ")

while respuesta_1 not in ("a", "b", "c", "d"):
  respuesta_1 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_1 == "b":
  puntaje += 10
  print ("Muy bien", nombre, "!")
else:
  puntaje -= 2
  print ("Incorrecto", nombre, "!")


print(nombre, "Llevas", puntaje, "puntos")

print ("\n 2) ¿Cual de estos lenguajes de programación es de más bajo nivel?")
print ("a) Python")
print ("b) Java")
print ("c) PHP")
print ("d) Assembly")

respuesta_2 = input("\nTu respuesta: ")

while respuesta_2 not in ("a", "b", "c", "d"):
  respuesta_2 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

#cierto o falso
if respuesta_2 == "a":
  puntaje -= 1
  print ("Incorrecto!", nombre, "Python es un lenguaje de alto nivel")
elif respuesta_2 == "b":
  puntaje -= 2
  print ("Incorrecto!", nombre, "Java es un lenguaje de alto nivel")
elif respuesta_2 == "c":
  puntaje -= 3
  print ("Incorrecto!", nombre, "PHP es un lenguaje de alto nivel")
else:
  puntaje += 10
  print ("Muy bien", nombre, "!")

print(nombre, "Llevas", puntaje, "puntos")


print ("\n 3) ¿En que lenguaje se progamo Minecraft?")
print ("a) Python")
print ("b) Java")
print ("c) PHP")
print ("d) Assembly")

#Incrementando
respuesta_3 = input(BLUE+"\nTu respuesta: "+RESET)

while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

if respuesta_3 == "a":
  print ("Totalmente incorrecto! ...")
  puntaje = puntaje / 2
elif respuesta_3 == "d":
  print ("...")
  puntaje = puntaje + 5
elif respuesta_3 == "c":
  print ("Incorrecto! ...")
  puntaje = puntaje - 5
else:
  print ("Correcto! ...")
  puntaje = puntaje * 2


print (MAGENTA+"Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)
######
print(WHITE+"\nHola William tu puedes\n"+RESET)

print(BLUE+"\nHola William para que te diviertas\n"+RESET)

time.sleep(2)
#print(9%2)
print ("\n 3) ¿Quien es mas fuerte ?")
print ("a) Goku")
print ("b) Superman")
print ("c) Holk)")
print ("d) Vegeta")

#Incrementando
respuesta_3 = input(BLUE+"\nTu respuesta: "+RESET)

if respuesta_3 == "b":
  print ("Creo! ...")
  puntaje = puntaje /2
elif respuesta_3 == "d":
  print ("Tu crees..")
  puntaje = puntaje + 5
elif respuesta_3 == "c":
  print ("Incorrecto! ...")
  puntaje = puntaje - 10
else:
  print ("Correcto! ...")
  puntaje = puntaje * 100

print (MAGENTA+"Gracias", nombre, "por jugar mi trivia, alcanzaste", puntaje, "puntos"+RESET)


  
num1 = int(input("\nIngrese un numero:"))
num2 = int(input("Ingrese otro numero:"))
op   = input("Ingrese la operacion:")
if op =="+":
	print("Resultado", num1+num2)
elif op=="-":
	print("Resultado", num1-num2)
elif op=="*":
	print("Resultado", num1*num2)
elif op=="/":
	print("Resultado", num1/num2)

else:
	print(CYAN+"Operador invalido. Por favor ingrese +,-,* o /. \n"+RESET)



time.sleep(2)

numero1 = 10 # int
numero2 = 30 # int
numero3 = 5.5 # float

print(RED+"Variables numéricas: Integer y Float"+RESET)
print("numero1:",numero1, "numero2:", numero2, "numero3:", numero3)
time.sleep(2)

x=0 
while x<=10:
	if x==3:
		print("BOOM!")
	else:
		print(x)
	x=x+1

x= 0
while x>10:
  print(x)
x=x+1