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

# Ejemplo de uso
sintomas_paciente = ["sintoma_3", "sintoma_2", "sintoma_4"]
enfermedades_diagnosticadas = motor_inferencia(sintomas_paciente)

print("Enfermedades diagnosticadas basadas en los síntomas del paciente:")
for enfermedad in enfermedades_diagnosticadas:
    print("-", enfermedad)
