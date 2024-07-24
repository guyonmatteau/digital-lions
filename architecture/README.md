# Development status

Table to track development status of the endpoints.

| Endpoint group  | Endpoint                          | Method   | Existing           | Functional | Tested | Payload/response final |
|-----------------|-----------------------------------|----------|--------------------|------------|--------|------------------------|
| **Health**      | `/health`                         | `GET`    | :white_check_mark: |            |        |                        |
| **Communities** | `/communities`                    | `POST`   | :white_check_mark: | yes        | yes    | yes                    |
|                 | `/communities`                    | `GET`    | :white_check_mark: | yes        | yes    | yes                    |
|                 | `/communities`                    | `PATCH`  | :white_check_mark: | yes        | yes    | yes                    |
|                 | `/communities/{community_id}`     | `DELETE` | :x:                | no         |        |                        |
|                 | `GET /communities/{community_id}` |          |                    | yes        | yes    |                        |
|                 |                                   |          |                    |            |        |                        |
|                 |                                   |          |                    |            |        |                        |
|                 |                                   |          |                    |            |        |                        |
