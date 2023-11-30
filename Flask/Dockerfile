FROM python:3
WORKDIR /app-flask
ARG PORT_BUILD=5000
ENV port=$PORT_BUILD
EXPOSE $PORT_BUILD
COPY . .
RUN pip install -r requirements.txt
ENTRYPOINT python3 main.py