#imagen de Python y distro linux que vamos a usar
FROM python:3.10


# Copia todo lo del directorio en el contenedor
COPY . /app


# Establece el directorio de trabajo en el contenedor
WORKDIR /app


# Corre comandos
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# Expone puerto
EXPOSE 5005

# OPCIÓN 1
# Setear las variables de entorno para Flask
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1
ENV FLASK_RUN_HOST=0.0.0.0

CMD ["sh","run.sh"]