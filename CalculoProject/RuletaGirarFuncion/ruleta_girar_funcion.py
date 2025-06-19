import tkinter as tk
from PIL import Image, ImageTk
import random

class RuletaClase(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ruleta Giratoria")
        self.geometry("600x400")
        self.configure(bg="#222")

        # Carga la imagen original de la ruleta
        self.ruleta_orig = Image.open("Ruleta.png").convert("RGBA")
        self.ruleta_tk = ImageTk.PhotoImage(self.ruleta_orig)

        # Canvas para dibujar la ruleta
        self.canvas = tk.Canvas(self, width=self.ruleta_orig.width, height=self.ruleta_orig.height, bg="#222", highlightthickness=0)
        self.canvas.pack(pady=20)
        self.ruleta_item = self.canvas.create_image(
            self.ruleta_orig.width//2,
            self.ruleta_orig.height//2,
            image=self.ruleta_tk
        )

        # Botón para girar
        btn = tk.Button(self, text="Girar", command=self.empezar_giro, font=("Arial", 14, "bold"))
        btn.pack()

        # Parámetros de animación
        self.animando = False
        self.angulo_actual = 0

    def empezar_giro(self):
        if self.animando:
            return  # no interrumpir si ya está girando
        self.animando = True
        # Elige un ángulo final aleatorio (por ejemplo entre 3 y 6 vueltas completas más un resto)
        vueltas = random.randint(3, 6)
        resto = random.randint(0, 359)
        self.angulo_destino = vueltas * 360 + resto
        self._animar()

    def _animar(self):
        # Velocidad variable: más rápido al inicio, más lento al acercarse al destino
        distancia = self.angulo_destino - self.angulo_actual
        if distancia <= 0:
            # Termina la animación
            self.animando = False
            return

        # paso = una fracción de la distancia restante (makes easing out)
        paso = max(1, int(distancia / 15))
        self.angulo_actual += paso

        # Rota la imagen
        ruleta_rotada = self.ruleta_orig.rotate(-self.angulo_actual, resample=Image.BICUBIC, expand=False)
        self.ruleta_tk = ImageTk.PhotoImage(ruleta_rotada)
        self.canvas.itemconfigure(self.ruleta_item, image=self.ruleta_tk)

        # siguiente frame
        # cuanto más pequeña la distancia, mayor el retraso → efecto de frenado
        delay = int(20 + (distancia / self.angulo_destino) * 30)
        self.after(delay, self._animar)

if __name__ == "__main__":
    app = RuletaClase()
    app.mainloop()
