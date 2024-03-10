def modus_tollens(p, q, not_q):
    if q == True:  # Si la consecuencia es verdadera
        return p  # Entonces la condición es verdadera
    else:
        return not_q # Si la consecuencia es falsa

# Ejemplo de uso
p = True  # Si llueve (Condición)
q = False # El suelo está mojado (Consecuencia)
not_q = False  # El suelo no está mojado

resultado = modus_tollens(p, q, not_q)
if resultado is not None:
    print("¿Está lloviendo?:", resultado)
