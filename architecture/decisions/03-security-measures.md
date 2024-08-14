# Security measures

> Date: Aug 8th, 2024

This document outlines the security measures that are or will be implemented in the system, to ensure the safety of the data and the system itself.

## General & codebase

- [x] No sensitive data is stored hardcoded in the codebase.
- [ ] All dependencies are kept up-to-date using a dependency management tool (e.g. [Dependabot](https://github.com/dependabot)).

## Authentication & Authorization

- [x] No plain passwords are stored in the database. Instead, we store the hash of the password and the [salt](https://auth0.com/blog/adding-salt-to-hashing-a-better-way-to-store-passwords/) used to generate the hash. Passwords can be reset via email links.
- [ ] The database will require a strong password to access it.
  - [ ] This password will be rotated every X months.
- [ ] All backend endpoints require a static API token to be included in the header of the request.
  - [ ] This API token will be renewed every X months.
- [ ] All user specific endpoints require a [Json Web Token (JWT)](https://blog.logrocket.com/secure-rest-api-jwt-authentication/) token to be included in the header of the request. This JWT can be obtained by logging in on the `POST /users/session` endpoint.
  - [ ] The JWT token will expire after X minutes.

## Networking

- [ ] The database will reside in virtual network of the backend and thus be network-isolated.
- [x] The backend will use [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) to only allow requests from the frontend origin.


