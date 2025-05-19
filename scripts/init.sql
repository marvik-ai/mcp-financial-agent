-- Create a table to store company financial information
CREATE TABLE IF NOT EXISTS company_financials (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(255) NOT NULL,
    currency_code CHAR(3) NOT NULL,
    revenue NUMERIC(15, 2) NOT NULL,
    profit NUMERIC(15, 2) NOT NULL
);

-- Insert dummy data into the table
INSERT INTO company_financials (company_name, currency_code, revenue, profit) VALUES
    ('TechCorp', 'USD', 5000000.00, 1200000.00),
    ('Innovate Ltd', 'EUR', 4200000.00, 1000000.00),
    ('Global Solutions', 'GBP', 3000000.00, 800000.00),
    ('FutureWorks', 'JPY', 600000000.00, 150000000.00),
    ('EcoWorld', 'AUD', 2500000.00, 600000.00);