-- create table client (
--     id_client INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
--     nom VARCHAR(100) NOT NULL ,
--     email VARCHAR(150) NOT NULL UNIQUE,
--     created_at TIMESTAMP DEFAULT NOW() NOT NULL
-- );
-- create table restaurants (
--     id_restaurant INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY ,
--     nom VARCHAR(150) NOT NULL,
--     city VARCHAR(100) NOT NULL,
--     category VARCHAR(50),
--     created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
-- );

-- create table drivers (
--     drivers_id INTEGER  GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--     nom VARCHAR(100) NOT NULL,
--     phone VARCHAR(20) UNIQUE NOT NULL,
--     is_available BOOLEAN DEFAULT TRUE NOT NULL,
--     created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
-- );

-- create table commandes(
--     id_commande INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
--     id_client INTEGER REFERENCES client(id_client) NOT NULL,
--     id_restaurant INTEGER REFERENCES restaurants(id_restaurant) NOT NULL,
--     drivers_id INTEGER REFERENCES drivers(drivers_id),
--     montant NUMERIC(10,2) CHECK (montant>=0) NOT NULL,
--     statut VARCHAR(30) NOT NULL,
--     created_at TIMESTAMPTZ DEFAULT NOW() NOT NULL
--  );

-- INSERT INTO client (nom, email)
-- VALUES ('Ahmed', 'ahmed.test@example.com')
-- RETURNING id_client;

-- INSERT INTO client (nom,email)
-- VALUES ('yassine','yassine@gmail.com')
-- RETURNING id_client;

-- INSERT INTO restaurants (nom, city, category)
-- VALUES ('Pizza Express', 'Casablanca', 'Fast Food')
-- RETURNING id_restaurant;

-- INSERT INTO commandes (id_client, id_restaurant, montant, statut)
-- VALUES (1, 1, 25.50, 'en cours')
-- RETURNING id_commande;

-- select nom, email 
-- from client
-- order by id_client;

-- select nom, city, category
-- from restaurants
-- order by id_restaurant;

-- update commandes
-- set montant = montant - 10
-- where id_commande = 1;

-- UPDATE commandes 
-- set montant = montant + montant * 0.1
-- where id_commande = 3;

-- SELECT
--     id_commande,
--     id_client,
--     id_restaurant,
--     drivers_id,
--     montant,
--     statut
-- FROM commandes
-- ORDER BY id_commande;
-- SELECT id_commande, montant
-- FROM commandes
-- WHERE id_commande = 3;
-- BEGIN;
--  UPDATE commandes
--  SET montant = 75.00
--  WHERE id_commande = 3;
--  COMMIT;
--  ROLLBACK;
  
-- SELECT id_commande, montant
-- FROM commandes
-- WHERE id_commande = 3;


-- select id_commande, montant
-- from commandes
-- where id_commande = 3;
 
-- BEGIN;
--  UPDATE commandes
--  SET montant = 100.00
--  WHERE id_commande = 3;

-- select id_commande, montant
-- from commandes
-- where id_commande = 3;

-- ROLLBACK;

-- select id_commande, montant
-- from commandes
-- where id_commande = 3;

-- select * from commandes
-- where id_commande = 3 or id_commande = 6;
-- begin;
-- update commandes
-- set montant = 80 
-- where id_commande = 3;
-- update commandes
-- set montant = - 10 
-- where id_commande = 6;
-- ROLLBACK;