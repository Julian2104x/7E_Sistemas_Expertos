# Función para verificar la coherencia de las reglas
def verificar_coherencia(reglas):
    for regla in reglas:
        for otra_regla in reglas:
            if regla != otra_regla:
                if regla[0] == otra_regla[0]:  # Verifica si las reglas tienen la misma premisa
                    print(f"Advertencia: Las reglas '{regla}' y '{otra_regla}' tienen la misma premisa.")

# Ejemplo de uso
reglas_ejemplo = [
    ("Si es día de semana, entonces trabajar."),
    ("Si es día de semana, entonces estudiar."),
    ("Si es fin de semana, entonces descansar.")
]

verificar_coherencia(reglas_ejemplo)
