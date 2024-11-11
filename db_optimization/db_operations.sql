--  average rating per product
SELECT p.product_id,
    p.name AS product_name,
    ROUND(AVG(r.rating), 2) AS average_rating,
    COUNT(r.review_id) AS total_reviews
FROM products p
    LEFT JOIN reviews r ON p.product_id = r.product_id
GROUP BY p.product_id,
    p.name
ORDER BY average_rating DESC;

--  total sales per category
SELECT c.name AS category_name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(
        CASE
            WHEN pr.promotion_id IS NOT NULL 
            AND pr.start_date <= GETDATE() 
            AND pr.end_date >= GETDATE() THEN t.total_price * (1 - pr.discount_percentage / 100)
            ELSE t.total_price
        END
    ) AS total_earned
FROM categories c
    LEFT JOIN products p ON c.category_id = p.category_id
    LEFT JOIN transactions t ON p.product_id = t.product_id
    LEFT JOIN promotions pr ON p.product_id = pr.product_id
GROUP BY c.category_id,
    c.name
ORDER BY total_earned DESC;

-- find by category
SELECT p.product_id,
    p.name,
    p.price,
    p.stock,
    u.name AS seller_name
FROM products p
    INNER JOIN categories c ON p.category_id = c.category_id
    INNER JOIN users u ON p.seller_id = u.user_id
WHERE c.category_id = ?
    OR c.parent_category_id = ?
ORDER BY p.price ASC;

-- find reviews per product
SELECT p.product_id,
    p.name AS product_name,
    r.rating,
    r.comment,
    u.name AS reviewer_name,
    r.review_date,
    r.seller_response,
    r.response_date
FROM products p
    LEFT JOIN reviews r ON p.product_id = r.product_id
    LEFT JOIN users u ON r.user_id = u.user_id
WHERE p.product_id = ?
ORDER BY r.review_date DESC;

-- update stock after a transaction
CREATE TRIGGER update_stock_after_transaction ON transactions
AFTER
INSERT AS BEGIN
UPDATE p
SET stock = p.stock - i.quantity
FROM products p
    INNER JOIN inserted i ON p.product_id = i.product_id
END;

-- get the average review rating per product
SELECT p.product_id,
    p.name AS product_name,
    ROUND(AVG(r.rating), 2) AS average_rating,
    COUNT(r.review_id) AS total_reviews
FROM products p
    LEFT JOIN reviews r ON p.product_id = r.product_id
GROUP BY p.product_id,
    p.name
ORDER BY average_rating DESC;

-- add loyalty points after a transaction
CREATE TRIGGER add_loyalty_points ON transactions
AFTER
INSERT AS BEGIN
UPDATE u
SET loyalty_points = loyalty_points + i.points_earned
FROM users u
    INNER JOIN inserted i ON u.user_id = i.user_id
END;

-- get the total sales per category considering active promotions
SELECT c.name AS category_name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(
        CASE
            WHEN pr.promotion_id IS NOT NULL
            AND pr.start_date <= GETDATE()
            AND pr.end_date >= GETDATE() THEN t.total_price * (1 - pr.discount_percentage / 100)
            ELSE t.total_price
        END
    ) AS total_price_with_promotions
FROM categories c
    LEFT JOIN products p ON c.category_id = p.category_id
    LEFT JOIN transactions t ON p.product_id = t.product_id
    LEFT JOIN promotions pr ON p.product_id = pr.product_id
GROUP BY c.category_id,
    c.name
ORDER BY total_price_with_promotions DESC;

