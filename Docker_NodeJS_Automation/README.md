# Micro-service with Docker, CI/CD with Jenkins and deployemnt to AWS

## Summary

Create a CI/CD pipline for your containers. Your final objective is to get jenkins to build the images and push to Dcoker hub, then to deploy onto AWS.

### Task

- Use Jenkins to clone the app and run the tests
- Once all the tests passed, Jenkins should triger build to build docker image and push it your docker hub repo
- Create a web-hook on your docker hub repo to send a notification email of success
- Next: Jenkins to trigger cd multi-stage docker build to deploy the containerised app on AWS
- We have done this with VMs and now it's time to see the real life difference between micro-services-containerisation VS VMs

### Acceptance Criteria

Jenkins to trigger docker build to containerise our node-app and push to docker hub repo. App and db deployed to AWS running in docker containers

## Code Breakdown

### Dockerfile

For this build `docker-compose` is used. The file can be found [HERE](container/docker-compose.yml). This solution has the option of removing the `Dockerfile` requirement, however it makes the structure cleaner and much easier to edit. The [Dockerfile](container/env/Dockerfile) contains just the image information and name alias as well as copying any necessary files and running any dependency installation. The format of this file is also known as Multi-Stage Build.

### Docker-Compose

The `docker-compose.yml` file therefore becomes our main hub of operation. This file breaks down both containers into stages, and each stage has its own operations. We can add commands, environment variables, volumes, dependancies and many other functionalities. This file will run specific stages for each container and therefore resulting in 2 containers being created at once.

### Ready Images

Images are available under the name of `deviljin112/eng74_nodejs_production` to specify which container you would like to pull use the tag `:app` or `:db`. These images can be loaded and started in seconds and full application deployed.

### Building Images

To build the images yourself:

- Clone the repository
- Navigate to the repository with your terminal
- Open the `container` folder
- Run `docker-compose build`
- Run `docker-compose up -d`
- Open browser and go to `localhost`
- Success

