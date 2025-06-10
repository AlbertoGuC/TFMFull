FROM jenkins/inbound-agent:latest

USER root

RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && \
    mv kubectl /usr/local/bin/

RUN curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 && \
    chmod 700 get_helm.sh && \
    ./get_helm.sh && \
    rm get_helm.sh

RUN curl -L https://github.com/kubernetes/kompose/releases/latest/download/kompose-linux-amd64 -o /usr/local/bin/kompose && \
    chmod +x /usr/local/bin/kompose && \
    apt-get clean

RUN apt-get update && \
    apt-get install -y buildah && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
USER jenkins