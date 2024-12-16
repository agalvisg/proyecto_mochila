def knapsack_fraccional(mochila):
    """
    Algoritmo greedy para resolver el problema de la mochila fraccional.
    :param mochila: Instancia de la clase Mochila.
    :return: Beneficio total y objetos seleccionados con posible fraccionamientos.
    """


#ordenar los objetos por importancia
    mochila.objetos.sort(key=lambda x: x.importancia, reverse=True)
    
    capacidad_restante = mochila.capacidad
    beneficio_total = 0
    seleccionados = []

    for obj in mochila.objetos:
        if capacidad_restante == 0:
            break

        if obj.peso <= capacidad_restante:
            seleccionados.append((obj,1))
            beneficio_total += obj.importancia
            capacidad_restante -= obj.peso

        elif obj.fraccionable:
            fraccion = capacidad_restante / obj.peso
            seleccionados.append((obj,fraccion))
            beneficio_total += fraccion * obj.importancia
            capacidad_restante = 0
    
    return beneficio_total, seleccionados
