#Escribir un programa que corra un bucle infinito leyendo e imprimiento las teclas y sólo terminará cuando se presione la tecla ↑ indicada como UP

from readchar import readkey, key

while True: #inicio de bluqie infinito
  print("presiona cualquier tecla")
  la_letra = readkey() #Aquí leo la tecla
  print("presionaste la letra ", la_letra)
  
    
  if la_letra == key.UP:
    print("si presionas la tecla hacia arriba el juego se detiene")
    break
  


