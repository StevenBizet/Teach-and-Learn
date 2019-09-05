
provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_container" "nginx" {
  image = "${docker_image.nginx.latest}"
  name = "enginecks"
  ports {
      internal = 80
      external = 80
  }
}

# docker run -p 80:80 -n enginecks nginx:latest

resource "docker_image" "nginx" {
  name = "nginx:latest"
}

# FROM nginx:latest

