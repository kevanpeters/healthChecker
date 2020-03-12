# HealthChecker

### Required Software

* Docker
* Docker Compose

### The Apps in this Repo

`Api/`
* This is a very simple flask API that has one endpoint that returns Date and Time in ISO format.

`healthChecker/`
* This is a CLI tool that runs a health Check against a given URL, It returns success and failure info along with time to last byte.

* The CLI help page can be accessed with the following Docker command from the healthCheckers folder.

        docker run -it $(docker build -q .) python healthChecker.py --help


* An example of using this tool could look like the following

        docker run -it $(docker build -q .) python healthChecker.py https://kevanpeters.com




### Setup with Docker-compose full example

Running the following command will run docker-compose up in the background. This will build the docker images in the API and HealthChecker folders along with pull an nginx image to run as a front end.

    make up
 
This runs the API, the Nginx webserver and the HealthChecker cli tool hitting  the Nginx serving the API. To stream these logs from the healthChecker you can run the following.

    make stream-health


In a different Shell you can test failure conditions

To trigger a connection error

    make fail-nginx

and to trigger a content resolve error

    make fail-api
