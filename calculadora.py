# --- Inicio del Programa ---
print("="*40)
print("✨ CALCULADORA DE UNA OPERACIÓN ✨".center(40))
print("="*40)

# Muestra el menú de opciones
print("\n--- Elige la operación que quieres realizar ---")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("="*46)

# Pide al usuario que elija una opción
opcion = input("Ingresa tu opción (1-4): ")

# Procesa la opción elegida
if opcion in ('1', '2', '3', '4'):
    try:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        
        if opcion == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif opcion == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif opcion == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif opcion == '4':
            if num2 == 0:
                print("Error: No se puede dividir por cero.")
            else:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
                
    except ValueError:
        print("Entrada inválida. Por favor, ingresa solo números.")
else:
    print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")

# El programa termina después de este punto
print("\n--- El programa ha finalizado. ---")

# --- Fin del Programa ---

#El programa inicia con un menú que permite al usuario elegir una operacion matematica basica,
#  le solicita dos numeros y realiza la opercion seleccionada.
# el programa finaliza mostrando el resultado de la opracion elegida