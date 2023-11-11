from pynput import keyboard as bk
import os
import random

class Juego:
    #(Código de la clase Juego actual)

class JuegoArchivo(Juego):
    def __init__(self, path_a_mapas):
        super().__init__()
        self.path_a_mapas = path_a_mapas
        self.laberinto = self.cargar_mapa_aleatorio()

    def cargar_mapa_aleatorio(self):
        archivos_mapa = os.listdir(self.path_a_mapas)
        nombre_archivo = random.choice(archivos_mapa)
        path_completo = os.path.join(self.path_a_mapas, nombre_archivo)

        # Leer datos del archivo de mapa
        with open(path_completo, 'r') as archivo:
            contenido = archivo.read()

        return contenido.strip()

    def leer_mapa(self):
        # Obtener el nombre del archivo actual
        nombre_archivo = self.laberinto.split('\n')[0].strip()

        # Componer la ruta completa al archivo
        path_completo = os.path.join(self.path_a_mapas, nombre_archivo)

        # Leer el contenido del archivo de mapa
        with open(path_completo, 'r') as archivo:
            contenido = archivo.read()

        return contenido.strip()

# Resto del código
# ... (El código restante debe modificarse para utilizar la nueva clase JuegoArchivo)
