SHELL = /bin/bash
current_dir = $(shell pwd)
app_name = calculate-properties


run_docker = docker run -it --rm \
				--name $(app_name) \
				$(app_name)-dev:latest

docker-run: docker-build
	docker run -p 8000:80 $(app_name)-dev:latest

docker-build:
	docker build \
		-t $(app_name)-dev:latest .

docker-shell: docker-build
	$(run_docker) /bin/bash

docker-test: docker-build
	$(run_docker) pytest -s --cov

install:
	@pip install \
	-r requirements.txt 

compile:
	@rm -f requirements*.txt
	@pip-compile requirements.in
    
sync:
	@pip-sync requirements*.txt