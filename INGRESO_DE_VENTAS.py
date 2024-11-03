
 def registrar_venta():
    print("\n--- Nuevo Registro de Venta ---")

    # SOLICITO INFORMACION DE LA VENTA
    producto_id = int(input("Ingrese el identificador del producto (número entero): "))
    while producto_id <= 0:
        print("El ID del producto debe ser un número mayor a cero.")
        producto_id = int(input("Ingrese el identificador del producto (número entero): "))

    producto_categoria = input("Ingrese la categoría del producto: ")
    while producto_categoria == "":
        print("La categoría no puede estar vacía.")
        producto_categoria = input("Ingrese la categoría del producto: ")

    producto_precio = float(input("Precio unitario del producto (en formato decimal): "))
    while producto_precio <= 0:
        print("El precio debe ser un valor positivo.")
        producto_precio = float(input("Precio unitario del producto (en formato decimal): "))

    unidades_vendidas = int(input("Cantidad vendida: "))
    while unidades_vendidas <= 0:
        print("La cantidad vendida debe ser un número mayor a cero.")
        unidades_vendidas = int(input("Cantidad vendida: "))

     
    fecha = input("Fecha de la venta (dd-mm-aaaa): ")
    fecha_valida = 0

while fecha_valida == 0:
    fecha = input("Ingresa la fecha en formato mm-dd-aaaa: ")
    
    # Comprobar que la longitud sea 10 y que los guiones estén en las posiciones correctas
    if len(fecha) == 10 and fecha[2] == '-' and fecha[5] == '-':
        
        mes = fecha[:2]
        dia = fecha[3:5]
        anio = fecha[6:]

        # Verificar que cada carácter sea un número y que esté dentro de rangos válidos
        if ('0' <= mes[0] <= '1' and '0' <= mes[1] <= '9' and 
            '0' <= dia[0] <= '3' and '0' <= dia[1] <= '9' and 
            '1' <= anio[0] <= '9' and '0' <= anio[1] <= '9' and 
            '0' <= anio[2] <= '9' and '0' <= anio[3] <= '9'):
            
            # Validar mes
            if mes == '01' or mes == '03' or mes == '05' or mes == '07' or mes == '08' or mes == '10' or mes == '12':
                # Meses con 31 días
                dias_maximos = 31
            elif mes == '04' or mes == '06' or mes == '09' or mes == '11':
                # Meses con 30 días
                dias_maximos = 30
            elif mes == '02':
                # Febrero, considerar un año bisiesto simple
                if (anio[0] == '2' and anio[1] == '0') or (anio[0] == '1' and anio[1] == '9'):
                    dias_maximos = 29  # Bisiesto
                else:
                    dias_maximos = 28  # No bisiesto
            else:
                dias_maximos = 0  # Mes inválido

            # Validar día
            dia_numero = (dia[0] == '0') * 10 + (dia[1] == '0')
            dia_numero += (dia[0] == '1') * 10 + (dia[1] == '1') + (dia[1] == '2') + (dia[1] == '3')
            dia_numero += (dia[0] == '2') * 10 + (dia[1] == '4') + (dia[1] == '5') + (dia[1] == '6') + (dia[1] == '7') + (dia[1] == '8') + (dia[1] == '9')

            # Verificar que el día sea válido
            if 1 <= dia_numero <= dias_maximos:
                fecha_valida = 1
                print("Fecha ingresada correctamente:", fecha)
            else:
                print("Error: día fuera de rango.")
        else:
            print("Error: mes, día o año deben ser números.")
    else:
        print("Error: formato incorrecto. Usa mm-dd-aaaa.")
  


    #LISTA CON LOS DATOS DE LA VENTA
    nueva_venta = [producto_id, producto_categoria, producto_precio, unidades_vendidas, fecha]
    print("Venta registrada correctamente.\n")
    return nueva_venta










# SEGUNDO BLOQUE

datos_ventas = []


# SE SOLICITA CANTIDAD DE VENTAS 

total_ventas = int(input("¿Cuántas ventas desea registrar en total? "))
print("\nIniciando el registro de ventas...\n")

# SE AGREGA CADA VENTA  LA LISTA

for i in range(total_ventas):
    datos_ventas.append(registrar_venta())

print("Datos de ventas ingresados exitosamente:", datos_ventas)
