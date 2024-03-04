tiendas = []

while True:
    nombre = input("nombre de la tienda:")
    ganancia = int(input("Cantidad  de ganancia:"))
    tiendas.append([nombre, ganancia])

    opcion = input("¿Quires seguir? (s/n)")
    if opcion.lower() == "n":
        break

    ganancias_totales = sum(tienda[1] for tienda in tiendas)
    media_ganancias = ganancias_totales / len(tiendas)

    mayor_ganancia = max(tienda[1] for tienda in tiendas)
    indice_mayor_ganancia = tiendas.index([tienda[0] for tienda in tiendas if tienda[1] == mayor_ganancia][0])

    print(f"la media de ganancias es:{media_ganancias}")
    print(f"la tienda con mayor cantidad de venta es:{tiendas[indice_mayor_ganancia][0]}")