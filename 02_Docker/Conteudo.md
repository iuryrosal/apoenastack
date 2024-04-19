# Referências
Projeto de inspiração: https://github.com/brenonogueirasilva/cdc-stream-kafka-datalake

# Comandos
docker build . -f DockerFile -t python_ingestion

docker run python_ingestion

docker-compose up -d 