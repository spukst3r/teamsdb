# :fireworks: TeamsDB server :eyes:


This API server provides access to a simple database consisting of teams and people. People can be groupped in teams that in turn can be grouped with other teams. Oh, and configurations like `team1 -> team2 -> team3 -> team1` are also possible! Have access to your organisation madness via a convenient API.

## Running TeamsDB

You need to have :whale: Docker installed.

```
docker-compose up
```

This command will download the [postgres image](https://hub.docker.com/_/postgres/) image, fill it with data; this will also build an image with the TeamsDB server and start it.


## API

### Teams

This resource exposes method `members`, which returns a list of names of people who belong to this team.

* URL: /api/v1/teams/:id/members

* Method: `GET`

*   **URL params**

    **Required**

	`id=[integer]` - the ID of the team

* **Success response**

  * **Code:** 200 <br/>
    **Content**: `["Person 1", "Person 2"]`

* **Error response**

  * **Code:**: 400 Bad Request <br/>
    **Content**: `{"error": "Requested to get members of a non-team"}`

  * **Code:**: 404 Not Found <br/>
    **Content**: _empty_


### People

This resource exposes method `teams`, which returns a list of names of teams which this person belongs to.

* URL: /api/v1/people/:id/teams

* Method: `GET`

*   **URL params**

    **Required**

	`id=[integer]` - the ID of the person

* **Success response**

  * **Code:** 200 <br/>
    **Content**: `["Team 1", "Team 2"]`

* **Error response**

  * **Code:**: 404 Not Found <br/>
    **Content**: _empty_
