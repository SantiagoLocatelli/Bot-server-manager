CREATE DATABASE "pensamiento_computacional";
\c "pensamiento_computacional";

CREATE TABLE "cuatrimestre" (
    "id" SERIAL NOT NULL,
    "description" VARCHAR(50) NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE "alumno" (
    "DNI" VARCHAR(11) NOT NULL,
    "nombre" VARCHAR(100) NOT NULL,
    "cuatrimestre_id" INTEGER NOT NULL,
    "registrado" BOOLEAN DEFAULT false,
    PRIMARY KEY ("DNI"),
    CONSTRAINT cuatrimestre_fk FOREIGN KEY(cuatrimestre_id) REFERENCES "cuatrimestre"(id) 
);

