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







