#PARTE I
#1. Criar um banco de dados chamado BD.
CREATE DATABASE BD;

#2. Abrir banco de dados BD para utilização.
USE BD;

#3. Criar a tabela CIDADE, conforme a especificação
CREATE TABLE CIDADE (
		codigo INT NOT NULL,
        nome VARCHAR(30) NOT NULL,
        PRIMARY KEY (codigo)
);

#4. CREATE TABLE SOCIO(
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
CREATE TABLE DEPENDENTE(
		socio CHAR(11) NOT NULL,
        numero INT NOT NULL,
        nome VARCHAR(30) NOT NULL,
        PRIMARY KEY (socio, numero),
        CONSTRAINT FK_DEPENDENTE_socio FOREIGN KEY (socio) REFERENCES SOCIO (cpf)
);

#PARTE II

#6. Adicionar, na tabela SÓCIO, o campo especificado.
ALTER TABLE SOCIO
		ADD datanasc DATETIME NULL;
        
#7. Adicionar, na tabela CIDADE, o campo abaixo especificado.
ALTER TABLE CIDADE
		ADD uf CHAR(2)
        #Domínio: 2 caracteres
        CONSTRAINT CK_CIDADE_uf CHECK (CHAR_LENGTH(uf)=2);
        
#8. Adicionar um domínio (validação) para o campo NÚMERO da tabela DEPENDENTE, de modo que o valor seja maior que 0 (zero).
ALTER TABLE DEPENDENTE
		ADD CONSTRAINT CK_DEPENDENTE_numero CHECK (numero > 0);
        
#9. Alterar, na tabela SÓCIO, o tipo do campo NOME para varchar(40).
ALTER TABLE SOCIO
		MODIFY nome VARCHAR(40) NOT NULL;

#10. Excluir, na tabela CIDADE, o domínio do campo UF.
ALTER TABLE CIDADE
		DROP CONSTRAINT CK_cidade_uf;

#11. Excluir, na tabela SÓCIO, o campo cidade.
ALTER TABLE SOCIO
		DROP CONSTRAINT FK_SOCIO_cidade;
ALTER TABLE SOCIO
		DROP COLUMN cidade;

#12. Excluir a tabela CIDADE.
DROP TABLE CIDADE;

#13. Excluir o banco de dados BD.
DROP DATABASE BD;
