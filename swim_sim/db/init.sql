-- Tabela de Atletas
CREATE TABLE IF NOT EXISTS atletas (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    nacionalidade TEXT NOT NULL,
    idade INTEGER,
    sexo TEXT NOT NULL,
    estilo_preferido TEXT
);

-- Tabela de Provas
CREATE TABLE IF NOT EXISTS provas (
    id INTEGER PRIMARY KEY,
    distancia INTEGER,
    estilo TEXT,
    genero TEXT
);

-- Tabela de Resultados
CREATE TABLE IF NOT EXISTS resultados (
    id INTEGER PRIMARY KEY,
    atleta_id INTEGER,
    prova_id INTEGER,
    tempo_segundos REAL,
    data TEXT,
    FOREIGN KEY (atleta_id) REFERENCES atletas(id),
    FOREIGN KEY (prova_id) REFERENCES provas(id)
);