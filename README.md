# Digital Lions

Application for coaches, volunteers, and admins of [Little Lions Child Coaching](https://littlelionschildcoaching.com/) to maintain teams, children, (attendance to) workshops. Hosted with [Railway Apps](https://railway.app/) on [staging.digitallions.annelohmeijer.com](https://staging.digitallions.annelohmeijer.com).


## Components 

The application is the simplest form of a private web CRUD application, consisting of a frontend (React), a backend (Python FastAPI), and PostgresDB. 

## Development

All components are dockerized and available in development locally with docker compose. This project uses [direnv](https://direnv.net/) to setup environment variables. First copy `.env.template` to `.env`. After that spin up the postgresDB (and optionally pgadmin if you want to inspect the database from the browser):
```bash
docker compose up -d db pgadmin
```
After that spin up the backend (either detached or in separate window):
```bash
docker compose up backend
```
The backend API should now be available at `http://localhost:8000/api/v1/docs#/`. Finally spin up the frontend (either detached or in separate window):
```bash
docker compose up frontend
```
The frontend should now be available at `http://localhost:5173`.

## System design

For system design, diagrams, and architecture decisions see the [architecture](architecture) folder. Status of the development of the endpoints can be found in the [architecture/README.md](architecture/README.md).

## Licence

To be added.
