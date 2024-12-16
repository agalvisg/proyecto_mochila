class Objeto:
    def __init__(self, nombre, peso, importancia, fraccionable):
        """
        self.nombre = nombre -> Nombre del objeto
        self.peso = peso -> Peso del objeto o volumen según lo determinado por el usuario
        self.importancia = importancia -> Importancia del objeto
        self.fraccionable = fraccionable   -> Si el objeto es fraccionable o no
         
        """

        self.nombre = nombre
        self.peso = peso
        self.importancia = importancia
        self.fraccionable = fraccionable

    def __repr__(self):
        return f"{self.nombre} (Peso: {self.peso} Importancia: {self.importancia} Fraccionable: {self.fraccionable})"