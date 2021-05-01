# Bet On You <> Florian

## Repository organisation

```
📦BetOnYou
 ┣ 📂controllers
 ┃ ┗ 📜playerController.py                          Player controller
 ┣ 📂models
 ┃ ┗ 📜Player.py                                    Player model
 ┣ 📂routes
 ┃ ┣ 📜playerRoutes.py
 ┃ ┗ 📜__init__.py                                  Routes aggregator
 ┣ 📜.gitignore
 ┣ 📜app.py                                         Flask server
 ┣ 📜BetOnYou Florian.postman_collection.json       Postman Collection
 ┣ 📜docker-compose.yml
 ┣ 📜Dockerfile                                     Python DockerFile
 ┣ 📜README.md
 ┣ 📜requirements.txt                               PIP Requirement
 ┗ 📜site.db                                        SQlite DB
```

## Requirements

- Docker
- Docker Compose
- Postman

## Setup

Start the API :

```
docker-compose up -d
```

API is running on port 5000

## Testing

You can import the Postman Collection and try the differents routes

## Ways to improve / Not cover

- Secure routes with user table and RBAC
- Handling errors
- Validate forms
- Test the API
- Logging API calls
- Paginate and filters the get all users route
