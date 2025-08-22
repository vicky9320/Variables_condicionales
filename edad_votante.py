# -*- coding: utf-8 -*-
# --- Inicio del Programa ---
print("="*40)
print("🗳️ VERIFICADOR DE EDAD PARA VOTAR 🗳️".center(40))
print("="*40)

# Solicitamos los datos del usuario
try:
    edad = int(input("\nPor favor, ingresa tu edad: "))
    # Guardamos la entrada original del país para el mensaje final
    pais_ingresado = input("Por favor, ingresa tu país de residencia (ej: Brasil, Cuba, Indonesia, Estados Unidos, Corea del Sur, Singapur .): ")
    pais = pais_ingresado.lower()

    # Usamos condicionales para verificar el país y la edad mínima
    if pais == "brasil":
        edad_requerida = 16
        if edad >= edad_requerida:
            print(f"\n¡Felicidades! 🎉 Con {edad} años, puedes votar en {pais_ingresado}.")
            if edad < 18:
                print("El voto es opcional para las personas de 16 y 17 años en Brasil.")
        else:
            print(f"\nLo siento. 😞 Con {edad} años, no puedes votar en {pais_ingresado}. La edad mínima es de {edad_requerida} años.")
            
    elif pais == "cuba":
        edad_requerida = 16
        if edad >= edad_requerida:
            print(f"\n¡Felicidades! 🎉 Con {edad} años, puedes votar en {pais_ingresado}.")
        else:
            print(f"\nLo siento. 😞 Con {edad} años, no puedes votar en {pais_ingresado}. La edad mínima es de {edad_requerida} años.")

    elif pais == "indonesia":
        edad_requerida = 17
        if edad >= edad_requerida:
            print(f"\n¡Felicidades! 🎉 Con {edad} años, puedes votar en {pais_ingresado}.")
        else:
            print(f"\nLo siento. 😞 Con {edad} años, no puedes votar en {pais_ingresado}. La edad mínima es de {edad_requerida} años.")

    elif pais == "estados unidos" or pais == "colombia":
        edad_requerida = 18
        if edad >= edad_requerida:
            print(f"\n¡Felicidades! 🎉 Con {edad} años, puedes votar en {pais_ingresado}.")
        else:
            print(f"\nLo siento. 😞 Con {edad} años, no puedes votar en {pais_ingresado}. La edad mínima es de {edad_requerida} años.")

    elif pais == "corea del sur":
        edad_requerida = 18
        if edad >= edad_requerida:
            print(f"\n¡Felicidades! 🎉 Con {edad} años, puedes votar en {pais_ingresado}.")
        else:
            print(f"\nLo siento. 😞 Con {edad} años, no puedes votar en {pais_ingresado}. La edad mínima es de {edad_requerida} años.")
            
    elif pais == "singapur":
        edad_requerida = 21
        if edad >= edad_requerida:
            print(f"\n¡Felicidades! 🎉 Con {edad} años, puedes votar en {pais_ingresado}.")
        else:
            print(f"\nLo siento. 😞 Con {edad} años, no puedes votar en {pais_ingresado}. La edad mínima es de {edad_requerida} años.")

    else:
        print("\nEl país ingresado no se encuentra en nuestra base de datos o no es válido.")

except ValueError:
    print("\nEntrada inválida. Por favor, ingresa un número para la edad.")