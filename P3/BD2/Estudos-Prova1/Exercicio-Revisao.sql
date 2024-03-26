CREATE TABLE engenheiro(
	codeng SERIAL NOT NULL,
	nome VARCHAR(30),
	salario DECIMAL(15,2),
	
	CONSTRAINT pk_eng PRIMARY KEY(codeng)
);

CREATE TABLE projeto(
	codproj SERIAL NOT NULL,
	titulo VARCHAR(30),
	area VARCHAR(30),
	
	CONSTRAINT pk_proj PRIMARY KEY(codproj)
);

CREATE TABLE atuacao(
	codeng INT NOT NULL,
	codproj INT NOT NULL,
	funcao VARCHAR(30),
	
	CONSTRAINT pk_atuacao PRIMARY KEY(codeng, codproj),
	CONSTRAINT fk_eng FOREIGN KEY(codeng) REFERENCES engenheiro(codeng),
	CONSTRAINT fk_codproj FOREIGN KEY(codproj) REFERENCES projeto(codproj)
)

-- DROP TABLE atuacao;

SELECT * FROM engenheiro;
SELECT * FROM projeto;
SELECT * FROM atuacao;

-- INSERTS

-- Q6
INSERT INTO engenheiro(codeng, nome, salario) VALUES
(default, 'Marcelo Bruno', 15000.00),
(default, 'Lucas Kaique', 16000.00),
(default, 'Silas Leao', 17000.00),
(default, 'Luiz Fernando', 18050.00)

UPDATE engenheiro 
SET salario = 10000.00
WHERE codeng = 4;

-- Q7
INSERT INTO projeto(codproj, titulo, area) VALUES
(default, 'Desenvolvimento', 'dados'),
(default, 'Dashboards', 'business intelligence'),
(default, 'Testes', 'quality assurance')

-- Q8
INSERT INTO atuacao(codeng, codproj, funcao) VALUES
(1,1,'analista de dados'),
(2,3, 'QA pleno'),
(3,2, 'analista senior')

-- Q9
	-- a
	SELECT nome
	FROM engenheiro
	WHERE salario < 15000;

	-- b
	-- USANDO JOIN
	SELECT e.nome
	FROM engenheiro e
	JOIN atuacao a
	ON e.codeng = a.codeng
	WHERE a.funcao LIKE '%analista%';
	
	-- USANDO SUBQUERY
-- 	SELECT nome
-- 	FROM engenheiro
-- 	WHERE nome in (
-- 		SELECT 
-- 	)

	-- c. Mostre a quantidade de engenheiros por área de projeto.
	SELECT p.area AS "Area Projeto", COUNT(a.codeng) AS "QTD FUNCIONARIOS"
	FROM projeto p
	JOIN atuacao a
	ON a.codproj = p.codproj
	GROUP BY p.area;
	
	-- d. Verifique os nomes dos engenheiros que ganham acima da média salarial de todos
	SELECT nome
	FROM engenheiro
	WHERE salario > (
		SELECT AVG(salario)
		FROM engenheiro
	);

-- Q10
SELECT nome
FROM engenheiro
WHERE codeng IN (
				SELECT codeng
				FROM atuacao
				WHERE codproj IN (
								SELECT codproj
								FROM projeto
								WHERE area LIKE '%dados%'));

/* Resposta: 
A consulta primeiramente procura pelo código do projeto cuja
área envolva qualquer palavra relacionada a dados na base Projeto.
Em seguida, busca na base Atuacao

*/

-- Q11
SELECT codeng
	FROM engenheiro
	WHERE salario > 2200
	INTERSECT
	SELECT codeng
		FROM atuacao;

SELECT e.codeng
FROM engenheiro e
JOIN atuacao a
ON e.codeng = a.codeng
WHERE salario > 2200;


/* Q12. Crie uma view mostrando os nomes dos engenheiros,
sua função em cada projeto e o título do projeto. Consulte-a (0,2) */

CREATE OR REPLACE VIEW EngProj(nome, funcao, titulo) AS
SELECT e.nome, a.funcao, p.titulo
FROM engenheiro e
JOIN atuacao a ON e.codeng = a.codeng
JOIN projeto p ON p.codproj = a.codproj;

SELECT * FROM EngProj;


SELECT * FROM engenheiro;
SELECT * FROM projeto;
SELECT * FROM atuacao;

-- Q13
CREATE ROLE gerente LOGIN
PASSWORD 'manager';
GRANT SELECT ON eng 
TO gerente;

/* Q14. Mostre os engenheiros cadastrados que não possuem projetos vinculados.
Quais estratégias de operadores de consultas podem ser usadas nesta questão? */
SELECT e.nome
FROM engenheiro e
LEFT JOIN atuacao a
ON e.codeng = a.codeng
WHERE a.codproj IS NULL;


















