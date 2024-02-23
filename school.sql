




CREATE TABLE student (
  id           serial PRIMARY KEY,
  first_name   CHAR(50) NOT NULL,
  last_name    CHAR(50) NOT NULL,
  age          INT NOT NULL,
  subject      INT NOT NULL
);

CREATE TABLE subjects (
    id      serial PRIMARY KEY,
    subject CHAR(50) NOT NULL
);

CREATE TABLE teachers (
    id              serial PRIMARY KEY,
    first_name      CHAR(50) NOT NULL,
    last_name       CHAR(50) NOT NULL,
    age             INT NOT NULL,
    subject         INT NOT NULL
);