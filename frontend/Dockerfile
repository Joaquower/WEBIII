# Imagen base
FROM mirror.gcr.io/library/node:current
# Carpeta de trabajo
WORKDIR /app
# Copiar dependencias
COPY package*.json ./
# Instalar dependencias
RUN npm install
# Copiar el resto del código
COPY . .
# Exponer el puerto donde corre React
EXPOSE 5173
# Iniciar en modo desarrollo (con hot reload)
CMD ["npm", "run", "dev"]
