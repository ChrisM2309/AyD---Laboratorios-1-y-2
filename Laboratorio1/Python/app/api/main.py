from fastapi import FastAPI, HTTPException
from datetime import datetime
from app.application.services import ReservaService
from app.infrastructure.repositories import ReservaRepoMemoria
from app.domain.errors import ReglaNegocioError

# Crear la api 
app = FastAPI(title="Tutorias API")

# Guardar en repo y servicio 
repo = ReservaRepoMemoria()
service = ReservaService(repo)

# Post de nuevas reservas, crear con estudiante, tutor y fecha 
@app.post("/reservas")
def crear_reserva(estudiante_id: str, tutor_id: str, fecha_hora: str):
    try:
        # convertimos el iso a fecha
        dt = datetime.fromisoformat(fecha_hora)
        # llamamos al servicio para crear la reserva
        r = service.crear_reserva(estudiante_id, tutor_id, dt)
        return {"id": r.id, "estado": r.estado} #devuelve la reserva 
    except ReglaNegocioError as e:
        # si hay error mandamos 400 
        raise HTTPException(status_code=400, detail=str(e)) #Mostrar si un problema en regla de negocio 
