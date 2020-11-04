DROP DATABASE IF EXISTS otusdc;
CREATE DATABASE otusdc;
CREATE USER otusdc  WITH LOGIN password 'otusdc';
GRANT ALL privileges ON DATABASE otusdc TO otusdc;
