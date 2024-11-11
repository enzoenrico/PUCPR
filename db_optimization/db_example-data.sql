--categories
INSERT INTO categories (name) VALUES
('Eletrônicos'),
('Vestuário'),
('Livros'),
('Casa & Jardim'),
('Esportes');

-- subcategories
INSERT INTO categories (name, parent_category_id) VALUES
('Smartphones', 1),
('Notebooks', 1),
('Camisetas', 2),
('Ficção', 3),
('Ferramentas', 4);

-- user entries
INSERT INTO users (name, email, password, address, location, loyalty_points) VALUES
('John Doe', 'john@example.com', 'hash1', 'Rua Principal, 123', POINT(-23.5505, -46.6333), 100),
('Jane Smith', 'jane@example.com', 'hash2', 'Avenida Paulista, 456', POINT(-22.9068, -43.1729), 50),
('Bob Wilson', 'bob@example.com', 'hash3', 'Rua dos Carvalhos, 789', POINT(-30.0346, -51.2177), 75),
('Alice Brown', 'alice@example.com', 'hash4', 'Rua dos Pinheiros, 321', POINT(-19.9167, -43.9345), 200),
('Charlie Davis', 'charlie@example.com', 'hash5', 'Avenida Brasil, 654', POINT(-25.4290, -49.2671), 150);

-- products
INSERT INTO products (seller_id, name, description, price, stock, category_id, location) VALUES
(1, 'iPhone 13', 'Último modelo do iPhone', 999.99, 10, 6, POINT(-23.5505, -46.6333)),
(2, 'Dell XPS 15', 'Notebook premium', 1499.99, 5, 7, POINT(-22.9068, -43.1729)),
(3, 'Camiseta de Algodão', 'Vestuário casual confortável', 19.99, 100, 8, POINT(-30.0346, -51.2177)),
(4, 'Coleção Harry Potter', 'Série completa de livros', 89.99, 15, 9, POINT(-19.9167, -43.9345)),
(5, 'Kit de Jardinagem', 'Ferramentas essenciais', 49.99, 20, 10, POINT(-25.4290, -49.2671));

-- promos
INSERT INTO promotions (product_id, discount_percent, valid_from, valid_until) VALUES
(1, 10.00, '2024-03-01', '2024-04-01'),
(2, 15.00, '2024-03-15', '2024-04-15'),
(3, 20.00, '2024-03-10', '2024-03-31'),
(4, 25.00, '2024-03-20', '2024-04-20'),
(5, 30.00, '2024-03-05', '2024-04-05');

-- transactions
INSERT INTO transactions (user_id, product_id, quantity, total_price, points_earned) VALUES
(1, 2, 1, 1499.99, 150),
(2, 1, 1, 999.99, 100),
(3, 3, 2, 39.98, 4),
(4, 5, 1, 49.99, 5),
(5, 4, 1, 89.99, 9);

-- rrreeeviews
INSERT INTO reviews (user_id, product_id, rating, comment, review_date, seller_response, response_date) VALUES
(1, 2, 5, 'Notebook excelente!', '2024-03-01', 'Obrigado pela sua compra!', '2024-03-02'),
(2, 1, 4, 'Bom celular', '2024-03-03', 'Que bom que você gostou!', '2024-03-04'),
(3, 3, 5, 'Caiu perfeitamente', '2024-03-05', 'Obrigado!', '2024-03-06'),
(4, 5, 4, 'Ferramentas muito úteis', '2024-03-07', NULL, NULL),
(5, 4, 5, 'Coleção incrível', '2024-03-09', 'Obrigado pela avaliação!', '2024-03-10');