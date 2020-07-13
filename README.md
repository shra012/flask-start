# flask-start
An example application with basic ecommerce UI.

## Github Action Build Status

![Docker Image](https://github.com/Learn-And-Earn/flask-start/workflows/Docker%20Image/badge.svg?branch=master)

REST API written in Python Flask & DB2

## Pre-requisites

- Download & install [Python 3.6](https://www.python.org/downloads/)
- Download & install [Pipenv](https://docs.pipenv.org/)

```cmd
 python -m pip install -U pip
 pip3 install pipenv
```

## Installation

```cmd
# Clone the repository
# Change into the directory
cd flask-start
# Install all required dependencies with
pipenv install --deploy --skip-lock
# [Optional Step] If you get a warining stating the virtual environment path dosent exist
set PIPENV_IGNORE_VIRTUALENVS=1
pipenv install --skip-lock
# Activate the project virtual environment
pipenv shell
```

You can also set the enviroment variables explicity (OPTIONAL)

```cmd
set FLASK_APP=app.py
set FLASK_ENV=development
set SECRET_KEY="SAMPLE_SECRET_KEY"
set SQLALCHEMY_DATABASE_URI="ibm_db_sa://username:password@hostname:port/databasename"
set GOOGLE_OAUTH_CLIENT_ID="OAuth Client Id"
set GOOGLE_OAUTH_CLIENT_SECRET="OAuth Client Secret"
set OAUTHLIB_INSECURE_TRANSPORT=True
set OAUTHLIB_RELAX_TOKEN_SCOPE=True
set PORT=5000
```

## vscode setup

- Install python from vscode extensions market place (ctrl+shift+x) [ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- Open the command palette in visual studio (ctrl+shift+P) type `>Python: Select Interpreter`
- Choose the python interpreter of virtual env `('flask-start': pipenv)`
- Once that is done check the .vscode folder settings.json if the `python.pythonPath` points to your virtual env.
- To debug the applictaion open Run (ctrl+shift+D) and click on the play button besided Run with Python: Flask selected in the drop down.

## Running the application

**Start the app in virtual env shell**

```cmd
flask run
```

## Usage

**Project Structure**

![Project Structure Example](https://raw.githubusercontent.com/Learn-And-Earn/flask-start/master/docs/images/flask-start-project-structure.png)

- __app.py__ contains the code call to initiazlie the app via create_app() definition under app/&#95;&#95;init__.py
- All the flask app configs are under config.py
- All the blueprints are under controllers
- Model &#95;&#95;init__.py contains the database initialization and SQLAlchemy.

**Blue-Prints Specifications**
#### Basic Route
- GET: /homepage - app/basic_routes.py
- GET & POST: /login - app/basic_routes.py
#### Mobile Controller
- GET: /mobile/{id}
- GET: /mobile/buynow/{id}
- GET: /mobile/addtocart/{id}
#### Cart Controller
- GET: /cart 
- GET: /cart/deleteItem/{id}
**Example**
curl http://localhost:5000/login

## Running the application as a Docker container

```cmd
cd flask-start
# Build the docker image
docker build -t shra012/flask-start:latest .
# Run the docker container
docker run --name flask-start -e FLASK_ENV=development -e FLASK_APP=app.py \
-e SECRET_KEY=SAMPLE_SECRET_KEY -e SQLALCHEMY_DATABASE_URI=ibm_db_sa://username:password@hostname:port/databasename \
-e GOOGLE_OAUTH_CLIENT_ID=OAuth_Client_Id -e GOOGLE_OAUTH_CLIENT_SECRET=OAuth_Client_Secret \
-p 5000:5000 shra012/flask-start:latest
# Check the logs
docker logs -f flask-start
# Cleaup the container
docker stop flask-start && docker rm flask-start
```

## Author

Shravankumar Nagarajan
