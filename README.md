# Laboratorio 1 y 2 – Sistema de Reservas y Tutorías

Estos laboratorios, en conjunto constan de **tres partes**

---

## Parte A – Modelado (Lab 1)

Incluye **imágenes** del Lab 1 desarrolladas en clase, que cubren:

* Diagrama de **casos de uso**
* Diagrama de **clases**
* Diagrama de **estados de la reserva**
* Diagrama de **secuencia de una reserva**

Los diagramas se encuentran como archivos de imagen dentro de esta sección

---

## Parte B – Constraints y USE con OCL

En esta parte se trabaja la validación formal del modelo utilizando **USE + OCL**.

### Archivos incluidos

* `reservas.use`
* `constraints.ocl`
* `reservas.cmd`

### Instrucciones de ejecución

> ⚠️ **Nota importante:** para que el modelo funcione correctamente, el contenido de `constraints.ocl` debe **copiarse y pegarse al final del archivo `reservas.use`**, dentro de la sección `constraints`.

#### Pasos:

1. Abrir la aplicación de **USE**
2. Cargar el archivo:

   * `reservas.use`
3. Ejecutar el script de estado:

   ```text
   open reservas.cmd
   ```
4. Ejecutar las validaciones OCL:

   ```text
   check
   ```

Esto permitirá verificar las invariantes, precondiciones y postcondiciones definidas.

---

## Parte C – Aplicación en Python (Arquitectura en Capas)

En esta parte se desarrolla una aplicación utilizando **Python** y **FastAPI**, siguiendo una **arquitectura en capas**

### Estructura del proyecto

* **app/**

  * `api/` – Endpoints y controladores
  * `application/` – Servicios de aplicación
  * `domain/` – Modelos y lógica de negocio
  * `infrastructure/` – Repositorio en memoria y persistencia
* **tests/**
  * Script de pruebas utilizando **pytest**

Las capas se comunican entre sí para permitir la creación de reservas, validaciones de negocio, llamadas a la API y almacenamiento en un repositorio en memoria.

---

## Configuración del entorno

Después de clonar el repositorio:

1. Crear y activar un entorno virtual
2. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

### Dependencias principales

* **FastAPI** – creación de la API
* **Uvicorn** – servidor 
* **Pytest** – ejecución de pruebas

---

## Ejecución de pruebas

```bash
python -m pytest -q
```

Se ejecutan **dos pruebas**, las cuales finalizan correctamente **sin errores**.

---

## Ejecución del servidor

```bash
python -m uvicorn app.api.main:app --reload
```

Luego, desde otra terminal, ejecutar:

```bash
curl -X POST "http://127.0.0.1:8000/reservas?estudiante_id=e1&tutor_id=t1&fecha_hora=2026-01-25T10:30:00"
```

### Resultado esperado

* Un mensaje que indique que el sistema **no permite reservar en el pasado**
* La API responde con:

  * **400 Bad Request**
* Se valida correctamente la regla de negocio definida en el dominio
