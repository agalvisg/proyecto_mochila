import tkinter as tk
from tkinter import messagebox, ttk
from objeto import Objeto
from mochila import Mochila
from fcn_frac import knapsack_fraccional
from fcn_dp import knapsack_01
from clima import obtener_clima

class MochilaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Optimizador de Mochila para Acampadas")
        self.root.geometry("600x500")

        # Variables
        self.objetos = []
        self.mochila = None
        self.capacidad = tk.StringVar()
        self.ciudad = tk.StringVar()

        # Etiqueta de título
        tk.Label(root, text="Optimizador de Mochila", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Entrada para la ciudad
        tk.Label(root, text="Ciudad de destino:").pack()
        self.ciudad_entry = tk.Entry(root, textvariable=self.ciudad, width=30)
        self.ciudad_entry.pack()

        tk.Button(root, text="Consultar Clima", command=self.consultar_clima).pack(pady=5)
        self.clima_label = tk.Label(root, text="", fg="blue")
        self.clima_label.pack()

        # Capacidad de la mochila
        tk.Label(root, text="Capacidad de la mochila (kg):").pack()
        self.capacidad_entry = tk.Entry(root, textvariable=self.capacidad, width=10)
        self.capacidad_entry.pack()

        # Sección para agregar objetos
        tk.Label(root, text="Agregar Objeto:").pack(pady=5)
        self.objeto_nombre = tk.Entry(root, width=20)
        self.objeto_nombre.insert(0, "Nombre")
        self.objeto_nombre.pack()

        self.objeto_peso = tk.Entry(root, width=10)
        self.objeto_peso.insert(0, "Peso")
        self.objeto_peso.pack()

        self.objeto_valor = tk.Entry(root, width=10)
        self.objeto_valor.insert(0, "Valor")
        self.objeto_valor.pack()

        self.divisible_var = tk.BooleanVar()
        tk.Checkbutton(root, text="¿Es divisible?", variable=self.divisible_var).pack()

        tk.Button(root, text="Agregar Objeto", command=self.agregar_objeto).pack(pady=5)

        # Mostrar lista de objetos
        self.lista_objetos = tk.Listbox(root, width=50, height=10)
        self.lista_objetos.pack(pady=10)

        # Botones para ejecutar algoritmos
        tk.Label(root, text="Selecciona un algoritmo:").pack(pady=5)
        tk.Button(root, text="Mochila 0/1 (Dinámica)", command=lambda: self.ejecutar_algoritmo("dp")).pack()
        tk.Button(root, text="Mochila Fraccional (Greedy)", command=lambda: self.ejecutar_algoritmo("greedy")).pack()

        # Resultado
        self.resultado_label = tk.Label(root, text="", fg="green")
        self.resultado_label.pack(pady=10)

    def consultar_clima(self):
        ciudad = self.ciudad.get()
        try:
            clima, temp = obtener_clima(ciudad)
            self.clima_label.config(text=f"Clima en {ciudad}: {clima}, {temp}°C")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo obtener el clima: {e}")

    def agregar_objeto(self):
        try:
            nombre = self.objeto_nombre.get()
            peso = float(self.objeto_peso.get())
            valor = int(self.objeto_valor.get())
            divisible = self.divisible_var.get()

            obj = Objeto(nombre, peso, valor, divisible)
            self.objetos.append(obj)
            self.lista_objetos.insert(tk.END, f"{nombre} - Peso: {peso} kg, Valor (1-10): {valor}, Divisible: {divisible}")
            self.objeto_nombre.delete(0, tk.END)
            self.objeto_peso.delete(0, tk.END)
            self.objeto_valor.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores válidos para el objeto.")

    def ejecutar_algoritmo(self, tipo):
        try:
            capacidad = int(self.capacidad.get())
            self.mochila = Mochila(capacidad)

            for obj in self.objetos:
                self.mochila.agregar_objeto(obj)

            if tipo == "dp":
                beneficio, seleccion = knapsack_01(self.mochila)
            else:
                beneficio, seleccion = knapsack_fraccional(self.mochila)

            resultado = f"Beneficio total: {beneficio}\nObjetos seleccionados:\n"
            for obj in seleccion:
                resultado += f"- {obj}\n"

            self.resultado_label.config(text=resultado)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese una capacidad válida.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MochilaApp(root)
    root.mainloop()
