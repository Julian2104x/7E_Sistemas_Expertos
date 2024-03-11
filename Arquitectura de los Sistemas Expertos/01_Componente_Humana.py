# Definición de la base de conocimiento
base_conocimiento = {
    "dolor_cabeza": ["tomar analgésicos", "descansar en un lugar oscuro"],
    "fiebre_alta": ["tomar antipiréticos", "consultar a un médico"],
    "dolor_garganta": ["gargarismos con agua tibia y sal", "beber líquidos tibios"],
    # Agrega más síntomas y acciones correspondientes según sea necesario
}

# Función para la interacción con el usuario
def interactuar_con_usuario():
    print("Bienvenido al sistema experto de diagnóstico de enfermedades.")
    print("Por favor, introduce tus síntomas separados por comas (ej. dolor_cabeza, fiebre_alta, dolor_garganta):")
    sintomas_usuario = input().strip().split(",")

    recomendaciones = []
    for sintoma in sintomas_usuario:
        if sintoma.strip() in base_conocimiento:
            recomendaciones.extend(base_conocimiento[sintoma.strip()])

    if recomendaciones:
        print("\nRecomendaciones:")
        for recomendacion in recomendaciones:
            print("-", recomendacion)
    else:
        print("\nLo siento, no se encontraron recomendaciones para los síntomas proporcionados.")

# Ejecución del sistema
interactuar_con_usuario()

