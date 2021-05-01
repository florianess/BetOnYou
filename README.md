# Bet On You <> Florian

## Repository organisation

```
📦BetOnYou
 ┃ ┣ 📜playerController.py                          Player controller
 ┃ ┗ 📜__init__.p
 ┣ 📂models
 ┃ ┣ 📜Player.py
 ┃ ┗ 📜__init__.py                                  Player model
 ┣ 📂routes
 ┃ ┣ 📜playerRoutes.py                              Routes aggregator
 ┃ ┗ 📜__init__.py
 ┣ 📂services
 ┃ ┣ 📜ClashRoyale.py                               Connection with Clash Royale API
 ┃ ┣ 📜Fortnite.py                                  Connection with Fornite API
 ┃ ┗ 📜__init__.py
 ┣ 📂tests
 ┃ ┣ 📜testPlayer.py                                Unit tests for the player route
 ┃ ┗ 📜__init__.py
 ┣ 📜.env.example
 ┣ 📜.gitignore
 ┣ 📜app.py                                         Flask server
 ┣ 📜BetOnYou_Florian.postman_collection.json       Postman Collection
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
cp .env.example .env
docker-compose up -d
```

Make sure to add the API keys in the .env file

- Fornite API : https://dashboard.fortniteapi.io/

- Clash Royal API : https://developer.clashroyale.com/

API is running on port 5000

## Testing

You can import the Postman Collection and try the differents routes

To run the unit test, make sure to use a virtual env with the requrements:

```
python -m unittest
```

## How to use the API

### Get all players (in python)

```python
import requests

url = "http://localhost:5000/api/players/"

response = requests.request("GET", url)
```

### Create a new player (in python)

```python
import requests
import json

url = "http://localhost:5000/api/players/"

payload={
    "email": "john@doe.com",
    "username": "johndoe",
    "firstname": "john",
    "lastname": "doe"

}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text)
```

## Ways to improve / Not cover

- Secure routes with user table and RBAC
- Handling errors
- Validate forms
- Enhance tests
- Better logging API calls
- Paginate and filters the get all users route
