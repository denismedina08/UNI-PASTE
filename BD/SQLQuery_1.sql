--INSERT
--UPDATE
--DELETE
--SELEST COM MAIS DE UMA TABELA

CREATE DATABASE TURMA1441AN

USE TURMA1441AN;

CREATE TABLE ALUNOS
(
    MATRICULA CHAR(10) CONSTRAINT PK_ALUNOS PRIMARY KEY,
    NOME CHAR(10),
    SONRENOME CHAR(+10 ),
)

INSERT ALUNOS(MATRICULA, NOME, SONRENOME)
VALUES ('RA1234','DENIS','MEDINA')

INSERT ALUNOS VALUES ('DENIS','MEDINA','RA123')
SELECT * FROM ALUNOS
ALTER TABLE ALUNOS ADD SEXO CHAR(10)