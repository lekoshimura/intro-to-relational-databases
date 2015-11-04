-- Antes de executar este script, faça:
-- $ psql
-- vagrant => create database tournament;

-- Para executar este script, faça:
-- $ psql
-- \i tournament.sql

\c tournament;

drop table if exists matches;
drop table if exists players;

create table players (
    id serial primary key,
    name varchar(128)
);

create table matches (
    id serial primary key,
    winner int references players(id),
    loser int references players(id)
);
