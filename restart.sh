docker rm -f psal-application
docker image rm psal/application
docker build . -t psal/application:latest
docker run -d --restart=always -p 8000:8000 --name psal-application psal/application:latest
