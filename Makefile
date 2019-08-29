DOCKERHUB_USERNAME ?= $(shell whoami)
#IMAGE:=$(shell basename "$$(pwd)")
IMAGE:=teach_and_learn
TAG:=$(shell TZ=UTC date +"%Y%m%d")


all: build test deliver

build:
	# docker-compose build
	docker build -f docker/Dockerfile.flask -t $(DOCKERHUB_USERNAME)/$(IMAGE):$(TAG) .

# Please use docker-compose instead
run: build
	#docker-compose up --build
	docker run -it $(DOCKERHUB_USERNAME)/$(IMAGE):$(TAG)

test: 
	docker run -it $(DOCKERHUB_USERNAME)/$(IMAGE):$(TAG) pipenv run pytest

deliver:
	docker tag $(DOCKERHUB_USERNAME)/$(IMAGE):$(TAG) $(DOCKERHUB_USERNAME)/$(IMAGE):latest
	echo "$(DOCKERHUB_PASSWORD)" | docker login -u "$(DOCKERHUB_USERNAME)" --password-stdin
	docker push $(DOCKERHUB_USERNAME)/$(IMAGE):latest


