import random
import time

ejercicios = {
    "Geometría Analítica": {
        "1": [
            {
                "pregunta": "Encuentra la distancia entre los puntos A(3,2) y B(7,5).",
                "opciones": {
                    "A": "5",
                    "B": "6",
                    "C": "7",
                    "D": "8"
                },
                "respuesta": "A"
            },
            {
                "pregunta": "Calcula la pendiente de la recta que pasa por A(1,2) y B(4,6).",
                "opciones": {
                    "A": "2/3",
                    "B": "3/2",
                    "C": "1/3",
                    "D": "2"
                },
                "respuesta": "A"
            }
        ],
        "2": [
            {
                "pregunta": "Encuentra la ecuación general de la recta que pasa por los puntos (2,3) y (4,7).",
                "opciones": {
                    "A": "y = 2x - 1",
                    "B": "y = x + 1",
                    "C": "y = 2x + 1",
                    "D": "y = 3x - 2"
                },
                "respuesta": "C"
            }
        ],
        "3": [
            {
                "pregunta": "Determina si los puntos A(1,2), B(3,6) y C(5,10) están alineados.",
                "opciones": {
                    "A": "Sí, están alineados.",
                    "B": "No, no están alineados.",
                    "C": "Solo A y B están alineados.",
                    "D": "Solo B y C están alineados."
                },
                "respuesta": "A"
            }
        ]
    },
    "Funciones y Gráficas": {
        "1": [
            {
                "pregunta": "Evalúa f(x) = 2x + 3 en x = 5.",
                "opciones": {
                    "A": "13",
                    "B": "15",
                    "C": "17",
                    "D": "10"
                },
                "respuesta": "A"
            }
        ],
        "2": [
            {
                "pregunta": "Determina el dominio de f(x) = 1 / (x - 2).",
                "opciones": {
                    "A": "x ≠ 2",
                    "B": "x ≠ 0",
                    "C": "x ≠ 1",
                    "D": "x ≠ -2"
                },
                "respuesta": "A"
            }
        ],
        "3": [
            {
                "pregunta": "Analiza la simetría de f(x) = x^3 - x.",
                "opciones": {
                    "A": "Es simétrica respecto al origen.",
                    "B": "Es simétrica respecto al eje X.",
                    "C": "Es simétrica respecto al eje Y.",
                    "D": "No tiene simetría."
                },
                "respuesta": "A"
            }
        ]
    },
    "Límites": {
        "1": [
            {
                "pregunta": "Calcula el límite: lim(x→2) (x^2 - 4)/(x - 2).",
                "opciones": {
                    "A": "4",
                    "B": "2",
                    "C": "1",
                    "D": "Indeterminado"
                },
                "respuesta": "A"
            }
        ],
        "2": [
            {
                "pregunta": "Resuelve: lim(x→0) (sin(x)/x).",
                "opciones": {
                    "A": "0",
                    "B": "1",
                    "C": "2",
                    "D": "Infinito"
                },
                "respuesta": "B"
            }
        ],
        "3": [
            {
                "pregunta": "Determina lim(x→∞) (3x^2 + x)/(2x^2 - 5).",
                "opciones": {
                    "A": "3/2",
                    "B": "1",
                    "C": "∞",
                    "D": "0"
                },
                "respuesta": "A"
            }
        ]
    },
    "Derivadas": {
        "1": [
            {
                "pregunta": "Deriva f(x) = x^2.",
                "opciones": {
                    "A": "2x",
                    "B": "x^2",
                    "C": "x",
                    "D": "x^3"
                },
                "respuesta": "A"
            }
        ],
        "2": [
            {
                "pregunta": "Halla la derivada de f(x) = x^3 + 2x.",
                "opciones": {
                    "A": "3x^2 + 2",
                    "B": "3x^2 + 1",
                    "C": "x^2 + 2",
                    "D": "x^3 + 2"
                },
                "respuesta": "A"
            }
        ],
        "3": [
            {
                "pregunta": "Calcula la derivada de f(x) = (x^2 + 1)/(x - 1).",
                "opciones": {
                    "A": "(2x(x-1) - (x^2 + 1)) / (x-1)^2",
                    "B": "(x^2 + 1)/(x^2 - 2x + 1)",
                    "C": "2x + 1",
                    "D": "Indeterminado"
                },
                "respuesta": "A"
            }
        ]
    },
    "Integrales": {
        "1": [
            {
                "pregunta": "Integra f(x) = x.",
                "opciones": {
                    "A": "x^2/2 + C",
                    "B": "x + C",
                    "C": "x^3 + C",
                    "D": "x^2 + C"
                },
                "respuesta": "A"
            }
        ],
        "2": [
            {
                "pregunta": "Resuelve ∫(2x + 1) dx.",
                "opciones": {
                    "A": "x^2 + x + C",
                    "B": "2x^2 + x + C",
                    "C": "2x + C",
                    "D": "x^2 + C"
                },
                "respuesta": "A"
            }
        ],
        "3": [
            {
                "pregunta": "Calcula ∫(x^2)/(x^3 + 1) dx.",
                "opciones": {
                    "A": "ln(x^3 + 1)/3 + C",
                    "B": "x^2 + C",
                    "C": "ln(x^3) + C",
                    "D": "Indeterminado"
                },
                "respuesta": "A"
            }
        ]
    }
}

temas = [
    "Geometría Analítica",
    "Funciones y Gráficas",
    "Límites",
    "Derivadas",
    "Integrales"
]

Dificultad = [
    "Fácil",
    "Intermedia",
    "Difícil"
]
print("Bienvenido a la Ruleta Interactiva de Cálculo!")
print("TEMAS: \n Geometría Análitica \n Funciones y Gráficas \n Límites \n Derivadas \n Integrales")

press = input("\nPresiona ENTER para girar la ruleta")

print("\nGirando la ruleta.", end="")

for _ in range(5):
    print(".", end="", flush=True)
    time.sleep(0.5)

tema_seleccionado = random.choice(temas)

print(f"\nLa ruleta se detuvo en: {tema_seleccionado}.")


while True:
    print("Qué dificultad deseas jugar?: ")
    print("DIFICULTAD: \n [1] Fácil \n [2] Intermedia \n [3] Difícil")

    resp_dificultad = input("\nEscribe el número según la dificulta que desees jugar: ")
    
    if resp_dificultad not in ["1", "2", "3"]:
        print("Error! Introduce de nuevo la difultad.")
    else:
        break

print(f"Tema a jugar: {tema_seleccionado}. Dificultad seleccionada: {resp_dificultad}.")

lista_ejercicios = ejercicios[tema_seleccionado][resp_dificultad]
ejercicio = random.choice(lista_ejercicios)

print(ejercicio["pregunta"])

print("\nOpciones: ")
for letra, opcion in ejercicio["opciones"].items():
    print(f"{letra}) {opcion}")

respuesta = str(input("\nEscribe tu respuesta: "))

respuesta = respuesta.upper()

if (respuesta == ejercicio["respuesta"]):
    print("Respuesta Correcta!")
else:
    print(f"Respuesta Incorrecta, la respuesta correcta era: {ejercicio['respuesta']}")