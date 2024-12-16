class Mochila:
    def __init__(self, capacidad, criterio="peso"):
        """
        Clase para gestionar la mochila.
        :param capacidad: Capacidad de la mochila (en peso, volumen o cantidad de objetos)
        :param criterio: Criterio principal (peso, volumen, o cantidad de objetos)
        """
        self.capacidad = capacidad
        self.criterio = criterio
        self.objetos = []

    def agregar_objeto(self, objeto):
        """
        Agrega un objeto a la mochila.
        :param objeto: Instancia de la clase Objeto
        """
        self.objetos.append(objeto)

    def __repr__(self):
        return f"Mochila (Capacidad: {self.capacidad}, Criterio: {self.criterio}, Objetos: {len(self.objetos)})"
