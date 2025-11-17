-- Esquema básico para base de datos de producción industrial

CREATE TABLE Produccion (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    FechaHora DATETIME NOT NULL,
    Linea INT NOT NULL,
    Referencia VARCHAR(50) NOT NULL,
    PiezasBuenas INT NOT NULL,
    PiezasScrap INT NOT NULL
);

CREATE TABLE Paradas (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    FechaInicio DATETIME NOT NULL,
    FechaFin DATETIME NOT NULL,
    Linea INT NOT NULL,
    Causa VARCHAR(100) NOT NULL
);

CREATE TABLE Alarmas (
    Id INT IDENTITY(1,1) PRIMARY KEY,
    FechaHora DATETIME NOT NULL,
    Linea INT NOT NULL,
    Codigo VARCHAR(50) NOT NULL,
    Severidad VARCHAR(20) NOT NULL,
    Mensaje VARCHAR(255) NOT NULL
);
