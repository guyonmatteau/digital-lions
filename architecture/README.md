# Development status

Table to track development status of the endpoints.

| **Endpoint group** | **Endpoint**                  | **Method** | **Present**        | **Functional**     | **Tested**         | **Endpoint specific TODO's**      |
|--------------------|-------------------------------|------------|--------------------|--------------------|--------------------|-----------------------------------|
| **Health**         | `/health`                     | `GET`      | :white_check_mark: | :white_check_mark: | :white_check_mark: |                                   |
| **Communities**    | `/communities`                | `POST`     | :white_check_mark: | :white_check_mark: | :white_check_mark: |                                   |
|                    | `/communities`                | `GET`      | :white_check_mark: | :white_check_mark: | :white_check_mark: | - [ ] add query parameters        |
|                    | `/communities/{community_id}` | `PATCH`    | :white_check_mark: | :white_check_mark: | :white_check_mark: |                                   |
|                    | `/communities/{community_id}` | `DELETE`   |         :x:        |                    |                    |                                   |
|                    | `/communities/{community_id}` | `GET`      | :white_check_mark: | :white_check_mark: | :white_check_mark: |                                   |
| **Children**       | `/children`                   | `GET`      | :white_check_mark: | :white_check_mark: | :white_check_mark: | - [ ] add query parameters        |
|                    | `/children`                   | `POST`     | :white_check_mark: | :white_check_mark: | :white_check_mark: |                                   |
|                    | `/children/{child_id}`        | `GET`      | :white_check_mark: | :white_check_mark: | :white_check_mark: |                                   |
|                    | `/children/{child_id}`        | `PATCH`    | :white_check_mark: | :white_check_mark: | :white_check_mark: |                                   |
|                    | `/children/{child_id}`        | `DELETE`   | :white_check_mark: | :white_check_mark: |         :x:        | - [ ] add cascading of attendance |
| **Teams**          | `/teams`                      | `GET`      | :white_check_mark: | :white_check_mark: |         :x:        |                                   |
|                    | `/teams`                      | `POST`     | :white_check_mark: | :white_check_mark: |         :x:        |                                   |
|                    | `/teams/{team_id}`            | `GET`      | :white_check_mark: | :white_check_mark: |         :x:        |                                   |
|                    | `/teams/{team_id}`            | `DELETE`   | :white_check_mark: |         :x:        |                    |                                   |
|                    | `/teams/{team_id}`            | `PATCH`    |         :x:        |                    |                    |                                   |
|                    | `/teams/{team_id}/workshops`  | `POST`     | :white_check_mark: |         :x:        |                    |                                   |
|                    | `/teams/{team_id}/workshops`  | `GET`      | :white_check_mark: |         :x:        |                    |                                   |
| **Users**          | `/users`                      | `GET`      | :white_check_mark: |         :x:        |                    |                                   |
|                    | `/users`                      | `POST`     | :white_check_mark: |         :x:        |                    |                                   |
|                    | `/users/login`                | `POST`     | :white_check_mark: |         :x:        |                    |                                   |
|                    | `/users/{user_id}`            | `GET`      | :white_check_mark: |         :x:        |                    |                                   |
|                    | `/users/{user_id}`            | `PATCH`    | :white_check_mark: |         :x:        |                    |                                   |
|                    | `/users/{user_id}`            | `DELETE`   |         :x:        |                    |                    |                                   |


In addition, the following components are on the planning but not implemented yet:
- [ ] Authentication with API token
- [ ] Content filtering based on roles / scopes in user JWT
- [ ] `active_only` query parameter on all `GET` endpoints
