def modus_ponens(condicion, consecuencia):
    if condicion == True:
        return consecuencia

# Ejemplo de uso de Modus Ponens
def ejemplo_modus_ponens():
    condicion = False
    consecuencia = "La calle está mojada"
    
    resultado = modus_ponens(condicion, consecuencia)
    
    if resultado:
        print("Se ha concluido que está lloviendo, por lo tanto:", resultado)
    else:
        print("No se puede inferir nada.")

ejemplo_modus_ponens()
