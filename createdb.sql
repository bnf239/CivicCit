DROP DATABASE civiccit;
CREATE DATABASE civiccit;
CREATE USER mydatabaseuser WITH PASSWORD 'mypassword';
ALTER ROLE mydatabaseuser SET client_encoding TO 'utf8';
ALTER ROLE mydatabaseuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE mydatabaseuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE civiccit TO mydatabaseuser;