# Stage 0, "build-stage", based on Node.js, to build and compile the frontend
# FROM node:14.17.6-alpine as build-stage

FROM cisar/node-frontend as build-stage


WORKDIR /app

COPY package*.json /app/

RUN npm install

COPY ./ /app/


ARG FRONTEND_ENV=production

ENV VUE_APP_ENV=${FRONTEND_ENV}

# Comment out the next line to disable tests
# RUN npm run test:unit

RUN npm run build

# EXPOSE 80

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=80

CMD [ "npm", "start" ]

# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
# FROM nginx:1.15

# COPY --from=build-stage /app/.nuxt/ /usr/share/nginx/html

# COPY --from=build-stage /nginx.conf /etc/nginx/conf.d/default.conf
# COPY ./nginx-backend-not-found.conf /etc/nginx/extra-conf.d/backend-not-found.conf
