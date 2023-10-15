# Para esta sección del proyecto integrador necesitaremos aprender a manipular la terminal:
# Iniciar con un número en 0, leer la tecla `n` del teclado en un bucle, por cada presionada, 
#borrar la terminal y e imprimir el nuevo número hasta el número 50.
#La operación de borrar la terminal e imprimir el nuevo número debe estar en su propia función.
# Para borrar la terminal antes de imprimir nuevo contenido usar la instrucción: 
# os.system('cls' if os.name=='nt' else 'clear'), para esto se debe importar la librería os

from readchar import readkey, key
import os
def borra_pantalla():
  os.system('cls' if os.name=='nt' else 'clear')

def imprimir_numero(contador):
  print(contador)
numero = 0
print ("Hola, presiona la tecla n para iniciar")
while True: #inicio de bucle infinito
  la_letra = readkey() #Aquí leo la tecla
  if la_letra == "n":
    borra_pantalla()
    imprimir_numero (numero)
    if numero == 50:
      print ("llegaste hasta 50 el juego terminó")
      break
    numero = numero + 1
    
    