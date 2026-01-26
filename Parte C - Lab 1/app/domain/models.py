from dataclasses import dataclass
from datetime import datetime


# Clase para las reservas de tutorias
@dataclass(frozen=True)
class Reserva:
    id: str
    estudiante_id: str
    tutor_id: str
    fecha_hora: datetime
    estado: str  # Tiene estados segun el enum 
