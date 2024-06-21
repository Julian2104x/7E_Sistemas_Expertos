import sqlite3
import sys  # Importamos el módulo sys para poder salir del programa

def conectar_bd():
    try:
        conn = sqlite3.connect('PLC_DATABASE.db')
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def hacer_pregunta(pregunta):
    while True:
        respuesta = input(pregunta + " (si/no): ").strip().lower()
        if respuesta in ["si", "no"]:
            return respuesta == "si"
        else:
            print("Por favor, responde 'si' o 'no'.")

def seleccionar_plc():
    while True:
        conn = conectar_bd()
        if conn is None:
            print("No se pudo conectar a la base de datos.")
            return

        cursor = conn.cursor()
        
        if hacer_pregunta("¿Necesitas 8 entradas digitales?"):
            entradas = 8
        elif hacer_pregunta("¿Necesitas 16 entradas digitales?"):
            entradas = 16
        else:
            print("No se especificó la cantidad exacta de entradas requeridas.")
            conn.close()
            continue
        
        if hacer_pregunta("¿Necesitas 4 salidas digitales?"):
            salidas = 4
        elif hacer_pregunta("¿Necesitas 12 salidas digitales?"):
            salidas = 12
        else:
            print("No se especificó la cantidad exacta de salidas requeridas.")
            conn.close()
            continue
        
        if hacer_pregunta("¿Necesitas salidas a relevador?"):
            tipo_salidas = 'RELEVADOR'
        elif hacer_pregunta("¿Necesitas salidas a transistor NPN?"):
            tipo_salidas = 'TRANSISTOR NPN'
        elif hacer_pregunta("¿Necesitas salidas a transistor PNP?"):
            tipo_salidas = 'TRANSISTOR PNP'
        else:
            print("No se especificó el tipo de salidas requerido.")
            conn.close()
            continue
        
        try:
            cursor.execute('''
                SELECT MODELO FROM PLC_SA2 
                WHERE ENTRADAS >= ? AND SALIDAS >= ? AND TIPO = ?
            ''', (entradas, salidas, tipo_salidas))
            
            resultado = cursor.fetchone()
            conn.close()
            
            if resultado:
                print(f"El modelo recomendado es {resultado[0]}")
            else:
                print("No hay modelos que cumplan con esos requisitos.")
        except sqlite3.Error as e:
            print(f"Error al realizar la consulta: {e}")
        
        reiniciar = hacer_pregunta("¿Deseas reiniciar para hacer otra consulta?")
        if not reiniciar:
            print("Gracias por usar el sistema experto.")
            sys.exit()  # Salimos del programa

# Ejecución del sistema experto
seleccionar_plc()
