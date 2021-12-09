# Docker Introduction

## What is docker

- Docker is an open source platform.
- It helps and enables us to seperate applications from the infrastructure.
- It allows us to deliver software faster.
- Docker is writen in GO language.

## Why Docker

- Largest Conglomorates are using or adapting Docker.
  - Ebay
  - Netflix
  - Sky
  - Many more
- Docker adoption is anticipated by 50% by the end of 2020
- Multiplatform

## Difference vs VirtualMachines

- Docker is light-weight and user friendly
- Docker shares the resources of the OS vs using a seperated OS
- Docker engine connects the container with OS and only use the resources required
- VM works with Hypervisor to connect guest OS/VM with host OS/server

## Microservices

Micoservices are a collection of small services that interact with each other to create the entire infrastructure. These services are:

- Highly maintainable and testable
- Independently deployable
- Organised into loose groups

## Monolithic

A monolithic application is a Host machine running most of the application on a container. This container is scaled up or down per needs, and the container is cloned as needed. Contrary to microservices where each segment of the infrastructure is seperated into its own container. With monolithic approach the entire container runs most of the infrastructure which is then cloned into a new container depending on the needs.

## Docker API

Syntax and Commands:

```bash
docker pull <image_name>
docker run <image_name>
docker build -t <image_name>
docker commit <image_name>/<container_id>
docker start <container_id>
docker stop <container_id>/<name>
docker rm <container_id>/<name>
docker ps
docker ps -a
```

### Logging into a container

```bash
docker exec -it <name>/<id>
```

## Mapping a port

```bash
docker run -d -p <host_port>:<container_port> <container_name>
```

## Building Docker Image

- To build a docker image we need to create a "Dockerfile"
- Why? To automate the tasks in an `image/container`
- What information is required inside the Dockerfile
  - It depends on the client's requirements
  - We need to know the dependancies to run the app/db
  - We need to wrap up all the dependencies in our Dockerfile and instrcut the execution command

## Syntax and Keywords for Dockerfile

- `FROM` is used to tell docker which base image to use
- `LABEL MAINTAINER=hswic@spartaglobal.com`
- `COPY` folder or files into the container from local host
- `EXPOSE` default port of the container
- `CMD` the execution command `["nginx", "-g", "daemon off"]`

## Task 1

Starting a container with `ghost`.

```bash
docker run -d -p 2368:2368 ghost
```

Open your browser and go to `localhost:3468`. You should see the website.
</br>
Stopping and removing the container.

```bash
docker ps
```

The above command will allow us the `<Container ID>` which we will need to use later. Copy it and have it ready to be pasted in the next commands.

```bash
docker kill <container_id>
docker rm <container_id>
```

If we check now whether the container exists or is available, we will notice its completely gone and new image must be created.

```bash
docker ps
docker ps -a
```

To check whether the image is still available run the following command.

```bash
docker images
```

## Task 2

Copy file into the container.

```bash
docker cp <host_file_location> <container_id>:<container_file_location>
```

## Task 3

Creating an image and pushing to dockerhub.

```bash
docker commit <container_id> <your_username>/<dockerhub_repo>
docker push <username>/<dockerhub_repo>:<tagname>
```

## Task 4

Getting logs from a container and pipping to a file.

```bash
docker logs <container_id> --details --timestamps > <file_name>.txt
```
