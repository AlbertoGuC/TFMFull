FROM jenkins/jenkins:lts

USER root

# Instalar Docker y Kompose dentro del contenedor de Jenkins
RUN apt-get update && \
    #apt-get install -y docker.io curl && \
    #Estos 3 comandos instalan Kompose
    curl -L https://github.com/kubernetes/kompose/releases/latest/download/kompose-linux-amd64 -o /usr/local/bin/kompose && \
    chmod +x /usr/local/bin/kompose && \
    apt-get clean

# Cambiar el usuario de vuelta a Jenkins
USER jenkins
