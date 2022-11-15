# Crypto currency

## Description
Using Flask to build an WebServer that exposes the following:
- Current value of Bitcoin in dollar (updated every 10 seconds)
- Average value over the last 10 minutes

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
├── .github
│   └── workflows
│       └── ci.yml
├── Dockerfile
├── README.md
├── app.py
├── config.ini
├── helpers.py
├── requirements.txt
├── static
│   └── css
│       └── style.css
└── templates
    ├── base.html
    └── index.html

```

## Configuration Variables
The variables are managed in `config.ini` file

- interval: interval in seconds for fetching the current Bitcoin price and calculate average
- average_window_minutes: total timeframe in minutes to calculate average price
- crypto_api_url: the crypto api json url
- currency: the currency we are interested in (EUR/USD/...)

## Run Flask
### Run flask for develop
```
$ python app.py
```
In flask, Default port is `5000`

Swagger document page:  `http://127.0.0.1:5000`


### Run with Docker

```
$ docker build -t crypto_currency .

$ docker run -d -p 80:5000 crypto_currency
 
```

### Ci
For each tag that is pushed to the repo, which is in kind `v*.*.*`, a ci build will be run.
In the ci build, the following steps will be running:
- Checkout repository
- Get tag
- Log into registry - login to acr (Azure container registry) using github secrets
- Build & Push - build docker image and push to acr 

### Cd
In order to deploy the new version of the service, the orchestration system should update the image tag to the new version

### References
- [Flask](http://flask.pocoo.org/)
- [Crypto api](https://api.coindesk.com/v1/bpi/currentprice.json)
