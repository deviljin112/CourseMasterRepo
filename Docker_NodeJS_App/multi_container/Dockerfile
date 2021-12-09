FROM node:latest as APP
WORKDIR /usr/src/app
COPY . .
RUN npm install
# EXPOSE 3000
# CMD ["node", "app.js"]

FROM node:alpine
COPY --from=APP /usr/src/app /usr/src/app
WORKDIR /usr/src/app
RUN npm install

EXPOSE 3000
CMD ["node", "app.js"]

# FROM mongo:latest
# WORKDIR /usr/src/db/
# COPY mongod.conf /etc/
# CMD ["mongod"]
# EXPOSE 27017
