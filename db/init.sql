-- Create a table
CREATE TABLE customer (
    customer_id SERIAL PRIMARY KEY,
    home_store VARCHAR(255),
    customer_first_name VARCHAR(255),
    customer_email VARCHAR(255),
    customer_since DATE,
    loyalty_card_number VARCHAR(50),
    birthdate DATE,
    gender VARCHAR(10),
    birth_year INTEGER
);

-- Insert data
COPY customer (
    "customer_id",
    "home_store",
    "customer_first_name",
    "customer_email",
    "customer_since",
    "loyalty_card_number",
    "birthdate",
    "gender",
    "birth_year"
)
FROM '/docker-entrypoint-initdb.d/data/customer.csv' DELIMITER ',' CSV HEADER;