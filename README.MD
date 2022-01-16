postgres=# create database juornal;
CREATE DATABASE
postgres=# CREATE USER admin WITH PASSWORD 'P@ssw0rd';
CREATE ROLE
postgres=# GRANT ALL PRIVILEGES ON DATABASE juornal TO admin;
GRANT
postgres=# \c juornal
You are now connected to database "juornal" as user "postgres".
juornal=# CREATE EXTENSION citext;
CREATE EXTENSION
juornal=# 


