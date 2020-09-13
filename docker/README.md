# OpenCV with Docker

Build docker image using Dockerfile, make sure there is a "Dockerfile" at current directory
<br>`docker build -t <IMAGE-NAME>:<VERSION> .`
<br>e.g. `docker build -t yptheangel/opencv:1.0 .` 

List out available docker images
<br>`docker images`

List out docker containers
<br>`docker ps` (running containers)
<br>`docker ps -a` (all containers)

Enter docker container and use bash
<br>`docker exec -it <CONTAINER-NAME> /bin/bash`

Run docker container in the background
<br>`docker run -it --name <CONTAINER-NAME> --detach <IMAGE-NAME>:<VERSION>`

Start docker container
<br>`docker start <CONTAINER-NAME>` (can also use CONTAINER-ID)

Stop docker container
<br>`docker stop <CONTAINER-NAME>` (can also use CONTAINER-ID)

Remove docker container
<br>`docker rm <CONTAINER-NAME>` (can also use CONTAINER-ID)

Remove docker image
<br>`docker image rm <IMAGE-NAME>`

Run a docker container that uses display because you want to view OpenCV frames
<br>`xhost + `
<br>`docker run --it --rm --net=host --ipc=host -v /tmp/.X11-unix:/tmp/.X11-unix --runtime nvidia --device /dev/video0 -e DISPLAY=$DISPLAY <CONTAINER-NAME>`

 
