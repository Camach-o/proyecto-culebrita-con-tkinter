from tkinter import *
import random

class Culebrita:
    def __init__(self):
        self.culebrita = []
        self.matriz_celdas = []
        self.flechas = ("Up", "Down", "Left", "Right")
        self.flecha_inicial = random.choice(self.flechas)
        self.flecha_actual = None

    def crear_cuadro(self):

        coord = self.culebrita[-1].get("coord")
        if self.culebrita[-1].get("pnult_flecha"):
            flecha = self.culebrita[-1].get("pnult_flecha")
        else:
            flecha = self.flecha_inicial

        nueva_coord = self.determinar_direccion(coord, flecha)

        label = self.matriz_celdas[nueva_coord[0]][nueva_coord[1]]

        label.config(background="red")
        cuadro = {"label":label, "coord":(nueva_coord[0], nueva_coord[1]), 
                    "ult_flecha":flecha, "pnult_flecha":None}
                    
        self.culebrita.append(cuadro)

    def guardar_flecha(self, event):
        if event.keysym in self.flechas:
            self.flecha_actual = event.keysym
        else:
            pass

    def siguiente_coordenada(self, coord, flecha):
        if flecha == "Up":
            return coord[0]-1, coord[1]
        elif flecha == "Down":
            return coord[0]+1, coord[1]
        elif flecha == "Left":
            return coord[0], coord[1]-1
        elif flecha == "Right":
            return coord[0], coord[1]+1

    def mover_culebrita(self):

        if self.flecha_actual:
            nueva_flecha = self.flecha_actual
        else:
            nueva_flecha = self.flecha_inicial

        for cuadro in self.culebrita:
            cuadro.get("label").config(background="green")
            pnult_flecha = cuadro.get("ult_flecha")

            nueva_coord = self.siguiente_coordenada(cuadro.get("coord"), pnult_flecha)

            label = self.matriz_celdas[nueva_coord[0]][nueva_coord[1]]
            if label.config().get("background")[-1] == "blue":
                self.crear_cuadro()
                self.crear_fruta()
            label.config(background="red")

            cuadro.update({"label": label, "coord": nueva_coord, "ult_flecha": nueva_flecha, "pnult_flecha": pnult_flecha})

            nueva_flecha = pnult_flecha

        self.ventana.after(140, self.mover_culebrita)

    def crear_ventana(self):
        self.ventana = Tk()
        self.ventana.title("Culebrita")
        self.ventana.geometry("+350+80")
        self.ventana.bind("<KeyPress>", self.guardar_flecha)

    def crear_celdas(self, x, y):
        for fila in range(0, x):
            fila_matriz = []
            for columna in range(0, y):
                cuadro = Label(self.ventana, bd=2, bg="green", width=5, height=2, relief="sunken")
                cuadro.grid(row=fila, column=columna)
                fila_matriz.append(cuadro)
            self.matriz_celdas.append(fila_matriz)

    def determinar_direccion(self, coord, flecha):
        if flecha == "Up":
            return coord[0]+1, coord[1]
        elif flecha == "Down":
            return coord[0]-1, coord[1]
        elif flecha == "Left":
            return coord[0], coord[1]+1
        elif flecha == "Right":
            return coord[0], coord[1]-1

    def crear_fruta(self):
        while True:

            label = self.matriz_celdas[random.randint(5, 15)][random.randint(5, 15)]
            if label.config().get("background")[-1] == "green":
                label.config(background="blue")
                break
            else:
                continue

    def crear_culebrita(self):

        row = random.randint(10, 12)
        col = random.randint(10, 12)

        label = self.matriz_celdas[row][col]
        label.config(background="red")
        cuadro = {"label":label, "coord":(row, col), "ult_flecha":self.flecha_inicial, "pnult_flecha":None}
        self.culebrita.append(cuadro)

        self.crear_cuadro()
        self.crear_cuadro()

    def iniciar(self):
        self.crear_ventana()
        self.crear_celdas(20, 20)
        self.crear_culebrita()
        self.crear_fruta()
        self.mover_culebrita()
        for cuadro in self.culebrita:
            print(cuadro)
        self.ventana.mainloop()

def main():
    juego = Culebrita()
    juego.iniciar()

if __name__ == "__main__":
    main()