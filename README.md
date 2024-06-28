# Digital Lions

POC for a CRUD application for coaches and volunteers of [Little Lions Child Coaching](https://littlelionschildcoaching.com/) to track workshops and classes. Components: frontend (Vue + Bootstrap), backend (Python FastAPI), and PostgresDB. All dockerized and available in development locally with docker compose. Hosted with [Railway Apps](https://railway.app/).


## Design

The application is a frontend that talks to a backend API, which in turn talks to a Postgres database. The Postgres Database is designed with the following concepts in mind. Each block in the schematic overview (community, team, children, workshop, attendances, users, program) translates to a table in the databse.

![Database Schema](./docs/concept.png)
