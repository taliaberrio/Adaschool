import os
from readchar import readkey, key
from pydantic import BaseModel
import random


class NotFileError(Exception):
    pass


class Juego(BaseModel):
    mapa: list[list[str]] | None
    laberinto: str | None
    posicion_inicial: tuple[int, int] | None
    posicion_final: tuple[int, int] | None

    def convertir_laberinto(self, laberinto) -> None:
        self.mapa = [list(fila.strip()) for fila in self.laberinto.split("\n")]

    def limpiar_pantalla(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar_mapa(self) -> None:
        for fila in self.mapa:
            print("".join(fila))

    def main_loop(self) -> None:
        px, py = self.posicion_inicial
        while (px, py) != self.posicion_final:
            self.limpiar_pantalla()
            self.mapa[px][py] = "P"
            self.mostrar_mapa()
            self.mapa[px][py] = "."

            tecla = readkey()
            if tecla == key.UP and px > 0 and self.mapa[px - 1][py] != "#":
                px -= 1  # Flecha arriba
            elif (
                tecla == key.DOWN
                and px < len(self.mapa) - 1
                and self.mapa[px + 1][py] != "#"
            ):
                px += 1  # Flecha abajo
            elif tecla == key.LEFT and py > 0 and self.mapa[px][py - 1] != "#":
                py -= 1  # Flecha izquierda
            elif (
                tecla == key.RIGHT
                and py < len(self.mapa[0]) - 1
                and self.mapa[px][py + 1] != "#"
            ):
                py += 1  # Flecha derecha
        print("Ganaste")


class JuegoArchivo:
    def _init_(self):
        self.juego = Juego(
            posicion_inicial=(0, 0), laberinto=None, mapa=None, posicion_final=None
        )

    def leer_archivo(self) -> str:
        path = "\Users\USUARIO\Desktop\ADA SCHOOL\Adaschool\Adaschool\parte5.py\directorio_de_mapas.py"
        laberinto = """..###################
        ....#...............#
        #.#.#####.#########.#
        #.#...........#.#.#.#
        #.#####.#.###.#.#.#.#
        #...#.#.#.#.....#...#
        #.#.#.#######.#.#####
        #.#...#.....#.#...#.#
        #####.#####.#.#.###.#
        #.#.#.#.......#...#.#
        #.#.#.#######.#####.#
        #...#...#...#.#.#...#
        ###.#.#####.#.#.###.#
        #.#...#.......#.....#
        #.#.#.###.#.#.###.#.#
        #...#.#...#.#.....#.#
        ###.#######.###.###.#
        #.#.#.#.#.#...#.#...#
        #.#.#.#.#.#.#.#.#.#.#
        #.....#.....#.#.#.#.#
        ###################.."""
        if os.path.exists(path):
            mapas = os.listdir(path)
            laberinto = list()
            if len(mapas) > 0:
                mapa = random.choice(mapas)
                with open(path + "/" + mapa, "r") as archivo:
                    laberinto = archivo.read()
            else:
                raise NotFileError(
                    "No hay archivos en la carpeta mapas, se cargará el mapa por defecto"
                )
        return laberinto.strip()

    def iniciar_juego(self):
        self.juego.laberinto = self.leer_archivo()
        self.juego.convertir_laberinto(self.juego.laberinto)
        self.juego.posicion_final = (
            len(self.juego.mapa) - 1,
            len(self.juego.mapa[0]) - 1,
        )
        self.juego.main_loop()


Jugar = JuegoArchivo()
Jugar.iniciar_juego()
