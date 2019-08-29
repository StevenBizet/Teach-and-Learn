USERNAME:=xzenos
#IMAGE:=$(shell basename "$$(pwd)")
IMAGE:="teach_and_learn"
TAG:=$(shell TZ=UTC date +"%Y%m%d")


all: build run

build:
	# docker-compose build
	docker build -f docker/Dockerfile.flask -t $(USERNAME)/$(IMAGE):$(TAG) .

# Please use docker-compose instead
run: build
	#docker-compose up --build
	docker run -it $(USERNAME)/$(IMAGE):$(TAG)

test: build
	docker run -it $(USERNAME)/$(IMAGE):$(TAG) pipenv run pytest

deliver: test
	docker tag $(USERNAME)/$(IMAGE):$(TAG) $(USERNAME)/$(IMAGE):latest
	docker push $(USERNAME)/$(IMAGE):latest


