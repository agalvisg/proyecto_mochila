def knapsack_01(mochila):
    """
    Algoritmo dinámico para resolver el problema de la mochila 0/1.
    :param mochila: Instancia de la clase Mochila.
    :return: Beneficio total y objetos seleccionados
    """

    n = len(mochila.objetos)
    capacidad = mochila.capacidad

    dp = [[0] * (capacidad + 1) for _ in range (n + 1)]

    for i in range(1, n + 1):
        for w in range (1, capacidad + 1):
            peso_obj = mochila.objetos[i - 1].peso
            valor_obj = mochila.objetos[i - 1].importancia
            if peso_obj <=w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - peso_obj] + valor_obj)
            else:
                dp[i][w] = dp[i - 1][w]
            

    # Reconstruir la solución
    w = capacidad
    seleccionados = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            seleccionados.append(mochila.objetos[i - 1])
            w -= mochila.objetos[i - 1].peso

    return dp[n][capacidad], seleccionados 