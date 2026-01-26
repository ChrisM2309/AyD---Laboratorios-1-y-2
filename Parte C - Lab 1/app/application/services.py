from datetime import datetime
from app.domain.errors import ReglaNegocioError

# Servicio de reservas 
class ReservaService:
    # Inicializar el sistema de reserva 
    def __init__(self, reserva_repo):
        self.reserva_repo = reserva_repo

    #  funcion que crea una nueva reserva
    def crear_reserva(self, estudiante_id, tutor_id, fecha_hora: datetime):
        # Regla de negocio, fecha es pasada 
        if fecha_hora < datetime.now():
            raise ReglaNegocioError("No se permite hacer una reserva en el pasado")

        # Regla de negocio, el tutor esta disponible
        if self.reserva_repo.existe_reserva(tutor_id=tutor_id, fecha_hora=fecha_hora):
            raise ReglaNegocioError("El tutor indicado ya tiene una reserva en ese horario")

        # si todo esta bien, creamos la reserva
        return self.reserva_repo.crear(estudiante_id, tutor_id, fecha_hora)
