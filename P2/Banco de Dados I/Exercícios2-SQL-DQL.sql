-- Com base no Banco de Dados CONTPEDIDO, escreva os comandos SQL necessários para responder as questões abaixo.  -- 
#PARTE I - CONSULTAS SIMPLES

#1. Obter, para todos os produtos, código, nome com o cabeçalho "Produto", quantidade em estoque com o cabeçalho "Estoque Real" e estoque mínimo com o cabeçalho "Estoque Mínimo".
SELECT idproduto, nome AS 'Produto', quantest AS 'Estoque Real', estmin AS 'Estoque Mínimo' FROM Produto;

#2. Exibir, para todos os produtos, o código, o nome, o preço de venda e uma coluna adicional informando um aumento de 25% sobre o preço de venda. Dê um nome a esta coluna.
SELECT idproduto, nome, venda * 1.25 AS 'Venda com aumento' FROM Produto;

#3. Exibir as cidades onde residem os funcionários. Elimine a repetição de linhas.
SELECT DISTINCT idreside
FROM Funcionario;

#4. Exibir código, nome, tipo, preço de custo e preço de venda de todos os produtos ordenados pelo tipo em ordem descendente e pelo nome em ordem ascendente.
SELECT idproduto, nome, idtipo, custo, venda
FROM Produto
ORDER BY idtipo DESC, nome;

#5. Exibir o nome e o setor dos funcionários que nasceram nas cidades com código 7, 8 e 15, ordenados pelo setor e nome do funcionário.
SELECT nome, setor
FROM Funcionario
WHERE idnatural IN (7,8,15)
ORDER BY idsetor, nome;

#6. Exibir todos os produtos cujo tipo seja 1, 2 ou 3 e o preço de venda esteja entre R$ 10,00 e R$ 50,00.
SELECT *
FROM Produto
WHERE idtipo IN (1,2,3) AND venda BETWEEN 10 AND 50;

#7. Exibir todos os dados dos funcionários que não têm e-mail, mas possuam celular.
SELECT *
FROM Funcionario
WHERE email is NULL AND celular IS NOT NULL;

#8. Exibir o nome e o salário dos funcionários homens, casados e com salário menor ou igual a R$ 3.000,00, ordenados pelo salário em ordem descendente.
SELECT nome, salario
FROM Funcionario
WHERE sexo = 'M' AND estcivil = 'C' AND salario <= 3000
ORDER BY salario DESC;

#9. Exibir o nome e o preço de venda dos produtos cuja descrição contenha a palavra "chocolate" com preço de venda maior ou igual a R$ 15,00, ordenados pelo preço de venda em ordem descendente.
SELECT nome, venda
FROM Produto
WHERE descricao LIKE '%CHOCOLATE%' AND venda >= 15
ORDER BY venda DESC;

#10. Exibir o código e o nome dos funcionários homens, exceto aqueles cujos nomes iniciam pela letra A, ordenados pelo nome em ordem ascendente.
SELECT idfuncionario, nome
FROM Funcionario
WHERE sexo = 'M' AND nome NOT LIKE '%A%'
ORDER BY nome;

#PARTE II - FUNÇÕES DE AGREGAÇÃO E AGRUPAMENTO

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
WHERE idfuncao in (10,11) AND estcivil <> 'C';

#14. Obter a data de nascimento da funcionária mais velha.
SELECT MIN(datanasc)
FROM Funcionario
WHERE sexo='F';

#15. Obter qual a quantidade mais vendida de um produto para cada pedido.
SELECT idpedido, MAX(quant) AS 'Qntd. Máxima'
FROM Itens
GROUP BY idpedido;

#16. Obter quantos homens e quantas mulheres funcionários nasceram em cada cidade.
SELECT idnatural, sexo, COUNT(*) AS 'Quantidade'
FROM Funcionario
GROUP BY sexo, idnatural; 

#17. Exibir o total de salários de cada setor da empresa que tenha este total > R$ 5.000,00.
SELECT idsetor, SUM(salaroio) as 'Total'
FROM Funcionario
GROUP BY idsetor
HAVING SUM(salario) > 5000;

#18. Exibir o código do cliente e a quantidade de pedidos realizados por cada um em cada ano, apenas para os anos em que foram realizados mais de 5 pedidos.
SELECT idcliente, YEAR(datapedid) AS 'Ano', COUNT(*) AS 'Quantidade'
FROM Pedido 
GROUP BY YEAR(datapedid), idcliente 
HAVING COUNT(*) > 5;

#PARTE III - JUNÇÃO DE TABELAS

#19. Obter todos os funcionários, mostrando código, nome, código da função, nome da função e gratificação da função.
SELECT F1.idfuncionario AS 'Código do Funcionário',
	   F1.nome AS 'Nome do Funcionário',
       F1.idfuncao AS 'Código da função',
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
SELECT AVG(F1.salario) AS 'Média salarial'
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