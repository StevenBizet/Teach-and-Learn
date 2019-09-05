USERNAME:=xzenos
#IMAGE:=$(shell basename "$$(pwd)")
IMAGE:="teach_and_learn"
TAG:=$(shell TZ=UTC date +"%Y%m%d")


all: build test deliver

build:
	# docker-compose build
	docker build -f docker/Dockerfile.flask -t $(USERNAME)/$(IMAGE):$(TAG) .

# Please use docker-compose instead
run: build
	#docker-compose up --build
	docker run -it $(USERNAME)/$(IMAGE):$(TAG)

test: 
	docker run -it $(USERNAME)/$(IMAGE):$(TAG) pipenv run pytest

deliver:
	docker tag $(USERNAME)/$(IMAGE):$(TAG) $(USERNAME)/$(IMAGE):latest
	echo "$(DOCKER_PASSWORD)" | docker login -u "$(DOCKER_USERNAME)" --password-stdin
	docker push $(USERNAME)/$(IMAGE):latest


