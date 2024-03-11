# Base de conocimiento inicial
base_conocimiento = {
    "Regla 1": {
        "premisas": ["sintoma_1", "sintoma_2"],
        "conclusion": "enfermedad_1"
    },
    "Regla 2": {
        "premisas": ["sintoma_3", "sintoma_4"],
        "conclusion": "enfermedad_2"
    },
    # Agregar más reglas según sea necesario
}

# Función para el subsistema de aprendizaje
def sistema_aprendizaje(feedback_usuario):
    for regla, info_regla in feedback_usuario.items():
        if regla in base_conocimiento:
            premisas = info_regla["premisas"]
            conclusion = info_regla["conclusion"]

            # Actualizar la base de conocimiento con la retroalimentación del usuario
            base_conocimiento[regla] = {"premisas": premisas, "conclusion": conclusion}

# Ejemplo de uso
feedback_usuario = {
    "Regla 1": {
        "premisas": ["sintoma_3", "sintoma_4"],  # Nuevas premisas proporcionadas por el usuario
        "conclusion": "enfermedad_2"  # Nueva conclusión proporcionada por el usuario
    }
}

# Aplicar la retroalimentación del usuario al sistema de conocimiento
sistema_aprendizaje(feedback_usuario)

# Imprimir la base de conocimiento actualizada
print("Base de conocimiento actualizada:")
for regla, info_regla in base_conocimiento.items():
    print(f"{regla}: Si {info_regla['premisas']}, entonces {info_regla['conclusion']}")
