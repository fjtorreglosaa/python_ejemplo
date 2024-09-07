from typing import List
from utilidades.coordenadas import Coordenadas

class Velocidad:
    def __init__(self, coordenadas: List[Coordenadas]):
        self.coordenadas = coordenadas
    
    @staticmethod    
    def obtener_velocidades(coordenadas: List[Coordenadas], caudal: float) -> List[float]:
        
        velocidades = []
        
        for coordenada in coordenadas:
            area = coordenada.y * coordenada.y
            velocidad = caudal / area
            velocidades.append(velocidad)
            
        return velocidades