-- Datos de ejemplo

INSERT INTO Produccion (FechaHora, Linea, Referencia, PiezasBuenas, PiezasScrap)
VALUES
('2025-11-16T06:00:00', 1, 'SG-12345', 1000, 25),
('2025-11-16T07:00:00', 1, 'SG-12345', 980, 30),
('2025-11-16T08:00:00', 1, 'SG-67890', 1100, 15);

INSERT INTO Paradas (FechaInicio, FechaFin, Linea, Causa)
VALUES
('2025-11-16T06:30:00', '2025-11-16T06:45:00', 1, 'Cambio de referencia'),
('2025-11-16T08:10:00', '2025-11-16T08:25:00', 1, 'Avería sensor temperatura');

INSERT INTO Alarmas (FechaHora, Linea, Codigo, Severidad, Mensaje)
VALUES
('2025-11-16T06:10:00', 1, 'TEMP_HIGH', 'ALTA', 'Temperatura cabezal por encima del límite'),
('2025-11-16T07:20:00', 1, 'SPD_LOW', 'MEDIA', 'Velocidad por debajo del objetivo');
