import tkinter as tk
from models.plato_model import PlatoTipico
from views.main_view import MainView


class MainController:
    def __init__(self, model: PlatoTipico, view: MainView):
        self.model = model
        self.view = view
        self.view.add_plato = self.add_plato
        self.view.edit_plato = self.edit_plato
        self.view.delete_plato = self.delete_plato

    def load_dishes(self):
        dishes = self.model.get_all_dishes()
        self.view.display_dishes(dishes)

    def add_dish(self, nombre, descripcion, ingredientes, precio, region):
        self.model.add_dish(nombre, descripcion, ingredientes, precio, region)
        self.load_dishes()

    def edit_dish(self, dish_id, nombre, descripcion, ingredientes, precio, region):
        self.model.edit_dish(dish_id, nombre, descripcion,
                             ingredientes, precio, region)
        self.load_dishes()

    def delete_dish(self, dish_id):
        self.model.delete_dish(dish_id)
        self.load_dishes()

    def run(self):
        self.view.root.mainloop()

    def add_plato(self):
        self.view.add_plato()

    def edit_plato(self):
        self.view.edit_plato()

    def delete_plato(self):
        self.view.delete_plato()
