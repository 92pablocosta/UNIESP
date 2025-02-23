CREATE TABLE clientes (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(15),
    endereco TEXT NOT NULL
);

CREATE TABLE pedidos (
    id SERIAL PRIMARY KEY,
    cliente_id INT REFERENCES clientes(id) ON DELETE CASCADE,
    status VARCHAR(10) CHECK (status IN ('Pendente', 'Pago', 'Cancelado'))
);

INSERT INTO clientes (nome, email, telefone, endereco) VALUES
('João Silva', 'joao@email.com', '(83) 99999-9999', 'Rua A, 123'),
('Maria Souza', 'maria@email.com', '(83) 98888-8888', 'Rua B, 456'),
('Carlos Pereira', 'carlos@email.com', '(83) 97777-7777', 'Rua C, 789');

INSERT INTO pedidos (cliente_id, status) VALUES ((SELECT id FROM clientes WHERE nome = 'João Silva'), 'Pendente');
INSERT INTO pedidos (cliente_id, status) VALUES ((SELECT id FROM clientes WHERE nome = 'Maria Souza'), 'Pago');

INSERT INTO pedidos (cliente_id, status) VALUES 
((SELECT id FROM clientes WHERE nome = 'Carlos Pereira'), 'Pago'),
((SELECT id FROM clientes WHERE nome = 'Carlos Pereira'), 'Cancelado');

SELECT * FROM clientes;
SELECT nome, email FROM clientes;
SELECT id, cliente_id, status FROM pedidos;
SELECT * FROM pedidos WHERE status = 'Pendente';
SELECT pedidos.* FROM pedidos
JOIN clientes ON pedidos.cliente_id = clientes.id
WHERE clientes.nome = 'Maria Souza';
UPDATE clientes SET telefone = '(83) 96666-6666' WHERE nome = 'Carlos Pereira';

UPDATE pedidos SET status = 'Pago' 
WHERE cliente_id = (SELECT id FROM clientes WHERE nome = 'João Silva');

DELETE FROM pedidos WHERE cliente_id = (SELECT id FROM clientes WHERE nome = 'João Silva');

DELETE FROM clientes WHERE nome = 'João Silva';

ALTER TABLE clientes ADD COLUMN cpf VARCHAR(14);
ALTER TABLE clientes ALTER COLUMN telefone TYPE VARCHAR(20);
ALTER TABLE clientes DROP COLUMN endereco;
