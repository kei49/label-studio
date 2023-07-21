# label-studio

## Start by docker-compose

docker-compose up -d

## Start by docker

docker pull heartexlabs/label-studio:latest
docker run -it -p 8080:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest

docker run -it -d -p 8009:8080 -v $(pwd)/mydata:/label-studio/data heartexlabs/label-studio:latest
