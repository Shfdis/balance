# Этап сборки
FROM node:23-slim AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Этап запуска
FROM node:23-slim
WORKDIR /app
COPY --from=build /app/build ./build

RUN npm install -g serve

EXPOSE 3001
CMD ["serve", "-s", "build", "-l", "3001"]