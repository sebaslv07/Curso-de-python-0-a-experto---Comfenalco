while True:
    numero_tabla = int(input("Ingrese el numero de la tabla de multiplicar: "))

    limite = int(input("Ingrese hasta qué numero desea mostrar la tabla de multiplicar: "))

    print(f"Tabla de multiplicar del {numero_tabla} hasta el {limite}:")
    for i in range(1, limite + 1):
        resultado = numero_tabla * i
        print(f"{numero_tabla} x {i} = {resultado}")

    continuar = input("¿Desea continuar con el programa? (s/n): ").lower()
    if continuar != 's':
        confirmacion = input("¿Enserio desea salir del programa? (s/n): ").lower()
        if confirmacion == 's':
            print("Adios..... Gracias.....")
            break