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

#19. Obter todos os funcionários, mostrando código, nome, código da função, nome da função e gratificação da função.
SELECT F1.idfuncionario AS 'Código do Funcionário',
       F1.nome AS 'Nome do Funcionário',
       F1.idfuncao AS 'Código da Função',
       F2.nome AS 'Nome da Função',
       F2.gratific AS 'Gratificação'
FROM Funcionario F1
INNER JOIN Funcao F2 ON F1.idfuncao = F2.idfuncao;

#20. Obter o código e o nome dos clientes que moram na cidade de nome "London".
SELECT Cli.idcliente AS 'Código do Cliente',
	   Cli.nome AS 'Nome do Cliente'
FROM Cliente Cli
INNER JOIN Cidade Cid ON Cli.idcidade = Cid.idcidade
WHERE Cid.nome = 'London';

#21. Obter a média salarial dos funcionários cujo nome da função inicie por “Diretor”.
SELECT AVG(F1.salario) AS 'Média Salarial'
FROM Funcionario F1
INNER JOIN Funcao F2 ON F1.idfuncao = F2.idfuncao
WHERE F2.nome LIKE 'Diretor%';

#22. Obter o código do pedido, o nome do cliente e o nome do funcionário de todos os pedidos.
SELECT P.idpedido AS 'Pedido',
	   C.nome AS 'Cliente',
       F.nome AS 'Funcionário'
FROM Pedido P
INNER JOIN Cliente C ON P.idcliente = C.idcliente
INNER JOIN Funcionario F ON P.idvendendor = F.idfuncionario;

#23. Obter a quantidade de funcionários agrupados pelo nome do setor, mostrando apenas os setores com mais de 5 funcionários.
SELECT S.nome AS 'Setor', 
       COUNT(*) AS 'Quantidade'
FROM Funcionario F
INNER JOIN Setor S ON F.idsetor = S.idsetor
GROUP BY S.nome
HAVING COUNT(*) > 5;

#24. Obter o código e o nome das cidades que não tenham funcionários residentes nelas, ordenado pelo nome da cidade em ordem ascendente.
SELECT C.idcidade AS 'Código da Cidade', 
       C.nome As 'Nome da Cidade'
FROM Cidade C
LEFT JOIN Funcionario F ON C.idcidade = F.idreside
WHERE F.idfuncionario IS NULL
ORDER BY C.nome; 

#25. Obter o nome do setor superior e a quantidade de setores subordinados a cada um deles, ordenados pela quantidade em ordem descendente.
SELECT S2.nome AS 'Setor Superior',
       COUNT(*) AS 'Quantidade de Setores Subordinados'
FROM Setor S1
INNER JOIN Setor S2
ON S1.idsuperior = S2.idsetor
GROUP BY S2.nome
ORDER BY COUNT(*) DESC;

#SCRIPT INICIAL (DDL)
CREATE DATABASE BD_EX_DML;
USE BD_EX_DML;
CREATE TABLE Emp
(
codigo INT NOT NULL,
nome VARCHAR(30) NOT NULL PRIMARY KEY,
sexo CHAR(1) NOT NULL,
fone VARCHAR(16) NULL,
cidade VARCHAR(20) NULL DEFAULT 'João Pessoa',
salario NUMERIC(10,2) NULL
);
CREATE TABLE Emp2
(
codigo INT NOT NULL PRIMARY KEY,
nome VARCHAR(30) NOT NULL,
salario NUMERIC(10,2)
);


#1. Inserir, na tabela Emp, os dados:
INSERT INTO Emp (codigo, nome,sexo,fone,cidade,salario)
VALUES (620,'Antonio Pereira','M','3212-1212',DEFAULT,5000.00),
       (371,'Flávio Santana','M','3245-4545','Recife',NULL),
       (209,'Maria de Fátima','F','3232-3232','Natal',3000.00),
       (110,'Carlos Alberto','M',NULL,'Recife',NULL),
       (555,'Maria Aparecida','F',NULL,DEFAULT,4000.00);

#2. Alterar, na tabela Emp, o telefone do empregado de código 555 para “3222-9999”.
UPDATE Emp
SET fone = '3222-9999'
WHERE codigo = 555;

#3. Colocar, na tabela Emp, o salário de R$ 1.500,00 para os empregados que estejam sem salário.
UPDATE Emp
SET salario = 1500.00
WHERE salario IS NULL;

#4. Alterar, na tabela Emp, o telefone do empregado de código 110 para “99988-7766” e o salário para R$ 2.000,00.
UPDATE Emp
SET fone = '99988-7766', salario = 2000.00
WHERE codigo = 110;

#5. Adicionar R$ 150,00 ao salário dos empregados da tabela Emp que não moram em "João Pessoa".
UPDATE Emp
SET salario = salario + 150.00
WHERE cidade != 'João Pessoa';

#6. Alterar o salário dos empregados da tabela Emp para que nenhum deles ultrapasse R$ 3.500,00. Ou seja, os que ganharem acima disso vão passar a ter o salário com esse valor.
UPDATE Emp
SET salario = 3500.00
WHERE salario > 3500.00;

#7. Inserir, na tabela Emp, um novo empregado com código 400, nome 'Francisco de Assis', sexo masculino e salário igual ao menor salário cadastrado.
INSERT INTO Emp (codigo, nome,sexo,salario)
SELECT 400, 'Francisco de Assis','M', MIN(salario) FROM Emp;

#8. Preencher a tabela Emp2 com os empregados do sexo feminino cadastrados na tabela Emp.
INSERT INTO Emp2 (codigo, nome, salario)
SELECT codigo,nome,salario FROM Emp
WHERE sexo = 'F';

#9. Excluir, na tabela Emp, todos os empregados do sexo feminino.
DELETE FROM Emp
WHERE sexo = 'F';

#10. Excluir todos os empregados da tabela Emp2.
DELETE FROM Emp2;







