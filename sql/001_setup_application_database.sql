CREATE DATABASE izanami OWNER = postgres TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'C' LC_CTYPE = 'C';
CREATE USER izanami WITH PASSWORD izanami;
GRANT ALL PRIVILEGES ON DATABASE izanami TO admin;
