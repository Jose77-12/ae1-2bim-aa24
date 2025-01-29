import tkinter as tk
from tkinter import ttk
from models.plato_model import PlatoTipico


class MainView:
    def __init__(self, root):
        self.root = root
        self.root.title("Platos Típicos de Ecuador")

        self.tree = ttk.Treeview(root, columns=(
            "Nombre", "Descripción", "Región", "Precio"), show='headings')
        self.tree.heading("Nombre", text="Nombre")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.heading("Región", text="Región")
        self.tree.heading("Precio", text="Precio")
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(
            root, text="Agregar Plato", command=self.add_plato)
        self.add_button.pack(side=tk.LEFT)

        self.edit_button = tk.Button(
            root, text="Editar Plato", command=self.edit_plato)
        self.edit_button.pack(side=tk.LEFT)

        self.delete_button = tk.Button(
            root, text="Eliminar Plato", command=self.delete_plato)
        self.delete_button.pack(side=tk.LEFT)

    def add_plato(self):
        # Lógica para agregar un plato
        def submit():
            nombre = nombre_entry.get()
            descripcion = descripcion_entry.get()
            region = region_entry.get()
            precio = precio_entry.get()
            self.insert_plato(PlatoTipico(nombre, descripcion, region, precio))
            add_window.destroy()

        add_window = tk.Toplevel(self.root)
        add_window.title("Agregar Plato")

        tk.Label(add_window, text="Nombre").grid(row=0, column=0)
        nombre_entry = tk.Entry(add_window)
        nombre_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Descripción").grid(row=1, column=0)
        descripcion_entry = tk.Entry(add_window)
        descripcion_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Región").grid(row=2, column=0)
        region_entry = tk.Entry(add_window)
        region_entry.grid(row=2, column=1)

        tk.Label(add_window, text="Precio").grid(row=3, column=0)
        precio_entry = tk.Entry(add_window)
        precio_entry.grid(row=3, column=1)

        submit_button = tk.Button(add_window, text="Agregar", command=submit)
        submit_button.grid(row=4, columnspan=2)

    def edit_plato(self):
        selected_item = self.tree.selection()
        if not selected_item:
            return

        def submit():
            nombre = nombre_entry.get()
            descripcion = descripcion_entry.get()
            region = region_entry.get()
            precio = precio_entry.get()
            self.tree.item(selected_item, values=(
                nombre, descripcion, region, precio))
            edit_window.destroy()

        item_values = self.tree.item(selected_item, "values")

        edit_window = tk.Toplevel(self.root)
        edit_window.title("Editar Plato")

        tk.Label(edit_window, text="Nombre").grid(row=0, column=0)
        nombre_entry = tk.Entry(edit_window)
        nombre_entry.grid(row=0, column=1)
        nombre_entry.insert(0, item_values[0])

        tk.Label(edit_window, text="Descripción").grid(row=1, column=0)
        descripcion_entry = tk.Entry(edit_window)
        descripcion_entry.grid(row=1, column=1)
        descripcion_entry.insert(0, item_values[1])

        tk.Label(edit_window, text="Región").grid(row=2, column=0)
        region_entry = tk.Entry(edit_window)
        region_entry.grid(row=2, column=1)
        region_entry.insert(0, item_values[2])

        tk.Label(edit_window, text="Precio").grid(row=3, column=0)
        precio_entry = tk.Entry(edit_window)
        precio_entry.grid(row=3, column=1)
        precio_entry.insert(0, item_values[3])

        submit_button = tk.Button(edit_window, text="Guardar", command=submit)
        submit_button.grid(row=4, columnspan=2)

    def delete_plato(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)

    def insert_plato(self, plato: PlatoTipico):
        self.tree.insert("", "end", values=(
            plato.nombre, plato.descripcion, plato.region, plato.precio))
