# Wybierz obraz bazowy (np. Node.js)
FROM node:14

# Utwórz katalog roboczy w kontenerze
WORKDIR /usr/src/app

# Skopiuj plik package.json i package-lock.json
COPY package*.json ./

# Zainstaluj zależności
RUN npm install

# Skopiuj resztę plików aplikacji
COPY . /home/frontEnd

# Ustaw port, na którym działa aplikacja
EXPOSE 4000

# Skompiluj aplikację (np. za pomocą komendy `npm run build`)
RUN npm run

# Uruchom serwer aplikacji
CMD ["npm", "start"]
