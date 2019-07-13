CREATE TABLE cats (
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
breed TEXT,
net_worth INTEGER
);

CREATE TABLE owners (id INTEGER PRIMARY KEY, name TEXT);

CREATE TABLE cats_owners (
cat_id INTEGER,
owner_id INTEGER
);

INSERT INTO cats (id, name, age, breed, net_worth) VALUES (1, "Maru", 3, "Scottish Fold", 1000000);
INSERT INTO cats (id, name, age, breed, net_worth) VALUES (2, "Hana", 1, "Tabby", 21800);
INSERT INTO cats (id, name, age, breed, net_worth) VALUES (3, "Grumpy Cat", 4, "Persian", 181600);
INSERT INTO cats (id, name, age, breed, net_worth) VALUES (4, "Lil\' Bub", 2, "Tortoiseshell", 2000000);

INSERT INTO owners (name) VALUES ("mugumogu");
INSERT INTO owners (name) VALUES ("Sophie");
INSERT INTO owners (name) VALUES ("Penny");

INSERT INTO cats_owners (cat_id, owner_id) VALUES (3, 2);
INSERT INTO cats_owners (cat_id, owner_id) VALUES (3, 3);
INSERT INTO cats_owners (cat_id, owner_id) VALUES (1, 2);
