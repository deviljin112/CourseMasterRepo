FROM mongo:latest AS database
COPY mongod.conf /etc/

FROM node:alpine AS app
WORKDIR /usr/src/app
COPY server_files .
RUN npm install