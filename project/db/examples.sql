CREATE TABLE "client" (
    "id" SERIAL NOT NULL,
    "denomination" VARCHAR(100) NOT NULL,
    "social_reason" VARCHAR(100) NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE "product" (
    "id" SERIAL NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE "product_version" (
    "id" SERIAL NOT NULL,
    "product_id" INTEGER NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "description" VARCHAR(100) NOT NULL,
    PRIMARY KEY ("id"),
    CONSTRAINT product_fk FOREIGN KEY(product_id) REFERENCES "product"(id)
);

CREATE TABLE "ticket" (
    "id" SERIAL NOT NULL,
    "title" VARCHAR(100) NOT NULL,
    "description" VARCHAR(100) NOT NULL,
    "state" INTEGER NOT NULL,
    "estimated_duration" TIMESTAMP NOT NULL,
    "started_date" TIMESTAMP NOT NULL,
    "finish_date" TIMESTAMP NOT NULL,
    "product_version_id" INTEGER NOT NULL,
    "client_id" INTEGER NOT NULL,
    PRIMARY KEY ("id"),
    CONSTRAINT client_fk FOREIGN KEY(client_id) REFERENCES "client"(id),
    CONSTRAINT product_version_fk FOREIGN KEY(product_version_id) REFERENCES "product_version"(id)
);

CREATE TABLE "resource" (
    "id" SERIAL NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "surname" VARCHAR(100) NOT NULL,
    "area_id" INTEGER NOT NULL,
    PRIMARY KEY ("id")
);

CREATE TABLE "task" (
    "id" SERIAL NOT NULL,
    "title" VARCHAR(100) NOT NULL,
    "description" VARCHAR(100) NOT NULL,
    "state" INTEGER NOT NULL,
    "estimated_duration" TIMESTAMP NOT NULL,
    "started_date" TIMESTAMP NOT NULL,
    "finish_date" TIMESTAMP NOT NULL,
    "resource_id" INTEGER NOT NULL,
    PRIMARY KEY ("id"),
    CONSTRAINT resource_fk FOREIGN KEY(resource_id) REFERENCES "resource"(id)
);

CREATE TABLE "ticket_task" (
    "ticket_id" INTEGER NOT NULL,
    "task_id" INTEGER NOT NULL,
    PRIMARY KEY ("ticket_id", "task_id"),
    CONSTRAINT ticket_fk FOREIGN KEY(ticket_id) REFERENCES "ticket"(id),
    CONSTRAINT task_fk FOREIGN KEY(task_id) REFERENCES "task"(id)
);
