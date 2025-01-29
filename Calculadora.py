import logging
import pdb

# Configuración de logging
logging.basicConfig(filename="errores.log", level=logging.ERROR, format="%(asctime)s - %(levelname)s - %(message)s")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("No se puede dividir por cero")
        return a / b
    except ZeroDivisionError as e:
        logging.error(f"Error en la operacion dividir: {e}")
        return "Error: Division por cero"
    
def calculadora():
    while True:
        print("Calculadora Tolerante A Fallos")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion == "5":
            print("Saliendo de la calculadora")
            break

        try:
            a = float(input("Ingrese el primer numero: "))
            b = float(input("Ingrese el segundo numero: "))
        except ValueError as e:
            print("Error: Debe ingresar un numero")
            logging.error("Error de entrada, tipo de dato invalido")
            continue

        if opcion == '1':
            resultado = sumar(a, b)
        elif opcion == '2':
            resultado = restar(a, b)
        elif opcion == '3':
            resultado = multiplicar(a, b)
        elif opcion == '4':
            # Usamos pdb para depuracion si el usuario ingresa 0 como divisor
            if b == 0:
                print("Activando depuracion...")
                pdb.set_trace()
            resultado = dividir(a, b)
        else:
            print("Opcion no valida")
            continue
        
        print(f"Resultado: {resultado}")

if __name__ == "__main__":
    calculadora()
