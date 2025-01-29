class PlatoTipico:
    def __init__(self, nombre, descripcion, ingredientes, region, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.ingredientes = ingredientes
        self.region = region
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.ingredientes} - {self.region} - ${self.precio}"