# --- Inicio del Programa ---
print("="*40)
print("🌡️ CONVERSOR DE TEMPERATURA 🌡️".center(40))
print("="*40)

# Muestra el menú de escalas
print("\n--- Opciones de Escala ---")
print("1. Celsius")
print("2. Fahrenheit")
print("3. Kelvin")
print("4. Salir")
print("="*26)

try:
    opcion_origen = input("Selecciona la escala de origen (1-3): ")
    if opcion_origen == '4':
        print("\n¡Gracias por usar el conversor! 👋")
    else:
        opcion_destino = input("Selecciona la escala de destino (1-3): ")
        if opcion_destino == '4':
            print("\n¡Gracias por usar el conversor! 👋")
        elif opcion_origen == opcion_destino:
            print("Error: La escala de origen y destino no pueden ser la misma.")
        else:
            valor_origen = float(input("Ingresa la temperatura a convertir: "))
            
            # Lógica de la conversión
            if opcion_origen == '1': # De Celsius
                if opcion_destino == '2':
                    resultado = (valor_origen * 9/5) + 32
                    print(f"{valor_origen}°C es igual a {resultado:.2f}°F")
                elif opcion_destino == '3':
                    resultado = valor_origen + 273.15
                    print(f"{valor_origen}°C es igual a {resultado:.2f}K")
            
            elif opcion_origen == '2': # De Fahrenheit
                if opcion_destino == '1':
                    resultado = (valor_origen - 32) * 5/9
                    print(f"{valor_origen}°F es igual a {resultado:.2f}°C")
                elif opcion_destino == '3':
                    resultado = (valor_origen - 32) * 5/9 + 273.15
                    print(f"{valor_origen}°F es igual a {resultado:.2f}K")
                    
            elif opcion_origen == '3': # De Kelvin
                if opcion_destino == '1':
                    resultado = valor_origen - 273.15
                    print(f"{valor_origen}K es igual a {resultado:.2f}°C")
                elif opcion_destino == '2':
                    resultado = (valor_origen - 273.15) * 9/5 + 32
                    print(f"{valor_origen}K es igual a {resultado:.2f}°F")
            
            else:
                print("Opción no válida. Por favor, selecciona del 1 al 4.")
                
except ValueError:
    print("Entrada inválida. Por favor, ingresa solo números.")

print("\n--- El programa ha finalizado. ---")