# ===============================
# Importación de librerías
# ===============================

import tkinter as tk                              # Interfaz gráfica principal
from tkinter import messagebox                    # Cuadros de diálogo emergentes
import random                                     # Selección aleatoria de ejercicios
import time                                       # Pausas en animaciones
import threading                                  # Hilos para tareas en paralelo
from PIL import Image, ImageTk                    # Para manejar imágenes
import pygame                                     # Para sonidos
import os                                         # Acceso a archivos del sistema

from datos import (
    ejercicios,
    temas,
    Dificultad,
)  # Importación de datos externos: lista de ejercicios, temas y niveles


# ===============================
# Clase principal de la aplicación
# ===============================
class RuletaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Ruleta Interactiva de Cálculo")
        self.root.iconbitmap("LogoCalculo.ico")
        self.root.geometry("900x600")

        # Inicialización de sonido
        pygame.mixer.init()
        self.sonido_click = pygame.mixer.Sound("button-click.mp3")

        self.temas = list(ejercicios.keys())
        self.dificultades = {
            "FÁCIL": "1",
            "INTERMEDIO": "2",
            "DIFÍCIL": "3",
        }
        self.tema_actual = None

        # ===============================
        # Carga de imágenes
        # ===============================
        self.bg_img = ImageTk.PhotoImage(
            Image.open("bg_app.png").resize((900, 600), Image.LANCZOS)
        )
        self.titulo_img = ImageTk.PhotoImage(Image.open("TextoTitulo.png"))
        self.boton_jugar_img = ImageTk.PhotoImage(Image.open("BotonJugar.png"))
        self.boton_instrucciones_img = ImageTk.PhotoImage(Image.open("BotonInstrucciones.png"))
        self.boton_girar_img = ImageTk.PhotoImage(Image.open("BotonGirarRuleta.png"))
        self.boton_empezar_img = ImageTk.PhotoImage(Image.open("BotonMostrarEjercicio.png"))

        original_salir = Image.open("BotonSalir.png")
        self.boton_salir_img = ImageTk.PhotoImage(original_salir)
        small_salir = original_salir.resize((120, 40), Image.LANCZOS)
        self.boton_salir_img_peque = ImageTk.PhotoImage(small_salir)

        # ===============================
        # Menú principal
        # ===============================
        self.menu_frame = tk.Frame(self.root, width=900, height=600)
        self.menu_frame.pack_propagate(False)

        self.menu_bg_label = tk.Label(self.menu_frame, image=self.bg_img)
        self.menu_bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.menu_titulo = tk.Label(
            self.menu_frame,
            image=self.titulo_img,
            bg="#9e3d3d",
            borderwidth=0,
        )
        self.menu_titulo.pack(pady=30)

        self.boton_jugar = tk.Button(
            self.menu_frame,
            image=self.boton_jugar_img,
            command=lambda: [
                self.reproducir_sonido_boton(),
                self.mostrar_interfaz_juego(),
            ],
            borderwidth=0,
            bg="#9e3d3d",
            activebackground="#9e3d3d",
        )
        self.boton_jugar.pack(pady=10)

        self.boton_instrucciones = tk.Button(
            self.menu_frame,
            image=self.boton_instrucciones_img,
            command=lambda: [
                self.reproducir_sonido_boton(),
                self.mostrar_instrucciones(),
            ],
            borderwidth=0,
            bg="#9e3d3d",
            activebackground="#9e3d3d",
        )
        self.boton_instrucciones.pack(pady=10)

        self.boton_salir = tk.Button(
            self.menu_frame,
            image=self.boton_salir_img,
            command=lambda: [
                self.reproducir_sonido_boton(),
                self.root.quit(),
            ],
            borderwidth=0,
            bg="#9e3d3d",
            activebackground="#9e3d3d",
        )
        self.boton_salir.pack(pady=10)

        self.menu_frame.pack()

        # ===============================
        # Interfaz del juego
        # ===============================
        self.interfaz_juego = tk.Frame(self.root, width=900, height=600)
        self.interfaz_juego.pack_propagate(False)

        self.bg_label_game = tk.Label(self.interfaz_juego, image=self.bg_img)
        self.bg_label_game.place(x=0, y=0, relwidth=1, relheight=1)

        self.titulo = tk.Label(
            self.interfaz_juego,
            image=self.titulo_img,
            bg="#9e3d3d",
            borderwidth=0,
        )
        self.titulo.pack(pady=10)
        self.titulo.lift()

        self.boton_girar = tk.Button(
            self.interfaz_juego,
            image=self.boton_girar_img,
            command=lambda: [
                self.reproducir_sonido_boton(),
                self.girar_ruleta(),
            ],
            borderwidth=0,
            bg="#9e3d3d",
            activebackground="#9e3d3d",
        )
        self.boton_girar.pack(pady=10)

        self.resultado_label = tk.Label(
            self.interfaz_juego,
            text="",
            font=("Impact", 20),
            fg="white",
            bg="#9e3d3d",
            highlightthickness=2,
            highlightbackground="white",
        )
        self.resultado_label.pack_forget()

        self.dificultad_var = tk.StringVar(value="FÁCIL")
        self.menu_dificultad = tk.OptionMenu(
            self.interfaz_juego,
            self.dificultad_var,
            *self.dificultades.keys(),
        )
        self.menu_dificultad.config(
            bg="#cc3131",
            fg="white",
            font=("Impact", 18),
            width=20,
            highlightthickness=0,
        )
        self.menu_dificultad["menu"].config(
            bg="#cc3131",
            fg="white",
            font=("Arial", 11),
        )
        self.menu_dificultad.pack(pady=10)

        self.boton_empezar = tk.Button(
            self.interfaz_juego,
            image=self.boton_empezar_img,
            command=lambda: [
                self.reproducir_sonido_boton(),
                self.mostrar_ejercicio(),
            ],
            borderwidth=0,
            bg="#9e3d3d",
            activebackground="#9e3d3d",
            state="disabled",
        )
        self.boton_empezar.pack(pady=10)

        self.pregunta_label = tk.Label(
            self.interfaz_juego,
            text="",
            wraplength=500,
            font=("Arial", 12),
            fg="white",
            bg="#9e3d3d",
            highlightthickness=2,
            highlightbackground="white",
        )
        self.pregunta_label.pack_forget()

        self.opciones_frame = tk.Frame(self.interfaz_juego, bg="#9e3d3d")
        self.opciones_frame.pack_forget()

        self.boton_volver_menu = tk.Button(
            self.interfaz_juego,
            image=self.boton_salir_img_peque,
            command=lambda: [
                self.reproducir_sonido_boton(),
                self.volver_al_menu(),
            ],
            borderwidth=0,
            bg="#9e3d3d",
            activebackground="#9e3d3d",
        )
        self.boton_volver_menu.place(relx=0.95, rely=0.95, anchor="se")

    # ===============================
    # Funciones auxiliares
    # ===============================

    def reproducir_sonido_boton(self):
        if self.sonido_click:
            self.sonido_click.play()

    def mostrar_interfaz_juego(self):
        self.menu_frame.pack_forget()
        self.interfaz_juego.pack()

    def volver_al_menu(self):
        self.interfaz_juego.pack_forget()
        self.menu_frame.pack()

    def mostrar_instrucciones(self):
        messagebox.showinfo(
            "Instrucciones",
            "1. Selecciona la dificultad.\n2. Haz click en |PREPARAR TEMA|.\n3. Responde el ejercicio que aparezca.",
        )

    def girar_ruleta(self):
        # 🔹 Mostrar el label solo cuando se presiona el botón
        self.resultado_label.pack(pady=10)
        self.resultado_label.config(
            text="Eligiendo tema...",
            bg="#a35353",
        )
        threading.Thread(target=self._girar_ruleta_animacion).start()

    def _girar_ruleta_animacion(self):
        for _ in range(5):
            time.sleep(0.3)
        self.tema_actual = random.choice(self.temas)
        self.resultado_label.config(text=f"Tema seleccionado: {self.tema_actual}")
        self.boton_empezar.config(state="normal")

    def mostrar_ejercicio(self):
        if self.tema_actual is None:
            messagebox.showerror(
                "Error",
                "⚠️ Debes girar la ruleta antes de mostrar un ejercicio.",
            )
            return

        dificultad_str = self.dificultad_var.get()
        dificultad = self.dificultades[dificultad_str]
        lista_ej = ejercicios[self.tema_actual][dificultad]
        self.ejercicio_actual = random.choice(lista_ej)

        self.pregunta_label.config(text=self.ejercicio_actual["pregunta"])
        self.pregunta_label.pack(pady=10)

        # Elimina opciones anteriores
        for widget in self.opciones_frame.winfo_children():
            widget.destroy()

        # Muestra nuevas opciones
        for letra, texto in self.ejercicio_actual["opciones"].items():
            b = tk.Button(
                self.opciones_frame,
                text=f"{letra}) {texto}",
                width=40,
                command=lambda l=letra: [
                    self.reproducir_sonido_boton(),
                    self.verificar_respuesta(l),
                ],
                bg="#cc3131",
                fg="white",
                font=("Arial", 11),
                activebackground="#a62828",
            )
            b.pack(pady=2)
            self.opciones_frame.pack(pady=5)

    def verificar_respuesta(self, letra):
        correcta = self.ejercicio_actual["respuesta"]

        if letra == correcta:
            messagebox.showinfo("Resultado", "✅ ¡Respuesta Correcta!")
        else:
            messagebox.showerror(
                "Resultado",
                f"❌ Incorrecto. La respuesta correcta era: {correcta}",
            )

        self.pregunta_label.config(text="")
        self.pregunta_label.pack_forget()

        for widget in self.opciones_frame.winfo_children():
            widget.destroy()
            self.opciones_frame.pack_forget()

        self.boton_empezar.config(state="disabled")


# ===============================
# Inicialización de la app
# ===============================
if __name__ == "__main__":
    root = tk.Tk()
    app = RuletaApp(root)
    root.mainloop()