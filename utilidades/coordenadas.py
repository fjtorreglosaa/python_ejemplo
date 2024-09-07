class Coordenadas:
    def __init__(self, x: float, y: float):
        self.x = x / 1000 # Convertir en m
        self.y = y / 1000 # Convertir en m

    def __str__(self):
        return f"({self.x}, {self.y})"