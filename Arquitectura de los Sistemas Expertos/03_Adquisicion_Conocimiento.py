# Definición de la base de conocimiento inicial
base_conocimiento = {}

# Función para agregar nuevas reglas a la base de conocimiento
def agregar_regla(regla, conocimiento):
    if conocimiento in base_conocimiento:
        base_conocimiento[conocimiento].append(regla)
    else:
        base_conocimiento[conocimiento] = [regla]

# Simulación de interacción con el experto humano
def interaccion_experto():
    print("Bienvenido al subsistema de adquisición de conocimiento.")
    print("Por favor, introduzca una nueva regla de inferencia:")
    nueva_regla = input("Regla: ")
    conocimiento_relacionado = input("Conocimiento relacionado: ")

    agregar_regla(nueva_regla, conocimiento_relacionado)
    print("La regla ha sido agregada correctamente a la base de conocimiento.")

# Ejemplo de uso
interaccion_experto()

# Imprimir la base de conocimiento actualizada
print("\nBase de conocimiento actualizada:")
for conocimiento, reglas in base_conocimiento.items():
    print("- Conocimiento:", conocimiento)
    print("  Reglas:", reglas)



