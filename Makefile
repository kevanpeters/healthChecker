.PHONY: healthChecker

HEALTH_ID = $(shell docker ps -q --filter="NAME=healthchecker_healthchecker")
NGINX_ID = $(shell docker ps -q --filter="NAME=healthchecker_nginx")
API_ID = $(shell docker ps -q --filter="NAME=healthchecker_api")

up:
	@docker-compose up --build -d

rebuild: up

down:
	@docker-compose down

healthChecker:
	 docker run -it $(shell docker build -q ./healthChecker/.) python healthChecker.py http://localhost:4000/api/time -i 5

stream-health:
	@docker logs $(HEALTH_ID) -f


#Failure Examples
fail-nginx:
	#This should give a connection time error
	docker stop $(NGINX_ID)
	sleep 7
	docker start $(NGINX_ID)

fail-api:
	#This should give a resolve error
	docker stop $(API_ID)
	sleep 7
	docker start $(API_ID)