class PlatoTipico:
    def __init__(self, nombre, descripcion, region, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.region = region
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.region} - ${self.precio}"