from datetime import datetime, timedelta
import pytest
from app.application.services import ReservaService
from app.infrastructure.repositories import ReservaRepoMemoria
from app.domain.errors import ReglaNegocioError

# Test para probar que no se pueda reservar en el pasado
def test_no_reservar_en_pasado():
    s = ReservaService(ReservaRepoMemoria()) # crear servicio 
    with pytest.raises(ReglaNegocioError): 
        s.crear_reserva("e1", "t1", datetime.now() - timedelta(days=1)) # crear una reserva ayer 

# Test para probar que no se dupliquen reservas del mismo tutor
def test_no_doble_reserva_mismo_tutor_misma_hora():
    repo = ReservaRepoMemoria() #acceder repo
    s = ReservaService(repo)
    dt = datetime.now() + timedelta(days=1)
    s.crear_reserva("e1", "t1", dt) # crear primera reserva 
    with pytest.raises(ReglaNegocioError):
        s.crear_reserva("e2", "t1", dt) #crear segunda reserva con mismos valores 
