import json

import tkinter as tk
from PIL import Image, ImageTk

from tkinter import simpledialog, messagebox



class MiVentana:
    def __init__(self, master, VenIm):
        self.VenIm = VenIm
        self.master = master
        self.pokemones = self.cargar_pokemones()
        self.respuestas = []
        self.pokemon_adivinado = None
        self.contador = 0

        # Botones Sí y No
        self.boton_si = tk.Button(self.master, text="Sí", command=lambda: self.registrar_respuesta(True))
        self.boton_si.pack(side=tk.LEFT, padx=10)

        self.boton_no = tk.Button(self.master, text="No", command=lambda: self.registrar_respuesta(False))
        self.boton_no.pack(side=tk.LEFT, padx=10)

        # Etiqueta de pregunta
        self.lbl_preg = tk.Label(self.master, text="Selecciona una característica:")
        self.lbl_preg.pack()

        self.caracteristicas = list(self.pokemones["pikachu"].keys())
        self.caracteristica_actual = self.caracteristicas[0]

        self.actualizar_pregunta()

    def cargar_pokemones(self):
        try:
            with open("pokemones.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {
                "pikachu": {
                    "es_amarillo": "True",
                    "es_pequeño": "True",
                    "tiene_mejillas_rojas": "True",
                    "es_naranja": "False",
                    "tiene_cola_de_fuego": "False",
                    "tiene_orejas": "True",
                    "tiene_craneo_de_sombrero": "False",
                    "tiene_hueso_en_la_mano": "False",
                    "tiene_mamá": "True",
                    "es_verde": "False",
                    "tiene_semilla_en_la_espalda": "False",
                    "tiene_ojos_rojos": "False",
                    "es_azul": "False",
                    "tiene_caparazon": "False",
                    "tiene_ojos_cafe": "False",
                },
                "charmander": {
                    "es_amarillo": "False",
                    "es_pequeño": "True",
                    "tiene_mejillas_rojas": "False",
                    "es_naranja": "True",
                    "tiene_cola_de_fuego": "True",
                    "tiene_orejas": "False",
                    "tiene_craneo_de_sombrero": "False",
                    "tiene_hueso_en_la_mano": "False",
                    "tiene_mamá": "True",
                    "es_verde": "False",
                    "tiene_semilla_en_la_espalda": "False",
                    "tiene_ojos_rojos": "False",
                    "es_azul": "False",
                    "tiene_caparazon": "False",
                    "tiene_ojos_cafe": "False",
                },                
                "squirtle": {
                    "es_amarillo": "False",
                    "es_pequeño": "True",
                    "tiene_mejillas_rojas": "False",
                    "es_naranja": "False",
                    "tiene_cola_de_fuego": "False",
                    "tiene_orejas": "False",
                    "tiene_craneo_de_sombrero": "False",
                    "tiene_hueso_en_la_mano": "False",
                    "tiene_mamá": "True",
                    "es_verde": "False",
                    "tiene_semilla_en_la_espalda": "False",
                    "tiene_ojos_rojos": "False",
                    "es_azul": "True",
                    "tiene_caparazon": "True",
                    "tiene_ojos_cafe": "True",
                },
                "bulbasaur": {
                    "es_amarillo": "False",
                    "es_pequeño": "True",
                    "tiene_mejillas_rojas": "False",
                    "es_naranja": "False",
                    "tiene_cola_de_fuego": "False",
                    "tiene_orejas": "True",
                    "tiene_craneo_de_sombrero": "False",
                    "tiene_hueso_en_la_mano": "False",
                    "tiene_mamá": "True",
                    "es_verde": "True",
                    "tiene_semilla_en_la_espalda": "True",
                    "tiene_ojos_rojos": "True",
                    "es_azul": "False",
                    "tiene_caparazon": "False",
                    "tiene_ojos_cafe": "False",
                },
                "cubone": {
                    "es_amarillo": "False",
                    "es_pequeño": "True",
                    "tiene_mejillas_rojas": "False",
                    "es_naranja": "True",
                    "tiene_cola_de_fuego": "False",
                    "tiene_orejas": "True",
                    "tiene_craneo_de_sombrero": "True",
                    "tiene_hueso_en_la_mano": "True",
                    "tiene_mamá": "False",
                    "es_verde": "False",
                    "tiene_semilla_en_la_espalda": "False",
                    "tiene_ojos_rojos": "False",
                    "es_azul": "False",
                    "tiene_caparazon": "False",
                    "tiene_ojos_cafe": "False",
                }
            }

    def guardar_pokemones(self):
        with open("pokemones.json", "w") as file:
            json.dump(self.pokemones, file, indent=4)

    def registrar_respuesta(self, respuesta):
        caracteristica = self.caracteristica_actual
        self.respuestas.append((caracteristica, respuesta))

        self.contador += 1

        if self.contador == len(self.caracteristicas):
            self.adivinar_pokemon()
        else:
            self.caracteristica_actual = self.caracteristicas[self.contador]
            self.actualizar_pregunta()

    def adivinar_pokemon(self):
        for pokemon, caracteristicas in self.pokemones.items():
            coincide = all(caracteristicas[caracteristica] == str(respuesta) for caracteristica, respuesta in self.respuestas)
            if coincide:
                self.pokemon_adivinado = pokemon
                break

        if self.pokemon_adivinado is None:
            print("Ningún pokemon coincide con las características.")
            nuevo_pokemon = self.agregar_nuevo_pokemon()
            if nuevo_pokemon:
                self.pokemones[nuevo_pokemon] = {caracteristica: str(respuesta) for caracteristica, respuesta in self.respuestas}
                self.guardar_pokemones()
                print(f"Se ha agregado el pokemon {nuevo_pokemon}.")
        else:
            print(f"El pokemon que estás pensando es {self.pokemon_adivinado}")

        respuesta = messagebox.askyesno("Jugar de nuevo", f"Tu pokemon es: {self.pokemon_adivinado}\n¿Deseas jugar de nuevo?")
        if respuesta:
            self.reiniciar_juego()
        else:
            self.VenIm.destroy()
            self.master.destroy()

    def agregar_nuevo_pokemon(self):
        nuevo_pokemon = simpledialog.askstring("Nuevo pokemon", "Ningún pokemon coincide. Ingresa un nuevo nombre:")
        return nuevo_pokemon

    def reiniciar_juego(self):
        self.respuestas = []
        self.pokemon_adivinado = None
        self.contador = 0
        self.caracteristicas = list(self.pokemones[list(self.pokemones.keys())[0]].keys())
        self.caracteristica_actual = self.caracteristicas[0]
        self.actualizar_pregunta()

    def actualizar_pregunta(self):
        caracteristica_formateada = self.caracteristica_actual.replace('_', ' ')
        self.lbl_preg.config(text=f"¿{caracteristica_formateada}?", font=("Arial Bold", 20), fg="Blue")
        

def iniciar_juego(venIm):
    ventana = tk.Tk()
    ventana.title("Adivina el Pokemon")
    ventana.geometry("500x100+250+800")
    mi_ventana = MiVentana(ventana,venIm)
    ventana.mainloop()

class Ventana1_MostrarPoke:
    def __init__(self, master):
        self.master = master

        #Imagenes

        # Cargar la imagen de fondo
        bg_image = Image.open("cargando.jpeg")
        bg_image = bg_image.resize((1000, 650))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Crear una etiqueta para la imagen de fondo
        self.bg_label = tk.Label(self.master, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.lbl_bienvenida = tk.Label(self.master, text="¡Bienvenido al juego Adivina Quién de Pokemon!", bg="red")
        self.lbl_bienvenida.config(font=("Times New Roman", 20), fg="yellow")
        self.lbl_bienvenida.place(x=200, y=0)
        self.lbl_bienvenida.pack()

        self.lbl_bienvenida = tk.Label(self.master, text="¡Elige Pokemon!", bg="Black")
        self.lbl_bienvenida.config(font=("Times New Roman", 20), fg="White")
        self.lbl_bienvenida.place(x=250, y=500)
        
        img_Rick = Image.open("pikachu.png")
        img_Rick = img_Rick.resize((100, 100))
        img_Rick_tk = ImageTk.PhotoImage(img_Rick)
        self.lbl_img_Rick = tk.Label(master, image=img_Rick_tk)
        self.lbl_img_Rick.image = img_Rick_tk
        self.lbl_img_Rick.pack()
        self.lbl_img_Rick.place(x=100, y=540)

        img_Morthy = Image.open("charmander.png")
        img_Morthy = img_Morthy.resize((100, 100))
        img_Morthy_tk = ImageTk.PhotoImage(img_Morthy)
        self.lbl_img_Morthy = tk.Label(master, image=img_Morthy_tk)
        self.lbl_img_Morthy.image = img_Morthy_tk
        self.lbl_img_Morthy.pack()
        self.lbl_img_Morthy.place(x=200, y=540)

        img_Summer = Image.open("bulbasaur.png")
        img_Summer = img_Summer.resize((100, 100))
        img_Summer_tk = ImageTk.PhotoImage(img_Summer)
        self.lbl_img_Summer = tk.Label(master, image=img_Summer_tk)
        self.lbl_img_Summer.image = img_Summer_tk
        self.lbl_img_Summer.pack()
        self.lbl_img_Summer.place(x=300, y=540)

        img_Beth = Image.open("squirtle.png")
        img_Beth = img_Beth.resize((100, 100))
        img_Beth_tk = ImageTk.PhotoImage(img_Beth)
        self.lbl_img_Beth = tk.Label(master, image=img_Beth_tk)
        self.lbl_img_Beth.image = img_Beth_tk
        self.lbl_img_Beth.pack()
        self.lbl_img_Beth.place(x=400, y=540)

        img_Jerry = Image.open("cubone.png")
        img_Jerry = img_Jerry.resize((100, 100))
        img_Jerry_tk = ImageTk.PhotoImage(img_Jerry)
        self.lbl_img_Jerry = tk.Label(master, image=img_Jerry_tk)
        self.lbl_img_Jerry.image = img_Jerry_tk
        self.lbl_img_Jerry.pack()
        self.lbl_img_Jerry.place(x=500, y=540)
        
        #Botones
        
        self.boton_cerrar = tk.Button(master, text="Siguiente", command=self.cerrar_ventana)
        self.boton_cerrar.config(font=("Arial", 20))
        self.boton_cerrar.config(bg="red", fg="black")
        self.boton_cerrar.place(x= 800, y = 500)

    def cerrar_ventana(self):
        self.master.destroy()
        nueva_ventana = Ventana2_RondaPreg()

class Ventana2_RondaPreg:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry("700x700+150+10")
        self.master.title("Ronda de preguntas")

        # Cargar la imagen de fondo
        bg_image = Image.open("adivina.png")
        bg_image = bg_image.resize((700, 700))
        self.bg_photo = ImageTk.PhotoImage(bg_image)

        # Crear una etiqueta para la imagen de fondo
        self.bg_label = tk.Label(self.master, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Carga de imágenes
        img_Rick = Image.open("pikachu.png")
        img_Morthy = Image.open("charmander.png")
        img_Summer = Image.open("bulbasaur.png")
        img_Beth = Image.open("squirtle.png")
        img_Jerry = Image.open("cubone.png")

        # Redimensionamiento de imágenes
        img_Rick = img_Rick.resize((100, 100))
        img_Morthy = img_Morthy.resize((100, 100))
        img_Summer = img_Summer.resize((100, 100))
        img_Beth = img_Beth.resize((100, 100))
        img_Jerry = img_Jerry.resize((100, 100))

        # Convertir imágenes a formato tkinter
        img_Rick_tk = ImageTk.PhotoImage(img_Rick)
        img_Morthy_tk = ImageTk.PhotoImage(img_Morthy)
        img_Summer_tk = ImageTk.PhotoImage(img_Summer)
        img_Beth_tk = ImageTk.PhotoImage(img_Beth)
        img_Jerry_tk = ImageTk.PhotoImage(img_Jerry)

        # Etiquetas para las imágenes
        self.lbl_img_Rick = tk.Label(self.master, image=img_Rick_tk)
        self.lbl_img_Rick.image = img_Rick_tk
        self.lbl_img_Rick.pack()
        self.lbl_img_Rick.place(x=0, y=600)

        self.lbl_img_Morthy = tk.Label(self.master, image=img_Morthy_tk)
        self.lbl_img_Morthy.image = img_Morthy_tk
        self.lbl_img_Morthy.pack()
        self.lbl_img_Morthy.place(x=100, y=600)

        self.lbl_img_Summer = tk.Label(self.master, image=img_Summer_tk)
        self.lbl_img_Summer.image = img_Summer_tk
        self.lbl_img_Summer.pack()
        self.lbl_img_Summer.place(x=200, y=600)

        self.lbl_img_Beth = tk.Label(self.master, image=img_Beth_tk)
        self.lbl_img_Beth.image = img_Beth_tk
        self.lbl_img_Beth.pack()
        self.lbl_img_Beth.place(x=300, y=600)

        self.lbl_img_Jerry = tk.Label(self.master, image=img_Jerry_tk)
        self.lbl_img_Jerry.image = img_Jerry_tk
        self.lbl_img_Jerry.pack()
        self.lbl_img_Jerry.place(x=400, y=600)

        # Etiqueta para el título
        self.lbl_tPers = tk.Label(self.master, text="Pokemones", bg="red")
        self.lbl_tPers.config(font=("Times New Roman", 20), fg="yellow")
        self.lbl_tPers.pack()

        # Iniciar el juego
        iniciar_juego(self.master)

        self.master.mainloop()
    
    def cerrar_ventana(self):
        self.master.destroy()


if __name__ == "__main__":
    # Crear la ventana inicio
    ventana_inicio = tk.Tk()
    ventana_inicio.geometry("1000x650+150+10")
    ventana_inicio.title("Pokemones")

    # Crear una instancia de VentanaAnterior
    ventana = Ventana1_MostrarPoke(ventana_inicio)

    ventana_inicio.mainloop()

