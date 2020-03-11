
up:
	@docker-compose up --build -d

healthChecker:
	python3 healthChecker.py http://localhost:4000/api/time -i 2
