#Criar um banco de dados chamado BD.
CREATE DATABASE BD;

#Abrir banco de dados BD para utilização.
USE BD;

#Criar a tabela CIDADE, conforme a especificação
CREATE TABLE CIDADE (
		codigo INT NOT NULL,
        nome VARCHAR(30) NOT NULL,
        PRIMARY KEY (codigo)
);

CREATE TABLE SOCIO(
		cpf CHAR(11) NOT NULL,
        nome VARCHAR(30) NOT NULL,
        sexo CHAR(1) NULL,
        email VARCHAR(30) NOT NULL UNIQUE,
        cidade INT NOT NULL,
        PRIMARY KEY(cpf),
        CONSTRAINT FK_SOCIO_cidade FOREIGN KEY (cidade) REFERENCES CIDADE (codigo),
        CONSTRAINT UK_SOCIO_email UNIQUE (email),
		CONSTRAINT CK_SOCIO_sexo CHECK (sexo IN ('M','F'))
);
#5. Criar a tabela DEPENDENTE, conforme a especificação abaixo.