def registrar_venta():

    print("\n--- Nuevo Registro de Venta ---")


    #SOLICITO INFORMACION DE LA VENTA

    producto_id = int(input("Ingrese el identificador del producto (número entero): "))
    producto_categoria = input("Ingrese la categoría del producto: ")
    producto_precio = float(input("Precio unitario del producto (en formato decimal): "))
    unidades_vendidas = int(input("Cantidad vendida: "))
    fecha = input("Fecha de la venta (dd-mm-aaaa): ")


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







#CUARTO BLOQUE (calculo PROMEDIO)
#para la funcion los datos ingresados tienen que estar en una lista
def promedio(ingresos):
    total_ingresos = 0
    num_ingresos = len(ingresos)

    for i in range(num_ingresos):
        ingreso = ingresos[i] 
        total_ingresos += ingreso 

    if num_ingresos > 0:
        promedio = total_ingresos / num_ingresos
    else:
        promedio = 0

    return promedio

