FROM node:21 AS build

WORKDIR /app 
COPY package*.json yarn.lock ./
RUN yarn install 
COPY . /app
RUN yarn build --outDir=./dist/out

FROM nginx
COPY --from=build /app/dist/out/ /usr/share/nginx/html
COPY /nginx.conf /etc/nginx/conf.d/default.conf