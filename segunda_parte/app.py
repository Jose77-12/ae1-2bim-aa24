import tkinter as tk
from controllers.main_controller import MainController
from models.plato_model import PlatoTipico
from views.main_view import MainView

if __name__ == "__main__":
    root = tk.Tk()
    
    view = MainView(root)
    app = MainController(PlatoTipico, view)
    app.run()
