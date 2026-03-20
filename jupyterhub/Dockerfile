FROM python:3.11-slim

RUN apt-get update && apt-get install -y nodejs npm curl && \
    npm install -g configurable-http-proxy && \
    apt-get clean

RUN pip install --no-cache-dir \
    jupyterhub==4.1.5 \
    jupyterlab==4.2.0 \
    notebook \
    ipykernel


RUN useradd -m -s /bin/bash admin && \
    echo "admin:admin" | chpasswd

WORKDIR /srv/jupyterhub
COPY jupyterhub_config.py .

EXPOSE 8000

CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]