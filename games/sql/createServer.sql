CREATE TABLE GIOCO (
	nome VARCHAR(50) PRIMARY KEY,
    descrizione VARCHAR(255) NOT NULL,
    piattaforma VARCHAR(50) NOT NULL,
    numgiocatorimassimi INT,
    immagine VARCHAR(50),
    link VARCHAR(100)
);

CREATE TABLE UTENTE (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50) NOT NULL,
    data DATE NOT NULL,
    ora TIME NOT NULL,
    immagine VARCHAR(50)
);

CREATE TABLE VOTAZIONE (
    nomegioco VARCHAR(50) NOT NULL,
    nomeutente VARCHAR(50) NOT NULL,
    voto INT CHECK (voto >= 1 AND voto <= 10) NOT NULL,
    commento VARCHAR(255),
    data DATE NOT NULL,
    ora TIME NOT NULL,
    PRIMARY KEY (nomegioco, nomeutente, data, ora),
    FOREIGN KEY (nomegioco) REFERENCES GIOCO(nome),
    FOREIGN KEY (nomeutente) REFERENCES UTENTE(username)
);

CREATE TABLE GENERE (
    nome VARCHAR(50) PRIMARY KEY,
    descrizione VARCHAR(255) NOT NULL
);

CREATE TABLE GIOCO_GENERE (
    nomegioco VARCHAR(50) NOT NULL,
    nomegenere VARCHAR(50) NOT NULL,
    PRIMARY KEY (nomegioco, nomegenere),
    FOREIGN KEY (nomegioco) REFERENCES GIOCO(nome),
    FOREIGN KEY (nomegenere) REFERENCES GENERE(nome)
);