#Lo primero que vamos a hacer es pedirle 2 numeros el importe y el entregado y cuando se los de se pasaran a centimos para tener un numero entero

importe = round(float(input("Importe (€): ")) * 100)
entregado = round(float(input("Entregado (€): ")) * 100)

#A lo siguiente necesita calcular el cambio con los dos numeros que le hemos dado antes

cambio = entregado - importe

#Ahora pasaremos el cambio a euros otra vez dividiendolo entre 100

print(f"Cambio total: {cambio / 100:.2f} €")

#Aqui tenemos una tabla de los valores en centimos

for valor, nombre in [(2000, "billete de 20 €"), (1000, "billete de 10 €"), (500, "billete de 5 €"),
                      (200, "moneda de 2 €"), (100, "moneda de 1 €"), (50, "moneda de 50 cént."),
                      (20, "moneda de 20 cént."), (10, "moneda de 10 cént."), (5, "moneda de 5 cént.")]:

#Aqui lo que hacemos es ver con que billetes o monedas repartimos el cambio gracias a la tabla anterior

    cantidad, cambio = divmod(cambio, valor)

#Gracias al if cantidad: nos dara solo los que tengan 1 o mas en el total

    if cantidad:
        print(f"{cantidad} x {nombre}")
