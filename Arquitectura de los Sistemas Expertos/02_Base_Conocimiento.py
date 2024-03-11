# Definición de la base de conocimiento
base_conocimiento = {
    "sintoma_1": ["posible_enfermedad_1", "posible_enfermedad_2"],
    "sintoma_2": ["posible_enfermedad_2", "posible_enfermedad_3"],
    "sintoma_3": ["posible_enfermedad_1", "posible_enfermedad_3"],
    # Agrega más síntomas y enfermedades correspondientes según sea necesario
}

# Función para consultar la base de conocimiento
def consultar_base_conocimiento(sintomas):
    enfermedades_posibles = []
    for sintoma in sintomas:
        if sintoma in base_conocimiento:
            enfermedades_posibles.extend(base_conocimiento[sintoma])

    # Eliminar duplicados y devolver resultados únicos
    return list(set(enfermedades_posibles))

# Ejemplo de uso
sintomas_paciente = ["sintoma_1", "sintoma_3"]
enfermedades_diagnosticadas = consultar_base_conocimiento(sintomas_paciente)

print("Basado en los síntomas proporcionados, las posibles enfermedades podrían ser:")
for enfermedad in enfermedades_diagnosticadas:
    print("-", enfermedad)
