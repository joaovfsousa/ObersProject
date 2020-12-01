# API for Obers
## About

API created as part of an interview for a software development job at Obers.

## Running the API

To start the API in docker, after cloning and entering the app directory, run:

```{bash}
sudo docker build -t obers-project:1.0 .

sudo docker run --publish 9095:9095 --detach --name FlaskApi obers-project:1.0
```

## Usage

### Route /health
↗️ GET localhost:9095/health to check whether or not the service is running

↗️ POST localhost:9095/validator/Cpf to validate a cpf

- Request body example
  ```
  {
	  "cpf": 12345678901
  }
  ```


