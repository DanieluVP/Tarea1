def obtener_estados_equivalentes(num_estados, alfabeto, estados_finales, transiciones):
    # Diccionario para marcar si un par de estados es equivalente (True) o no (False)
    pares = {}
    for i in range(num_estados):
        for j in range(i + 1, num_estados):
            pares[(i, j)] = True  # Al inicio asumimos que todos son equivalentes

    # Paso 1: Marcar como no equivalentes los pares donde uno es final y el otro no
    for (i, j) in pares.keys():
        if (i in estados_finales) ^ (j in estados_finales):
            pares[(i, j)] = False

    # Paso 2: Refinar la tabla hasta que no haya cambios
    cambio = True
    while cambio:
        cambio = False
        for (i, j) in pares.keys():
            if pares[(i, j)]:  # Solo revisamos los que aún creemos equivalentes
                for simbolo_idx in range(len(alfabeto)):
                    sig_i = transiciones[i][simbolo_idx]
                    sig_j = transiciones[j][simbolo_idx]

                    if sig_i != sig_j:
                        a, b = sorted((sig_i, sig_j))
                        if a != b and (a, b) in pares and not pares[(a, b)]:
                            pares[(i, j)] = False
                            cambio = True
                            break

    # Paso 3: Crear la lista de pares equivalentes en formato (i, j)
    equivalentes = [f"({i}, {j})" for (i, j), eq in pares.items() if eq]
    return " ".join(equivalentes)


# ----------- PROGRAMA PRINCIPAL -----------
casos = int(input("Ingrese el número de casos: "))

for caso in range(casos):
    print(f"\n--- Caso {caso + 1} ---")
    num_estados = int(input("Cantidad de estados: "))
    alfabeto = input("Alfabeto (separado por espacios): ").split()
    estados_finales = list(map(int, input("Estados finales (separados por espacios): ").split()))

    print("Ingrese la tabla de transiciones (una línea por estado):")
    transiciones = []
    for i in range(num_estados):
        fila = list(map(int, input(f"Estado {i}: ").split()))
        transiciones.append(fila)

    resultado = obtener_estados_equivalentes(num_estados, alfabeto, estados_finales, transiciones)
    print("Estados equivalentes:", resultado)
