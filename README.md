# Garden Palooza

A multiplayer gardening game. 

## Installation

### Manual

For the API and game servers, you'll need `python3` and `pip`

For developing the React app, you'll need `create-react-app`, or at least `npm`

#### API Server

Switch to the `api/` directory

Create and activate virtual environment using virtualenv
```bash
$ python3 -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies

```bash
pip install -r requirements.txt
```

#### Game Server

Switch to the `socket/` directory

Create and activate virtual environment using virtualenv. Make sure to use a separate one from the API server!
```bash
$ python3 -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies

```bash
pip install -r requirements.txt
```

#### React App 

Install JavaScript dependencies
```bash
$ npm install package.json

```

### Docker

Make sure you have the `docker` daemon installed and running, and `docker-compose` installed.

Create a .env file using the example.env template.

For development, run `docker-compose -f docker-compose.yml -f docker-compose-dev.yml build`

## Usage

### Manual

#### API Server

Create a .env file inside the /api directory using the example.env template.

Start flask development server, using the virtualenv inside the /api directory.
```bash
$ export FLASK_ENV=development
$ flask run
```
#### Game Server

Source the virtualenv inside the /socket directory.

Start the server
```bash
uwsgi --http :5000 --gevent 1000 --http-websockets --master --wsgi-file app.py --callable app --py-autoreload 1

```
### Docker

For development, run `docker-compose -f docker-compose.yml -f docker-compose-dev.yml up`

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.