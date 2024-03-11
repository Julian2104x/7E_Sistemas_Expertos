# Definición de acciones basadas en enfermedades
acciones_por_enfermedad = {
    "enfermedad_1": ["Recetar medicamento A", "Recomendar reposo"],
    "enfermedad_2": ["Recetar medicamento B", "Recomendar ejercicios"],
    # Agregar más acciones según sea necesario
}

# Función para ejecutar órdenes basadas en enfermedades diagnosticadas
def ejecutar_ordenes(enfermedades):
    acciones_ejecutadas = []

    for enfermedad in enfermedades:
        if enfermedad in acciones_por_enfermedad:
            acciones_ejecutadas.extend(acciones_por_enfermedad[enfermedad])

    return acciones_ejecutadas

# Ejemplo de uso
enfermedades_diagnosticadas = ["enfermedad_1", "enfermedad_2"]
ordenes_ejecutadas = ejecutar_ordenes(enfermedades_diagnosticadas)

print("Acciones ejecutadas basadas en las enfermedades diagnosticadas:")
for accion in ordenes_ejecutadas:
    print("-", accion)
