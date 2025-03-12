FROM jenkins/jenkins:lts

USER root

# Instalar Docker dentro del contenedor de Jenkins
RUN apt-get update && \
    apt-get install -y docker.io

# Cambiar el usuario de vuelta al usuario Jenkins
USER jenkins
