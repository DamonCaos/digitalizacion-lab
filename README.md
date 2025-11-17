# Carpeta Base de Proyectos · Digitalización Avanzada

Esta carpeta contiene una base avanzada para practicar y trabajar
habilidades típicas del área de digitalización industrial:

- C# / .NET
- SQL Server
- Python (Dashboards e informes)
- OPC UA (simulado)
- Esquema de base de datos industrial

## Estructura

- `dotnet-industrial-tool/`
  - Proyecto de consola en .NET 8 para conectarse a SQL Server y leer datos de producción.

- `python-dashboard/`
  - Esqueleto de dashboard industrial con Python y datos simulados.

- `opcua-simulator/`
  - Servidor OPC UA de ejemplo con variables típicas de línea de extrusión.

- `sql/`
  - `schema.sql`: tablas de Produccion, Paradas y Alarmas.
  - `sample-data.sql`: datos de ejemplo.

- `reports/`
  - `daily_report.py`: script de informe diario a partir de datos de producción.

## Uso recomendado

1. Carga el esquema SQL en tu SQL Server o entorno de pruebas.
2. Ajusta las cadenas de conexión en C# y Python.
3. Lanza el servidor OPC UA simulado si quieres practicar integraciones.
4. Extiende los proyectos con tus propias necesidades de planta.
