-- Parte 1: Criação do Banco de Dados
CREATE DATABASE IF NOT EXISTS doce_sabor;
# DROP DATABASE doce_sabor;

USE doce_sabor;

-- Parte 2: Criação das Tabelas
-- Criação da tabela Funcionario
CREATE TABLE IF NOT EXISTS Funcionario(
  cpf CHAR(11) NOT NULL,
  nome VARCHAR(45) NOT NULL,
  registro_habilitacao VARCHAR(45) NULL,
  categoria_habilitacao VARCHAR(45) NULL,
  FUNCIONARIO_cpf CHAR(11) NULL,

  CONSTRAINT PK_cpf_funcionario PRIMARY KEY (cpf),
  CONSTRAINT FK_cpf_funcionario FOREIGN KEY (FUNCIONARIO_cpf) REFERENCES Funcionario(cpf)
);

-- Criação da tabela Telefone
CREATE TABLE IF NOT EXISTS Telefone(
  FUNCIONARIO_cpf CHAR(11) NOT NULL,
  telefone VARCHAR(12) NOT NULL,
  
  CONSTRAINT CHK_telefone CHECK(LENGTH(telefone) >= 12),
  CONSTRAINT PK_telefone_func PRIMARY KEY (FUNCIONARIO_cpf, telefone),
  CONSTRAINT FK_telefone_funcionario FOREIGN KEY (FUNCIONARIO_cpf) REFERENCES Funcionario(cpf)
);

-- Criação da tabela Entregador
CREATE TABLE IF NOT EXISTS Entregador(
  FUNCIONARIO_cpf CHAR(11) NOT NULL,
  registro_habilitacao VARCHAR(45) NOT NULL,
  categoria_habilitacao VARCHAR(45) NOT NULL CHECK(categoria_habilitacao IN('A', 'AB', 'B')),

  CONSTRAINT PK_entregador_funcionario PRIMARY KEY (FUNCIONARIO_cpf),
  CONSTRAINT UQ_registro_habilitacao UNIQUE (registro_habilitacao),
  CONSTRAINT FK_funcionario_cpf_entregador FOREIGN KEY (FUNCIONARIO_cpf) REFERENCES Funcionario(cpf)
);

-- Criação da tabela Confeiteiro
CREATE TABLE IF NOT EXISTS Confeiteiro(
  FUNCIONARIO_cpf CHAR(11) NOT NULL,

  CONSTRAINT PK_confeiteiro_funcionario PRIMARY KEY (FUNCIONARIO_cpf),
  CONSTRAINT FK_funcionario_cpf_confeiteiro FOREIGN KEY (FUNCIONARIO_cpf) REFERENCES Funcionario(cpf)
);

-- Criação da tabela Curso
CREATE TABLE IF NOT EXISTS Curso(
  CONFEITEIRO_FUNCIONARIO_cpf CHAR(11) NOT NULL,
  descricao VARCHAR(45) NOT NULL,

  CONSTRAINT PK_curso PRIMARY KEY (CONFEITEIRO_FUNCIONARIO_cpf, descricao),
  CONSTRAINT FK_funcionario_cpf_curso FOREIGN KEY (CONFEITEIRO_FUNCIONARIO_cpf) REFERENCES Confeiteiro(FUNCIONARIO_cpf)
);

-- Criação da tabela Dependente
CREATE TABLE IF NOT EXISTS Dependente(
  FUNCIONARIO_cpf CHAR(11) NOT NULL,
  numero INT NOT NULL,
  nome VARCHAR(45) NOT NULL,

  CONSTRAINT PK_funcionario_dependente PRIMARY KEY (FUNCIONARIO_cpf, numero),
  CONSTRAINT FK_funcionario_cpf_dependente FOREIGN KEY (FUNCIONARIO_cpf) REFERENCES Funcionario(cpf)
);

-- Criação da tabela Cliente
CREATE TABLE IF NOT EXISTS Cliente(
  cpf CHAR(11) NOT NULL,
  nome VARCHAR(45) NOT NULL,
  telefone VARCHAR(12) NOT NULL CHECK(LENGTH(telefone) >= 12),
  email VARCHAR(45) NULL,
  data_nasc DATE NOT NULL,
  rua VARCHAR(45) NOT NULL,
  bairro VARCHAR(45) NOT NULL,
  cep VARCHAR(8) NOT NULL CHECK(LENGTH(cep) = 8),
  numero INT NOT NULL,
  cidade VARCHAR(45) NOT NULL DEFAULT 'João Pessoa',

  CONSTRAINT PK_cpf PRIMARY KEY (cpf)
  );

-- Criação da tabela Pedido
CREATE TABLE IF NOT EXISTS Pedido(
  cod_pedido INT NOT NULL AUTO_INCREMENT,
  FK_FUNCIONARIO_cpf CHAR(11) NOT NULL,
  FK_CLIENTE_cpf CHAR(11) NOT NULL,
  data_atendimento DATETIME NOT NULL,
  data_entrega DATETIME NOT NULL,
  tipo_entrega VARCHAR(45) NOT NULL DEFAULT 'Retirada',

  CONSTRAINT PK_cod_pedido PRIMARY KEY (cod_pedido),
  CONSTRAINT UQ_funcionario_cliente_pedido UNIQUE (FK_FUNCIONARIO_cpf, FK_CLIENTE_cpf),

  CONSTRAINT FK_funcionario_cpf FOREIGN KEY (FK_FUNCIONARIO_cpf) REFERENCES Funcionario(cpf),
  CONSTRAINT FK_cliente_cpf FOREIGN KEY (FK_CLIENTE_cpf) REFERENCES Cliente(cpf)
);

-- Criação da tabela Produto
CREATE TABLE IF NOT EXISTS Produto(
  codigo_produto INT NOT NULL,
  descricao VARCHAR(45) NOT NULL,
  CONSTRAINT PK_codigo_produto PRIMARY KEY (codigo_produto)
  );

-- Criação da tabela Contido_Em
CREATE TABLE IF NOT EXISTS Contido_em(
  PRODUTO_codigo_produto INT NOT NULL,
  PEDIDO_cod_pedido INT NOT NULL,
  valor DECIMAL(8,2) NOT NULL,
  unidade VARCHAR(3) NOT NULL,

  CONSTRAINT PK_contido_em PRIMARY KEY (PRODUTO_codigo_produto, PEDIDO_cod_pedido),
  CONSTRAINT FK_codigo_produto_contido FOREIGN KEY (PRODUTO_codigo_produto) REFERENCES Produto(codigo_produto),
  CONSTRAINT FK_codigo_pedido_contido FOREIGN KEY (PEDIDO_cod_pedido) REFERENCES Pedido(cod_pedido)
);


-- Parte 3: Inserção de dados nas Tabelas
INSERT INTO funcionario (cpf, nome, registro_habilitacao, categoria_habilitacao, funcionario_cpf)
VALUES 
	('07455264038', 'Alceu Paiva Valença', '92182215293', 'AB', NULL),
	('12345678900', 'Elba Maria Nunes Ramalho', '66294147113', 'AB', NULL),
	('32165498701', 'José Ramalho Neto', '93522240789', 'D', NULL),
    ('61575296432', 'Fábio Correia Júnior', NULL, NULL, '32165498701'),
	('86568010073', 'Maria Bethânia Viana Teles Veloso', NULL, NULL, '32165498701'),
	('78945612311', 'Geraldo Azevedo', NULL, NULL, '12345678900'),
	('11144477799', 'José Domingos de Morais', '66433740713', 'AB', '12345678900'),
	('58278632030', 'Marisa de Azevedo Monte',  NULL, NULL, '12345678900'),
    ('15272616464', 'Djavan Caetano Viana', '70369621234', 'B', '12345678900'),
    ('27498212404', 'Luiz Gonzaguinha', '62123470369', 'B', '12345678900'),
	('53021260012', 'Antônio Carlos Gomes Belchior', '73557013200', 'A', '07455264038'),
    ('08332112383', 'Roberto Carlos Braga', '13117622101', 'AB', '07455264038'),
    ('68833844560', 'Flávio José Marcelino Remígio', '22101131176', 'A', '07455264038'),
    ('15975345655', 'Raimundo Fagner Cândido Lopes', '00552770369', 'A', '07455264038'),
	('04147229069', 'Gal Maria da Graça Penna Burgos Costa', '12117504570', 'AB', '07455264038');

INSERT INTO telefone (funcionario_cpf, telefone)
VALUES 
	('32165498701', '083931117511'),
	('61575296432', '083998819881'),
	('15272616464', '083999775544'),
	('08332112383', '083988121314'),
	('27498212404', '083998812023'),
	('68833844560', '083999912023'),
	('12345678900', '083921033864'),
	('07455264038', '083927343456'),
    ('15975345655', '062925416558'),
	('78945612311', '082925063609'),
	('53021260012', '082926956837'),
	('86568010073', '083924787742'),
	('58278632030', '081928918417'),
	('11144477799', '083938469725'),
	('04147229069', '081932879043');

INSERT INTO confeiteiro (funcionario_cpf)
VALUES
	('78945612311'),
    ('11144477799'),
    ('58278632030'),
    ('15272616464'),
    ('27498212404');

INSERT INTO curso(confeiteiro_funcionario_cpf, descricao)
VALUES
	('78945612311', 'Curso Doces Finos'),
    ('15272616464', 'Curso de Panetones Gourmet'),
    ('11144477799', 'Curso de Pasta Americana'),
    ('58278632030', 'Curso Decoração de Bolos'),
    ('27498212404', 'Curso de Panetones Gourmet');

INSERT INTO entregador (funcionario_cpf, registro_habilitacao, categoria_habilitacao)
VALUES
	('53021260012', '73557013200', 'A'),
    ('08332112383', '13117622101', 'AB'),
    ('68833844560', '22101131176', 'A'),
	('15975345655', '00552770369', 'A'),
    ('04147229069', '12117504570', 'AB');

INSERT INTO dependente (funcionario_cpf, numero, nome)
VALUES
	('53021260012', '1', 'Nicolas Martins Melo Belchior'),
	('53021260012', '2', 'Marcos Martins Melo Belchior'),
	('86568010073', '3', 'Otávio Araujo Veloso'),
	('04147229069', '4', 'Sofia Castro Araujo Costa'),
	('32165498701', '5', 'Maria Barros Silva Ramalho'),
	('15975345655', '6', 'Sophia Rodrigues Cândido Lopes'),
	('15975345655', '7', 'Diogo Rodrigues Cândido Lopes'),
	('07455264038', '8', 'Julian Dias Pinto Valença'),
	('58278632030', '9', 'Raissa Goncalves de Azevedo Monte'),
	('12345678900', '10', 'Fernanda Cavalcanti Nunes Ramalho');

INSERT INTO Cliente(cpf, nome, telefone, email, data_nasc, rua, bairro, cep, numero)
VALUES
  ('12345678901', 'Ana Silva', '083987654321', 'ana.silva@email.com', '1990-05-15', 'Rua Arborizada', 'Mangabeira', '58055080', 10),
  ('23456789012', 'Pedro Santos', '083876543210', 'pedro.santos@email.com', '1985-10-22', 'Rua Boa Vizinhança', 'Bessa', '58035190', 20, 'João Pessoa'),
  ('34567890123', 'Juliana Oliveira', '083765432109', 'juliana.oliveira@email.com', '1992-02-03', 'Rua Caras Amigas', 'Mangabeira', '58055050', 30, 'João Pessoa'),
  ('45678901234', 'Marcos Pereira', '083654321098', NULL, '1988-07-12', 'Rua De Cristal', 'Bessa', '58035193', 40, 'João Pessoa'),
  ('56789012345', 'Larissa Santos', '081543210987', 'larissa.santos@email.com', '1995-11-28', 'Rua Esperança', 'Jaguaribe', '56789012', 50, 'João Pessoa'),
  ('67890123456', 'Thiago Lima', '083432109876', NULL, '1983-04-19', 'Rua Feira das Frutas', 'Jaguaribe', '58011402', 60, 'João Pessoa'),
  ('78901234567', 'Camila Silva', '083321098765', 'camila.silva@email.com', '1998-09-05', 'Rua Gente do Bem', 'Centro', '58010695', 70, 'João Pessoa'),
  ('89012345678', 'Rafael Oliveira', '083210987654', 'rafael.oliveira@email.com', '1980-12-08', 'Rua Hora do Rush', 'Centro', '58010695', 80, 'João Pessoa'),
  ('90123456789', 'Vanessa Santos', '083109876543', 'vanessa.santos@email.com', '1993-06-14', 'Rua Infinita', 'Intermares', '58102256', 90, 'Cabedelo'),
  ('01234567890', 'Leonardo Lima', '081987654321', 'leonardo.lima@email.com', '1986-01-23', 'Rua Já Vai', 'Altiplano', '58046335', 100, 'João Pessoa'),
  ('12301234501', 'Amanda Pereira', '083876543210', 'amanda.pereira@email.com', '1991-08-18', 'Rua Kukies', 'Ilha do Bispo', '58011402', 110, 'Bayeux'),
  ('23412345612', 'Guilherme Santos', '083765432109', 'guilherme.santos@email.com', '1987-03-27', 'Rua Lombada Rachada', 'Tambaú', '23412345', 120, 'João Pessoa'),
  ('34523456723', 'Isabella Lima', '081654321098', 'isabella.lima@email.com', '1994-12-02', 'Rua Mais Bonita', 'Altiplano', '58046335', 130, 'João Pessoa'),
  ('45634567834', 'Gabriel Oliveira', '083543210987', 'gabriel.oliveira@email.com', '1984-05-09', 'Rua Nova', 'Altiplano', '58046335', 140, 'João Pessoa'),
  ('56745678945', 'Larissa Lima', '083432109876', 'larissa.lima@email.com', '1999-02-16', 'Rua Ondulada', 'Mandacaru', '56745678', 150, 'João Pessoa'),
  ('67856789056', 'Bruno Santos', '083321098765', 'bruno.santos@email.com', '1982-07-21', 'Rua Perdida', 'Intermares', '58102256', 160, 'Cabedelo'),
  ('78967890167', 'Carolina Oliveira', '083210987654', 'carolina.oliveira@email.com', '1996-10-26', 'Rua Quero Ir Pra Casa', 'Mandacaru', '78967890', 170, 'João Pessoa'),
  ('89078901278', 'Lucas Lima', '083109876543', NULL, '1981-04-11', 'Rua Reta', 'Manaíra', '58055080', 180, 'João Pessoa'),
  ('90189012389', 'Beatriz Santos', '083987654321', 'beatriz.santos@email.com', '1997-01-30', 'Rua Sem Sombra', 'Bancários', '58055080', 190, 'João Pessoa'),
  ('01290123490', 'Henrique Oliveira', '083876543210', 'henrique.oliveira@email.com', '1989-08-07', 'Rua Terra', 'Intermares', '58102256', 200, 'Cabedelo'),
  ('30888509464', 'Leandro Leonardo', '083998817582', 'leo.santos@email.com', '1970-10-22', 'Rua Sertajena', 'Bessa', '58035190', 20, 'João Pessoa'),
  ('49102086409', 'Jão Paulo Daniel', '083988141413', 'jp.daniel@email.com', '1970-12-31', 'Rua Sertajena', 'Bessa', '58035190', 25, 'João Pessoa');  

INSERT INTO Pedido(FK_FUNCIONARIO_cpf, FK_CLIENTE_cpf, data_atendimento, data_entrega, tipo_entrega)
VALUES
	('61575296432', '67856789056', '2023-11-11 10:00:00', '2023-11-12 13:30:00', 'Delivery'),
    ('86568010073', '12345678901', '2023-12-9 13:30:00', '2023-12-10 13:45:00', 'Retirada'),
    ('61575296432', '30888509464', '2023-12-10 18:00:00', '2023-12-11 17:00:00', 'Delivery'),
    ('86568010073', '90123456789', '2023-11-9 13:30:00', '2023-11-15 13:15:00', 'Retirada'),
    ('61575296432', '78967890167', '2023-12-10 13:30:00', '2023-12-25 17:00:00', 'Delivery'),
    ('86568010073', '23412345612', '2023-11-8 14:30:00', '2023-11-10 13:45:00', 'Retirada'),
    ('61575296432', '34523456723', '2023-10-15 16:30:00', '2023-10-31 17:00:00', 'Delivery'),
	('61575296432', '67890123456', '2023-12-11 17:00:00', '2023-12-24 13:00:00', 'Delivery');


INSERT INTO Produto(codigo_produto, descricao)
VALUES
	(100 , 'Brownie'),
	(110 , 'Palha italiana'),
	(120 , 'Docinho'),
	(130 , 'Bolo'),
	(140 , 'Sobremesa'),
	(150 , 'Pirulito de chocolate'),
	(160 , 'Ovo de colher'),
	(170 , 'Cupcake'),
	(180 , 'Bolo no pote'),
	(190 , 'Trufas'),
	(200 , 'Cookies');


INSERT INTO Contido_em(PRODUTO_codigo_produto, PEDIDO_cod_pedido, valor, unidade)
VALUES
	(100, 1, 2.15, 10),
    (110, 1, 3.23, 15),
    (120, 4, 1.00, 50),
    (130, 8, 65.00, 1),
    (140, 4, 56.50 ,1),
    (150, 1, 3.50, 10),
    (160, 5, 24.65, 3),
    (170, 5, 7.80, 15),
    (180, 6, 7.00, 10),
    (190, 6, 3.50, 15),
	(200, 7, 8.89, 30);


  

-- Parte 4: Consultas SQL
# 1. Consultar clientes que moram nos bairros 'Bessa', 'Manaíra' e 'Tambaú' 
SELECT *
FROM Cliente
WHERE bairro IN ('Bessa', 'Manaíra', 'Tambaú')
ORDER BY bairro;


# 2. Consulta dos funcionários que não possuem habilitação
SELECT cpf, nome, registro_habilitacao
FROM funcionario 
WHERE registro_habilitacao IS NULL
ORDER BY nome;


# 3. Consultar funcionários e seus telefones
SELECT
	F.nome AS 'Funcionário',
    T.telefone AS 'Telefone'
FROM Funcionario F
JOIN Telefone T
ON F.cpf = T.funcionario_cpf
ORDER BY F.nome;


# 4. Consultar número de dependentes por funcionário
SELECT
  F.nome AS 'Funcionário',
  COUNT(*) AS Dependentes
FROM Funcionario F
JOIN Dependente D
ON F.cpf = D.funcionario_cpf
GROUP BY F.nome
ORDER BY Dependentes DESC, F.nome;


# 5. Consultar clientes cujos nomes começam com "L" 
SELECT *
FROM Cliente
WHERE nome LIKE 'L%'
ORDER BY nome;


# 6. Encontrar bairros onde existem pelo menos dois clientes
SELECT bairro, COUNT(*) AS total_clientes
FROM Cliente
GROUP BY bairro
HAVING total_clientes >= 2
ORDER BY total_clientes DESC, bairro;


# 7. Consulta para retornar os produtos com códigos cadastrados entre 100 e 150
SELECT * FROM Produto
WHERE codigo_produto BETWEEN 100 AND 150;


# 8. Consulta para retornar o valor total a pagar de determinado pedido feito por um cliente
SELECT
  fk_cliente_cpf AS 'CPF Cliente',
  cod_pedido AS Pedido,
  Round(SUM(valor * unidade), 2) AS 'Total a pagar'
FROM pedido
JOIN contido_em
ON pedido.cod_pedido = contido_em.pedido_cod_pedido
JOIN produto
ON contido_em.produto_codigo_produto = produto.codigo_produto
GROUP BY cod_pedido
HAVING pedido.fk_cliente_cpf = '67856789056';