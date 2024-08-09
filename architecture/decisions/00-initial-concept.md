## Design

> June 28th, 2024


The application is a frontend that talks to a backend API, which in turn talks to a Postgres database. The Postgres Database is designed with the following concepts in mind. Each block in the schematic overview (community, team, children, workshop, attendances, users, program) translates to a table in the database.

![Database Schema](img/initial-concept.png)
