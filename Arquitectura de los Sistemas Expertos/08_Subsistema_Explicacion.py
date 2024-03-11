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

# Función para explicar la inferencia realizada por el sistema experto
def explicar_inferencia(sintomas, enfermedades_diagnosticadas):
    explicaciones = []

    for enfermedad in enfermedades_diagnosticadas:
        explicacion = f"El paciente presenta los siguientes síntomas: {', '.join(sintomas)}."
        explicacion += f"\nSe ha diagnosticado la enfermedad '{enfermedad}' basándose en las siguientes reglas:"

        for regla, info_regla in base_conocimiento.items():
            premisas = info_regla["premisas"]
            conclusion = info_regla["conclusion"]

            if conclusion == enfermedad:
                explicacion += f"\n- {regla}: Si {' y '.join(premisas)}, entonces '{enfermedad}'."

        explicaciones.append(explicacion)

    return explicaciones

# Ejemplo de uso
sintomas_paciente = ["sintoma_1", "sintoma_2"]
enfermedades_diagnosticadas = ["enfermedad_1"]

explicaciones = explicar_inferencia(sintomas_paciente, enfermedades_diagnosticadas)

print("Explicación de la inferencia realizada por el sistema experto:")
for explicacion in explicaciones:
    print(explicacion)
