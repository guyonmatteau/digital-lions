# ADR 1: Program and Team structure

Quick write up of how a workshop relates to teams. A program is a "blueprint" for a set of workshops that **each team** goes through. Then,
First create a team with children. Upon creation, by default it gets assigned Program 1, which consists of 12 workshops.

If you then call GET /teams/:teamId/workshops you get a list of workshop for that team, but they are empty, because they haven't taken place yet.
```
GET /teams/:teamId/workshops 
API response:
{
  "program_id": 1,
  "workshops": [
    {
      "workshop_number": 1,
      "date": null,
      "workshop_id": null
      "attendance": []
    },
    {
      "workshop_number": 2,
      "date": null,
      "workshop_id": null
      "attendance": []
    },
    ...
    {
      "workshop_number": 12,
      "date": null,
      "workshop_id": null
      "attendance": []
    },
  ]
}
```

Next a workshop is happening, so we want to add the attendance of this workshop to the team. We call do this by creating a workshop with attendance:
```
POST /teams/:teamId/workshops
API body:
{
  "workshop_number": 1,
  "date": "2016-10-01",
  "attendance": [
    {
      "child_id": 1,
      "attendance": "present"
    },
    {
      "child_id": 2,
      "attendance": "absent"
    },
    {
      "child_id": 3,
      "attendance": "present"
    }
  ]
}
```
The reponse will be a workshop ID (`{"id": "<workshop_id>"}`), which is a unique identifier of a workshop that took place. Let's say the ID is 132. Now
if we list the workshops for the team again we get:
```
GET /teams/:teamId/workshops 
Reponse:
{
  "program_id": 1,
  "workshops":
  [
    {
      "workshop_number": 1,
      "date": "2016-10-01",
      "workshop_id": 132,
      "attendance": [
        {
          "child_id": 1,
          "first_name": "John",
          "last_name": "Doe",
          "attendance": "present"
        },
        {
          "child_id": 2,
          "first_name": "Jane",
          "last_name": "Doe",
        },
          "attendance": "absent"
        {
          "child_id": 3,
          "first_name": "Jack",
          "last_name": "Doe",
          "attendance": "present"
        }
      ] 
    },
    {
      "workshop_number": 2,
      "date": null,
      "workshop_id": null
      "attendance": []
    },
    ...
    {
      "workshop_number": 12,
      "date": null,
      "workshop_id": null
      "attendance": []
    },
  ]
}
```
This continues until all 12 workshops have been filled. Of course strict validation will take place (i.e. are the passed `child_id` actually part of the team, is the `attendance` value correct, 


