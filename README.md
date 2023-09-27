# tech1-api

## Features:  
- Create operation for users and articles.
- Get all Users whose age is greater than some value
- Get all Users from Articles, in which color is some certain value from the enum 
- Get unique names from Users that have more than 3 Articles

## Prerequisites

Before you begin, ensure you have the following installed:

-   Docker: [Install Docker](https://docs.docker.com/get-docker/)

## Getting Started

Follow these steps to set up and run the tech1-api project using local project and Docker:

1.  Clone this repository to your local machine:
    
    `git clone https://github.com/mariiahorbova/tech1-api.git`
2. Navigate to the project directory: `cd tech1-api` 
3. Create `.env` file and define environmental variables by following `.env_sample`: 
```
SECRET=your_secret_key
ALGORITHM=your_encryption_algorithm
POSTGRES_NAME=your_postgres_name
POSTGRES_PASSWORD=your_postgres_password
POSTGRES_DB=db
POSTGRES_HOST=your_postgres_host
```
:heavy_exclamation_mark: :exclamation: You should generate secret key using steps below:

Go to the python shell, do these steps and copy the result string into `.env` file:
```
>>> import os
>>> import binascii
>>> binascii.hexlify(os.urandom(24))
b'3ddaa62a2b1a49c2b895e86093c0eb5e2cad246d06e3b433'
```

4.  Build the Docker container using Docker Compose and start it:

    `docker-compose up --build`
## Endpoints  
```
POST /users/signin - Create Token For Signin
GET /users/{age} - Get Users By Age
GET /users/articles/{color} - Get Users By Article Color
GET /users-qt-3-articles - Get Unique Names With More Than 3 Articles
POST /users - Create User
POST /articles - Create Article
```
5. To test endpoints above, import `Tech1.postman_collection.json` to collections and `Tech1.postman_environment.json` to environments
6. To run tests in docker:

    Access list of containers:
`docker ps -a`

    Open docker container:
`docker exec -it <container_id here> bash`

    Run tests using `python -m pytest tests` command


## Technologies used

### FastAPI, SQLAlchemy, Alembic, PostgreSQL, Docker
