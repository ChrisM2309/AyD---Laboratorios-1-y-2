# Laboratorios 1 y 2 – Sistema de Reservas y Tutorías

Este repositorio contiene el desarrollo de **dos laboratorios** que muestran el **proceso completo de construcción de un sistema sencillo de reservas de tutorías**.

El trabajo cubre todo el flujo:
**modelado UML - especificación formal con OCL - implementación en Python**, manteniendo trazabilidad entre cada etapa.

---

## Laboratorio 1 

El **Laboratorio 1** está compuesto por **dos partes**, enfocadas en una primera aproximación al dominio y a la implementación.

###   Parte A – Diagramas y Contexto del Sistema

En esta parte se desarrollan **diagramas iniciales** que permiten entender el contexto general del sistema y su arquitectura básica.

* Contexto (Actores, Sistema, Externos)
* Arquitectura en capas (Vista logica)

---

### Parte B – Implementación Inicial en Python (API)

En esta parte se desarrolla una **implementación inicial del sistema de tutorías**, utilizando **Python** y **FastAPI**, siguiendo una **arquitectura en capas**.

#### Arquitectura utilizada

* Separación clara entre dominio, aplicación, infraestructura y API
* Reglas de negocio centralizadas en el dominio
* Repositorio en memoria para persistencia básica

#### Estructura del proyecto

```text
app/
├── api/              # Endpoints y controladores FastAPI
├── application/      # Servicios / casos de uso
├── domain/           # Modelos y reglas de negocio
└── infrastructure/   # Repositorio en memoria
tests/
└── tests con pytest
```

### Configuración del entorno (Laboratorio 1)

Después de clonar el repositorio:

1. Crear y activar un entorno virtual
2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

#### Dependencias principales

* **FastAPI** – creación de la API
* **Uvicorn** – servidor ASGI
* **Pytest** – ejecución de pruebas

---

### Ejecución de pruebas

```bash
python -m pytest -q
```

Se ejecutan **dos pruebas**, las cuales finalizan correctamente **sin errores**.

---

### Ejecución del servidor

```bash
python -m uvicorn app.api.main:app --reload
```

Desde otra terminal, ejecutar:

```bash
curl -X POST "http://127.0.0.1:8000/reservas?estudiante_id=e1&tutor_id=t1&fecha_hora=2026-01-25T10:30:00"
```

#### Resultado esperado

* El sistema **no permite reservar en el pasado**
* La API responde con **400 Bad Request**
* Se valida correctamente una regla de negocio del dominio

---

## Laboratorio 2 – UML, OCL y Arquitectura Formal

El **Laboratorio 2** amplía y formaliza el trabajo del Laboratorio 1.
Está compuesto por **tres partes**, que siguen el flujo completo enseñado en clase.

---

### Parte A – Modelado UML en Draw.io

Incluye capturas de los distintos modelos UML creados para el proyecto:

* Diagrama de **Casos de Uso**
* Diagrama de **Clases del Dominio**
* Diagrama de **Secuencia: Crear Reserva**
* Diagrama de **Estados de la Reserva**

---

### Parte B – OCL con USE (Validación Formal)

En esta parte se realiza la **especificación formal del modelo** utilizando **OCL y USE**, permitiendo validar reglas de negocio antes de implementar código.

#### Archivos incluidos

* `Cars.use` / `Cars.cmd` – ejercicio introductorio
* `University.use` / `University.cmd` – association class
* `Reservas.use` / `Reservas.cmd` – modelo simplificado
* `Tutorias.use` – modelo completo con pre y postcondiciones

> ⚠️ **Nota importante:**
> En USE, las restricciones OCL deben incluirse **al final del archivo `.use`**, dentro de la sección `constraints`.
> El archivo `constraints.ocl` sirve como apoyo, pero su contenido debe copiarse dentro del `.use`.

#### Ejecución en USE

1. Abrir la aplicación **USE**
2. Cargar el modelo:

   * `reservas.use` o `tutorias.use`
3. Ejecutar el script:

   ```text
   open reservas.cmd
   ```
4. Ejecutar validaciones:

   ```text
   check
   ```

USE detecta automáticamente:

* Violaciones de invariantes
* Incumplimiento de reglas de negocio
* Errores de consistencia del modelo

---

### Parte C – Implementación en Python

En esta parte se implementa nuevamente el sistema en Python, pero con una **arquitectura más formal y alineada al modelo UML y OCL**.

#### Características principales

* Separación estricta por capas:

  * `domain`
  * `repositories`
  * `services`
* Reglas OCL traducidas directamente a validaciones en código
* Uso de excepciones de dominio (`DomainError`)
* Pruebas con **pytest**
* Trazabilidad directa UML → OCL → Código

