import uuid
from app.domain.models import Reserva

# Clase de repositorio de memoria 
class ReservaRepoMemoria:
    # Al inicio, la lista esta vacia 
    def __init__(self):
        self._items = []

    # Verificar si ya hay una reserva con ese tutor y hora
    def existe_reserva(self, tutor_id, fecha_hora):
        return any(
            r.tutor_id == tutor_id and r.fecha_hora == fecha_hora and r.estado != "CANCELADA"
            for r in self._items
        )

    # Crea y guardar la reserva en memoria 
    def crear(self, estudiante_id, tutor_id, fecha_hora):
        # crear objeto reserva
        r = Reserva(
            id=str(uuid.uuid4()),
            estudiante_id=estudiante_id,
            tutor_id=tutor_id,
            fecha_hora=fecha_hora,
            estado="CREADA",
        )
        # lo agregamos a la lista
        self._items.append(r)
        return r
