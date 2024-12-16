from objeto import Objeto
from mochila import Mochila
from fcn_frac import knapsack_fraccional
from fcn_dp import knapsack_01
from clima import obtener_clima

def main():
    print("Bienvenido al optimizador de mochila para acampadas.")
    ciudad = input("Ingrese la ciudad de destino para consultar el clima: ")
    
    try:
        clima, temp = obtener_clima(ciudad)
        print(f"El clima en {ciudad} es {clima} con {temp}°C.")
    except Exception as e:
        print(f"No se pudo obtener el clima: {e}")
        return

    # Crear objetos de ejemplo
    objetos = [
        Objeto("Tienda", 5, 10, False),
        Objeto("Saco de dormir", 3, 7, False),
        Objeto("Cocina portátil", 4, 8, False),
        Objeto("Linterna", 1, 2, True),
        Objeto("Botiquín", 2, 5, True),
    ]

    capacidad = int(input("Ingrese la capacidad de la mochila (kg): "))
    mochila = Mochila(capacidad)

    for obj in objetos:
        mochila.agregar_objeto(obj)

    print("\nSeleccione el algoritmo a usar:")
    print("1. Mochila 0/1 (Programación Dinámica)")
    print("2. Mochila Fraccional (Greedy)")
    opcion = int(input("Opción: "))

    if opcion == 1:
        beneficio, seleccion = knapsack_01(mochila)
    elif opcion == 2:
        beneficio, seleccion = knapsack_fraccional(mochila)
    else:
        print("Opción no válida.")
        return

    print(f"\nBeneficio total: {beneficio}")
    print("Objetos seleccionados:")
    for obj in seleccion:
        print(obj)

if __name__ == "__main__":
    main()
