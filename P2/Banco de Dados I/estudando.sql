#Estudo Exercícios SQL - DDL Parte 1

#1. Criar um banco de dados chamado BD.
CREATE DATABASE BD;

#2. Abrir banco de dados BD para utilização.
USE BD;

#3. Criar a tabela CIDADE, conforme a especificação abaixo.
CREATE TABLE CIDADE (
    codigo INT NOT NULL,
    nome VARCHAR(30) NOT NULL;
    PRIMARY KEY (codigo)
)

#4. Criar a tabela SOCIO, conforme a especificação abaixo.
CREATE TABLE SOCIO(
    cpf CHAR(11) NOT NULL,
    nome VARCHAR(30) NOT NULL,
    sexo CHAR(1) NULL,
    email VARCHAR(30) NOT NULL,
    cidade INT NOT NULL,
    PRIMARY KEY cpf
    CONSTRAINT FK_SOCIO_cidade FOREIGN KEY (cidade) REFERENCES CIDADE(codigo),
    CONSTRAINT UK_SOCIO_email UNIQUE (email),
    CONSTRAINT CK_SOCIO_sexo CHECK (sexo IN ('M','F'))
);

#5. Criar a tabela DEPENDENTE, conforme a especificação abaixo.
CREATE TABLE DEPENDENTE(
    socio CHAR(11) NOT NULL,
    numero INT NOT NULL,
    nome VARCHAR(30) NOT NULL,
    PRIMARY KEY (socio, numero),
    CONSTRAINT FK_DEPENDENTE_socio FOREIGN KEY (socio) REFERENCES SOCIO(cpf)
);

#Estudo Exercícios SQL - DDL Parte 2

#6. Adicionar, na tabela SÓCIO, o campo abaixo especificado.
ALTER TABLE SOCIO
        ADD datanasc DATETIME NULL;

#7. Adicionar, na tabela CIDADE, o campo abaixo especificado.
ALTER TABLE CIDADE
        ADD uf CHAR(2) NOT NULL
        #Domínio: 2 caracteres
        CONSTRAINT CK_CIDADE_uf CHECK (CHAR_LENGTH(uf)=2);

#8. Adicionar um domínio (validação) para o campo NÚMERO da tabela DEPENDENTE, de modo que o valor seja maior que 0 (zero).
ALTER TABLE DEPENDENTE
        ADD CONSTRAINT CK_DEPENDENTE_numero CHECK (numero>0);

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


#Estudo Exercícios SQL - DQL Parte 1 "Consulta Simples"

#1. Obter, para todos os produtos, código, nome com o cabeçalho "Produto", quantidade em estoque com o cabeçalho "Estoque Real" e estoque mínimo com o cabeçalho "Estoque Mínimo".
SELECT idproduto, nome AS 'Produto', quantest AS 'Estoque Real', estmin AS 'Estoque Mínimo' FROM Produto;

#2. Obter, para todos os produtos, o código, o nome, o preço de venda e uma coluna adicional informando um aumento de 25% sobre o preço de venda. Dê um nome a esta coluna.
SELECT idproduto, nome, venda * 1.25 AS 'Venda com aumento' FROM Produto; 

#3. Obter as cidades onde residem os funcionários. Elimine a repetição de linhas.
SELECT DISTINCT idreside
FROM Funcionario;

#4. Obter código, nome, tipo, preço de custo e preço de venda de todos os produtos ordenados pelo tipo em ordem descendente e pelo nome em ordem ascendente.
SELECT idproduto, nome, tipo, custo, venda
FROM Produto
ORDER BY idtipo DESC, nome;

#5. Obter o nome e o setor dos funcionários que nasceram nas cidades com código 7, 8 e 15, ordenados pelo setor e nome do funcionário.

SELECT nome, setor FROM Funcionario
WHERE idnatural IN (7,8,15) 
ORDER BY idsetor, nome;

#6. Obter os produtos cujo tipo seja 1, 2 ou 3 e o preço de venda esteja entre R$ 10,00 e R$ 50,00.
SELECT *
FROM Produto
WHERE idtipo IN (1,2,3) AND venda BETWEEN 10 AND 50;

#7. Obter todos os dados dos funcionários que não têm e-mail, mas possuam celular.
SELECT * 
FROM Funcionario
WHERE email IS NULL AND celular IS NOT NULL;

#8. Obter o nome e o salário dos funcionários homens, casados e com salário menor ou igual a R$ 3.000,00, ordenados pelo salário em ordem descendente.
SELECT nome, salario
FROM Funcionario
WHERE sexo = 'M' AND estcivil = 'C' AND salario <= 3000
ORDER BY salario DESC;

#9. Obter o nome e o preço de venda dos produtos cuja descrição contenha a palavra "chocolate" com preço de venda maior ou igual a R$ 15,00, ordenados pelo preço de venda em ordem descendente.
SELECT nome,venda
FROM Produto
WHERE descricao LIKE '%CHOCOLATE%' AND venda >= 15
ORDER BY venda DESC;

#10. Obter o código e o nome dos funcionários homens, exceto aqueles cujos nomes iniciam pela letra "A", ordenados pelo nome em ordem ascendente.
SELECT idfuncionario,nome
FROM Funcionario
WHERE sexo = 'M' AND nome NOT LIKE '%A%'
ORDER BY nome ASC;

#Estudo Exercícios SQL - DQL Parte 2 "Funções de Agregação e Agrupamento"

#11. Obter quantos clientes fizeram pedido na empresa.
SELECT COUNT(DISTINCT idcliente)
FROM Pedido;

#12. Obter a soma do valor do frete de todos os pedidos atendidos por via marítima.
SELECT SUM(frete)
FROM Pedido
WHERE via='M';

#13. Obter a média de salário dos vendedores (funções 10 e 11) que não sejam casados.
SELECT AVG(salario)
FROM Funcionario
WHERE idfuncao IN (10,11) AND estcivil <> 'C';

#14. Obter a data de nascimento da funcionária mais velha.
SELECT MIN(datanasc)
FROM Funcionario
WHERE sexo = 'F'; 

#15. Obter qual a quantidade mais vendida de um produto para cada pedido.
SELECT idpedido, MAX(quant) AS 'Qntd. Máxima'
FROM Itens
GROUP BY idpedido;

#16. Obter quantos homens e quantas mulheres funcionários nasceram em cada cidade.
SELECT idnatural, sexo, COUNT(*) AS 'Quantidade'
FROM Funcionario
GROUP BY sexo, idnatural;

#17. Obter o total de salários de cada setor da empresa que tenha este total maior que R$ 5.000,00.
SELECT idsetor, SUM(salario) AS 'Total:'
FROM Funcionario
GROUP BY idsetor
WHERE SUM(salario)  > 5000;

#18. Obter o código do cliente e a quantidade de pedidos realizados por cada um em cada ano, apenas para os anos em que foram realizados mais de 5 pedidos.
SELECT idcliente, YEAR(datapedid) AS 'Ano', COUNT(*) AS 'Quantidade'
FROM Pedido 
GROUP BY YEAR(datapedid), idcliente 
HAVING COUNT(*) > 5;

#Estudo Exercícios SQL - DQL Parte 3 "Junção de Tabelas"