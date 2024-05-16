import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import random

class JuegoClue:
    def __init__(self, master):
        self.master = master
        self.master.title("Juego Clue")
        
        # Ajustar tamaño de la ventana
        self.master.geometry("600x700")
        
        # Lista de personajes y armas de "Dungeon Meshi"
        self.personajes = ["Laios", "Marcille", "Chilchuck", "Senshi", "Falin"]
        self.armas = ["Espada", "Bastón", "Arco", "Acha", "Daga"]
        
        # Lista de lugares
        self.lugares = ["Cocina", "Sala", "Baño", "Libreria", "Armeria"]
        
        # Diccionarios de pistas para personajes, armas y lugares
        self.pistas_personajes = {
            "Laios": ["Laios siempre lleva su fiel espada.", "Laios no fue a la Sala.", "Laios no usa un arco."],
            "Marcille": ["Marcille está siempre acompañada de su bastón mágico.", "Marcille no fue a la Cocina.", "Marcille no usa un hacha."],
            "Chilchuck": ["Chilchuck es sigiloso y lleva una daga oculta.", "Chilchuck no fue al Baño.", "Chilchuck no usa un bastón."],
            "Senshi": ["Senshi, siempre lista para la batalla y siempre lleva consigo un acha.", "Senshi no fue a la Libreria.", "Senshi no usa una daga."],
            "Falin": ["Falin es una arquera experta, carga consigo su fiel arco.  ", "Falin no fue a la Armeria.", "Falin no usa un arco."]
        }
        
        self.pistas_armas = {
            "Espada": ["El arma del crimen es una espada.", "La espada no se usó en la Cocina.", "El arma del crimen no es un arco."],
            "Bastón": ["El arma del crimen es un bastón.", "El bastón no se usó en la Sala.", "El arma del crimen no es una espada."],
            "Arco": ["El arma del crimen es un arco.", "El arco no se usó en el Baño.", "El arma del crimen no es un bastón."],
            "Acha": ["El arma del crimen es un acha.", "El acha no se usó en la Libreria.", "El arma del crimen no es una daga."],
            "Daga": ["El arma del crimen es una daga.", "La daga no se usó en la Armeria.", "El arma del crimen no es una espada."]
        }
        
        self.pistas_lugares = {
            "Cocina": ["El crimen no ocurrió en la Cocina.", "La Cocina no fue el lugar del crimen de Laios.", "El crimen no fue con un arco en la Cocina."],
            "Sala": ["El crimen no ocurrió en la Sala.", "La Sala no fue el lugar del crimen de Marcille.", "El crimen no fue con una espada en la Sala."],
            "Baño": ["El crimen no ocurrió en el Baño.", "El Baño no fue el lugar del crimen de Chilchuck.", "El crimen no fue con un bastón en el Baño."],
            "Libreria": ["El crimen no ocurrió en la Libreria.", "La Libreria no fue el lugar del crimen de Senshi.", "El crimen no fue con un acha en la Libreria."],
            "Armeria": ["El crimen no ocurrió en la Armeria.", "La Armeria no fue el lugar del crimen de Falin.", "El crimen no fue con un arco en la Armeria."]
        }
        
        # Variables para almacenar las selecciones del jugador
        self.personaje_seleccionado = tk.StringVar(master)
        self.lugar_seleccionado = tk.StringVar(master)
        self.arma_seleccionada = tk.StringVar(master)
        
        # Configurar las opciones seleccionables para personajes, lugares y armas
        self.personaje_seleccionado.set(self.personajes[0])
        self.lugar_seleccionado.set(self.lugares[0])
        self.arma_seleccionada.set(self.armas[0])
        
        # Desplegar opciones seleccionables
        self.menu_personajes = tk.OptionMenu(master, self.personaje_seleccionado, *self.personajes, command=self.mostrar_pistas_personaje)
        self.menu_personajes.pack()
        self.menu_lugares = tk.OptionMenu(master, self.lugar_seleccionado, *self.lugares, command=self.mostrar_pistas_lugar)
        self.menu_lugares.pack()
        self.menu_armas = tk.OptionMenu(master, self.arma_seleccionada, *self.armas, command=self.mostrar_pistas_arma)
        self.menu_armas.pack()
        
        # Cargar y mostrar imagen de lugares
        self.ruta_imagen = "dungeon.png"
        self.cargar_imagen()
        
        # Etiqueta para mostrar las pistas
        self.etiqueta_pistas = tk.Label(self.master, text="")
        self.etiqueta_pistas.pack()
        
        # Escena del crimen
        self.escena_crimen = self.generar_escena_crimen()
        
        # Etiqueta para mostrar la historia del crimen
        self.etiqueta_historia = tk.Label(self.master, text=self.escena_crimen["historia"])
        self.etiqueta_historia.pack()
        
        # Botón para resolver el caso
        self.boton_resolver = tk.Button(self.master, text="Resolver", command=self.resolver_caso)
        self.boton_resolver.pack()
        
        # Botón para reiniciar el juego
        self.boton_reiniciar = tk.Button(self.master, text="Reiniciar", command=self.reiniciar_juego)
        self.boton_reiniciar.pack()
        
        # Etiqueta para mostrar el resultado
        self.etiqueta_resultado = tk.Label(self.master, text="")
        self.etiqueta_resultado.pack()
        
    def cargar_imagen(self):
        # Redimensionar imagen para que se ajuste al tamaño de la ventana
        imagen = Image.open(self.ruta_imagen)
        imagen = imagen.resize((400, 300))
        self.img = ImageTk.PhotoImage(imagen)
        
        # Mostrar imagen en un widget Label
        self.etiqueta_imagen = tk.Label(self.master, image=self.img)
        self.etiqueta_imagen.pack()
        
    def generar_escena_crimen(self):
        # Obtener personaje, lugar y arma aleatorios
        personaje = random.choice(self.personajes)
        lugar = random.choice(self.lugares)
        arma = random.choice(self.armas)
        
        # Generar una historia de asesinato
        if personaje == "Laios":
            historia = f"Sissel fue encontrado muerto en la {lugar} con un {arma}."
        elif personaje == "Marcille":
            historia = f"Sissel fue encontrado muerto en la {lugar} con una {arma}."
        elif personaje == "Chilchuck":
            historia = f"Sissel fue encontrado muerto en la {lugar} con un {arma}."
        elif personaje == "Falin":
            historia = f"Sissel fue encontrado muerto en la {lugar} con una {arma}."
        elif personaje == "Senshi":
            historia = f"Sissel fue encontrado muerto en la {lugar} con un {arma}."
        
        return {"personaje": personaje, "lugar": lugar, "arma": arma, "historia": historia}
    
    def mostrar_pistas_personaje(self, *args):
        personaje = self.personaje_seleccionado.get()
        pistas = self.pistas_personajes.get(personaje, [])
        self.mostrar_pistas(pistas)
    
    def mostrar_pistas_lugar(self, *args):
        lugar = self.lugar_seleccionado.get()
        pistas = self.pistas_lugares.get(lugar, [])
        self.mostrar_pistas(pistas)
        
    def mostrar_pistas_arma(self, *args):
        arma = self.arma_seleccionada.get()
        pistas = self.pistas_armas.get(arma, [])
        self.mostrar_pistas(pistas)
        
    def mostrar_pistas(self, pistas):
        self.etiqueta_pistas.config(text="\n".join(pistas))
        
    def resolver_caso(self):
        sospechoso = self.escena_crimen["personaje"]
        
        if sospechoso == self.personaje_seleccionado.get():
            self.etiqueta_resultado.config(text="¡Felicidades! Has resuelto el caso.")
        else:
            self.etiqueta_resultado.config(text="Incorrecto. Inténtalo de nuevo.")
        
    def reiniciar_juego(self):
        self.personaje_seleccionado.set(random.choice(self.personajes))
        self.lugar_seleccionado.set(random.choice(self.lugares))
        self.arma_seleccionada.set(random.choice(self.armas))
        self.etiqueta_pistas.config(text="")
        self.etiqueta_resultado.config(text="")
        self.escena_crimen = self.generar_escena_crimen()
        self.etiqueta_historia.config(text=self.escena_crimen["historia"])
        
    def ejecutar(self):
        self.master.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    juego = JuegoClue(root)
    juego.ejecutar()
