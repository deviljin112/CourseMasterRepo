# Docker NodeJS App

This repository was created to easily create and connect 2 seperate Docker containers. One which launches the NodeJS app and other which runs the MongoDB Database.

## Pre-requisites

- Docker

## Creating and Running the images

Navigate to `db` folder in order to build the initial image. Afterwards run the build command.

```bash
docker build -t <name_of_image>
```

Ensure that you only create `db` image as the app image will be created afterward due to the file requiring an IP address to be added to the environment.
</br>
In order to run the full application you need to firstly run the database image. Followed by a docker command that returns the IP address of the database container, after which the app image can be created and initialised. The syntax is in the following order.

```bash
docker run -d -p 27017:27017 <database_image>
docker inspect --format '{{ .NetworkSettings.IPAddress }}' <database_container_id>
```

The `inspect` command will return a string with an IP address of the database container. We need to now take that IP address and add it to our app's `Dockerfile`. We need to change the `DB_HOST` IP address to the one that the above command has provided.

```bash
FROM node:latest
WORKDIR /usr/src/app
COPY . .
RUN npm install
EXPOSE 3000
ENV DB_HOST=<your_ip>:27017
CMD ["node", "app.js"]
```

After we have added our Database's IP address we can now create the image and run it.

```bash
docker build -t <name_of_image>
docker run -d -p 80:3000 <app_image>
```

If we have followed the instructions correctly after running `docker ps` we should see two containers running and after accessing `localhost` with out browser we should see the application running. If we navigate to `localhost/posts/` we should see a "Recent Posts" page meaning the DB connection was established.
