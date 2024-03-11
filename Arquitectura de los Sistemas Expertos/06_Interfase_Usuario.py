# Base de conocimiento: Reglas de producción
base_conocimiento = {
    "Regla 1": {
        "premisas": ["sintoma_1", "sintoma_2"],
        "conclusion": "enfermedad_1"
    },
    "Regla 2": {
        "premisas": ["sintoma_3", "sintoma_4"],
        "conclusion": "enfermedad_2"
    },
    # Agrega más reglas según sea necesario
}

# Función para el motor de inferencia
def motor_inferencia(sintomas):
    enfermedades = []

    # Iterar sobre cada regla en la base de conocimiento
    for regla, info_regla in base_conocimiento.items():
        premisas = info_regla["premisas"]
        conclusion = info_regla["conclusion"]

        # Verificar si todas las premisas de la regla están presentes en los síntomas del paciente
        if all(premisa in sintomas for premisa in premisas):
            enfermedades.append(conclusion)

    return enfermedades

# Interfaz de usuario
def interfaz_usuario():
    print("Bienvenido al sistema experto de diagnóstico de enfermedades.")
    print("Por favor, ingrese los síntomas que experimenta el paciente, separados por comas:")
    sintomas_input = input().strip().split(",")

    enfermedades_diagnosticadas = motor_inferencia(sintomas_input)

    if enfermedades_diagnosticadas:
        print("\nEnfermedades diagnosticadas basadas en los síntomas proporcionados:")
        for enfermedad in enfermedades_diagnosticadas:
            print("-", enfermedad)
    else:
        print("\nLo siento, no se encontraron enfermedades diagnosticadas para los síntomas proporcionados.")

# Ejecución de la interfaz de usuario
interfaz_usuario()
