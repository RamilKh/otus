##################################################################
# Скрипт запуска
##################################################################

#!/bin/bash


echo '';
echo '--- 1. Clean:';
container=`docker ps -a -q --filter="name=otus-docker"`;
docker stop $container;
docker rm $container;
sleep 1;

echo '';
echo '--- 2. Build image:';
docker build -t otus-docker -f Dockerfile .

echo '';
echo '--- 3. Start container:';
docker run -d -p 9002:9002 --name otus-docker otus-docker
sleep 2;

echo '';
echo '--- 4. Result:';
docker ps | grep 'otus-docker';

echo '';
echo '--- 5. Check:';
container_server=`docker ps -q --filter="name=otus-docker"`;
if [ -z $container_server ]; then
	echo 'Error start';
	docker logs -f kov-chat-client
	exit 1;
else
   echo 'Successful starting!';
fi
