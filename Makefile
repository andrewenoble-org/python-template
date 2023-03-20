.DEFAULT_GOAL := help

.PHONY: help
help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo ""
	@echo "  build       build docker image"
	@echo "  exec        launch a shell in a running docker container"
	@echo "  git-config  configure git with dummy user email and name"
	@echo "  rmi         remove docker image"
	@echo "  run         deploy docker container"
	@echo "  stop        stop docker container"
	@echo ""
	@echo "Check the Makefile to know exactly what each target is doing."

.PHONY: build
build:
	docker build -t python-template .

.PHONY: exec
exec:
	docker exec -it python-template /bin/bash

.PHONY: git-config
git-config:
	git config --global user.email "a@b"
	git config --global user.name "a"

.PHONY: rmi
rmi:
	docker rmi python-template

.PHONY: run
run:
	docker run -v `pwd`:/home/project -itd --rm --name python-template python-template \
		/bin/bash

.PHONY: stop
stop:
	docker stop python-template
