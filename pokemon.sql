DROP database Pokemon;

CREATE database pokemon;
USE pokemon;

CREATE TABLE Pokemon(
    id INT PRIMARY KEY,
    name varchar(20),
    height INT,
    weight INT
);

CREATE TABLE Type(
    name varchar(20) PRIMARY KEY
);


CREATE TABLE Pokemon_types(
    pid INT,
    tname varchar(20),
    FOREIGN KEY(pid) REFERENCES Pokemon(id), 
    FOREIGN KEY(tname) REFERENCES Type(name),
    PRIMARY KEY (pid , tname)
);

CREATE TABLE Trainer(
    name varchar(20) PRIMARY KEY,
    town varchar(20)
);

CREATE TABLE pokemon_trainer(
    pid INT,
    tname varchar(20),
    FOREIGN KEY(pid) REFERENCES Pokemon(id),
    FOREIGN KEY(tname) REFERENCES Trainer(name),
    PRIMARY KEY(pid , tname)
);

create TABLE war(
    trainer VARCHAR(20) PRIMARY KEY,
    pokemon VARCHAR(20)
);